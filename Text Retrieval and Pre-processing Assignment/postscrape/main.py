import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from postscrape.spiders.news_spider import NewsSpider

class CrawlerService:
    def __init__(self, scrapper: scrapy.Spider):
        self.scrapper = scrapper

    def run(self):
        settings = get_project_settings()
        process = CrawlerProcess(settings)
        process.crawl(self.scrapper)
        process.start()


def crawl_specific_site(scrapper):
    CrawlerService(scrapper).run()

crawl_specific_site(NewsSpider)