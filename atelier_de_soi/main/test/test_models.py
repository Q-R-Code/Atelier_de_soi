import time

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from seleniumlogin import force_login

from ..models import NewsPost


class Test_Functionnal_App_Main_News(StaticLiveServerTestCase):
    """Test for read a news"""

    def setUp(self):
        """setUP USer instance and news for home"""

        self.driver = webdriver.Firefox()
        User.objects.create(
            username="user1", email="user1@user1.com", password="azerty"
        ).save()
        self.user1 = User.objects.get(username="user1")
        NewsPost.objects.create(
            title="news test 1",
            slug="news-test-1",
            author=self.user1,
            published=True,
            content="News test 1 News test 1 News test 1  News test 1"
        ).save()


    def test_news_button(self):
        """Force login , click on "Actualité" menu and click on first news, read more button
        """
        force_login(self.user1, self.driver, self.live_server_url)
        self.driver.get(str(self.live_server_url))
        news_button = self.driver.find_element_by_id('news')
        news_button.click()

        redirection_url = self.driver.current_url
        self.assertEquals(self.live_server_url + "/#Actus", redirection_url)

        time.sleep(2)

        read_more_button = self.driver.find_element_by_id('read-more-news-test-1')
        read_more_button.click()

        time.sleep(2)

        redirection_url = self.driver.current_url
        self.assertEquals(self.live_server_url + "/accueil/news-test-1/", redirection_url)

        time.sleep(2)

        self.driver.quit()


