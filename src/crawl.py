from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup
from config import BASE_LINK, STORAGE_TYPE
from storage import FileStorage, MongoStorage
from parser import AdvertisementDataParser


class CrawlerBase(ABC):
    """Base class for inheritance in other classes"""

    def __init__(self):
        self.storage = self.__set_storage()

    @abstractmethod
    def __set_storage():
        if STORAGE_TYPE == 'mongo':
            return MongoStorage()
        return FileStorage()

    @abstractmethod
    def start(self, store=False):
        pass

    @abstractmethod
    def store(self, data, filename=None):
        pass

    @staticmethod
    def get_page(link):
        """Send GET request to retrieve page content"""
        try:
            response = requests.get(link)
        except requests.HTTPError:
            return None
        return response


class LinkCrawler(CrawlerBase):
    """Retrieve all advertisements links and store them"""

    def __init__(self, cities, link=BASE_LINK):
        self.cities = cities
        self.link = link
        super().__init__()

    @staticmethod
    def find_links(html_doc):
        """Find all advertisements links in html page"""
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup.find_all('a', attrs={'class': 'grd_search_links'})

    def crawl_city(self, url):
        """Crawl and retrieve links in each page"""
        start = 1
        adv_links = list()
        while start <= 50:
            response = self.get_page(url.format(str(start)))
            if response is None:
                continue
            new_links = self.find_links(response.text)
            adv_links.extend(new_links)
            start += 1

        return adv_links

    def start(self, store=False):
        """Start to crawl page"""
        adv_links = list()
        links = self.crawl_city(self.link)
        for link in links:
            link = link['href'][0:39]
            if link not in adv_links:
                adv_links.append(link)
        print(f'Total: {len(adv_links)} link')
        if store:
            self.store([{'url': link, 'flag': False} for link in adv_links])
        return adv_links

    def store(self, data, *args):
        """Store links in database or file"""
        self.storage.store(data, 'advertisements_links')


class DataCrawler(CrawlerBase):
    """Retrieve all advertisements data and store them"""

    def __init__(self):
        super().__init__()
        self.links = self.__load_links()
        self.parser = AdvertisementDataParser()

    def __load_links(self):
        """Load links from mongodb or file for crawl"""
        return self.storage.load('advertisements_links', {'flag': False})

    def start(self, store=False):
        """Start to crawl saved links and retrieve data"""
        for link in self.links:
            response = self.get_page(link['url'])
            data = self.parser.parse(response.text)
            if store:
                self.store(data, data.get('post_id'))
            self.storage.update_flag(link)

    def store(self, data, filename):
        """Store data in database or file"""
        self.storage.store(data, 'advertisement_data')
        print(data['post_id'])
