import time

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from seleniumlogin import force_login

from ..models import BlogPost, Comment


class Test_Functionnal_App_Blog(StaticLiveServerTestCase):
    """Test for read and comment an article"""

    def setUp(self):
        """setUP USer instance and article for blog"""

        self.driver = webdriver.Firefox()
        User.objects.create(
            username="user1", email="user1@user1.com", password="azerty"
        ).save()
        self.user1 = User.objects.get(username="user1")
        BlogPost.objects.create(
            title="Article test 1",
            slug="article-test-1",
            author=self.user1,
            published=True,
            content="Article test 1 Article test 1 Article test 1"
        ).save()
        BlogPost.objects.create(
            title="Article test 2",
            slug="article-test-2",
            author=self.user1,
            published=True,
            content="Article test 2 Article test 2 Article test 2"
        ).save()

    def test_blog_and_article_button(self):
        """Force login , click on blog menu and click on first article button
        """
        force_login(self.user1, self.driver, self.live_server_url)
        self.driver.get(str(self.live_server_url))
        blog_button = self.driver.find_element_by_id('blog')
        blog_button.click()

        redirection_url = self.driver.current_url
        self.assertEquals(self.live_server_url + "/blog/", redirection_url)

        time.sleep(2)

        article_button = self.driver.find_element_by_id('more-article-test-1')
        article_button.click()

        time.sleep(2)

        redirection_url = self.driver.current_url
        self.assertEquals(self.live_server_url + "/blog/article-test-1/", redirection_url)

        time.sleep(2)

        self.driver.quit()

    def test_add_comment_and_count(self):
        old_count_comment = Comment.objects.count()
        force_login(self.user1, self.driver, self.live_server_url)
        self.driver.get(str(self.live_server_url + "/blog/article-test-1/"))
        comment_form = self.driver.find_element_by_xpath('//form[@id = "content" ]')
        content = comment_form.find_element_by_name("content")
        content.send_keys("test commentaire")

        time.sleep(2)

        comment_button = self.driver.find_element_by_id('send')
        comment_button.click()

        time.sleep(2)

        new_count_comment = Comment.objects.count()
        self.assertEquals(new_count_comment, old_count_comment + 1)

