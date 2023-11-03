
import scrapy
from postscrape.items import Article

class NewsSpider(scrapy.Spider):
    name = "NewsSpider"
    base_domain = "https://www.rouydad24.ir"
    shop_domain = ""
    base_url = "https://www.rouydad24.ir/fa/services/{category}/page/{page}"
    allowed_domains = []
    category_mapping = {
        'economic': 2,
        'politic': 3,
        'society': 4,
        'sport': 5
    }
    def start_requests(self):
        for category_name, category_index in self.category_mapping.items():
            for page_number in range(1, 120):
                yield scrapy.Request(
                    self._format_url(page_number, category_index),
                    self.parse,
                    meta={'category': category_name}
                )

    def _format_url(self, page_number, category_index):
        return self.base_url.format(category=category_index, page=page_number)

    def parse(self, response):
        articles = self._get_items(response)
        subtitles = response.css('.cat_item_subtitle::text').extract()
        category = response.meta['category']
        for article_data, subtitle in zip(articles, subtitles):
            article = Article()
            article['title'] = article_data.css("::text").extract()[0]
            article['category'] = category
            article['uri'] = article_data.css("a::attr(href)").extract()[0]
            article['content'] = subtitle
            yield article

    def _parse_article_page(self, response, article):
        print('xx')
        yield article

    def _get_items(self, response):
        return response.css(".title_list")
