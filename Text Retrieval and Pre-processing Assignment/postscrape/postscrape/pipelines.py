# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class PostscrapePipeline:
    def open_spider(self, spider):
        self.data = []

    def close_spider(self, spider):
        with open('../news.json', 'w') as news_file:
            news_file.write(json.dumps(self.data))
        print(self.data)

    def process_item(self, item, spider):
        product_data = ItemAdapter(item).asdict()
        self.data.append(product_data)
        return item