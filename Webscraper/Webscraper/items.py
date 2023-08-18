# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebscraperItem(scrapy.Item):
    # define the fields for your item here like:
    prod_name = scrapy.Field() 
    prod_brand = scrapy.Field()
    prod_price = scrapy.Field()
    prod_star = scrapy.Field()
    prod_no_of_ratings = scrapy.Field()
    product_availability = scrapy.Field()
    oper_sys = scrapy.Field()
    ram = scrapy.Field() 
    in_store = scrapy.Field()
    battery = scrapy.Field()
    capacity = scrapy.Field()
    fast_charge = scrapy.Field()
    display = scrapy.Field()
    connectivity = scrapy.Field()
    perform = scrapy.Field()
    features = scrapy.Field()
    rear_camera = scrapy.Field()
    front_camera = scrapy.Field()
    refresh_rate = scrapy.Field()
    prod_url = scrapy.Field()
    launch_date = scrapy.Field()
    

