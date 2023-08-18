import scrapy
from Webscraper.items import WebscraperItem

class SpidermobileSpider(scrapy.Spider):
    name = "spidermobile"
    allowed_domains = ["pricebaba.com"]
    start_urls = ["https://pricebaba.com/mobile/pricelist/all-mobiles-sold-in-india"]

    def parse(self, response):
        product_urls = response.css("a.productSKULink ::attr(href)").getall()
        for product in product_urls :
            yield response.follow(product,callback = self.parse_product)
        for i in range(2,3):
            next_page_url = "https://pricebaba.com/mobile/pricelist/all-mobiles-sold-in-india?page=" + f"{i}" 
            yield response.follow(next_page_url,callback = self.parse)
        

    def parse_product(self,response) :
        prod_data = WebscraperItem()
        prod_price = response.css("div.txt-xl span ::text").get()
        prod_price = int(prod_price.replace("Rs.","").strip().replace(",",""))
        product_availability  = response.css("div.txt-clr-grey ::text").get()
        ref_prod_avail = response.css("div.txt-clr-grey ::text").get().split(":")

        if ref_prod_avail[1].strip() != 'Upcoming' and prod_price > 9999 :
        
            prod_url = response.url
            prod_name = response.css("h1.txt-wt-b ::text").get()
            prod_brand = response.css("a.txt-clr-brand ::text").get()
            prod_star = response.css("div.txt-m span ::text").get()
            try : 
                prod_star = float(prod_star)
                prod_no_of_ratings = response.css("span.txt-wt-b ::text").get()
            except ValueError :
                prod_star = 0.0
                prod_no_of_ratings = "0"
                                
            prod_specs_list = response.css("div#keyspecificationsTab ::text").getall()
            try :
                oper_sys = prod_specs_list[prod_specs_list.index(" Operating System ") + 1]
            except ValueError :
                oper_sys = ""   
            try :
                display =  prod_specs_list[prod_specs_list.index(" Display ") + 1]
            except ValueError :
                display = ""
            try :
                perform = prod_specs_list[prod_specs_list.index(" Performance ") + 1]
            except ValueError :
                perform = ""
            try :
                battery = prod_specs_list[prod_specs_list.index(" Battery ") + 1] 
            except ValueError :
                battery = ""
            try : 
                connectivity = prod_specs_list[prod_specs_list.index(" Connectivity ") + 1]
                      
            except ValueError :
                connectivity = ""
            try :
                camera_back = prod_specs_list[prod_specs_list.index(" Camera ") + 1] 
                if prod_specs_list[prod_specs_list.index(" Camera ") + 2] != " Battery " : 
                    camera_front = prod_specs_list[prod_specs_list.index(" Camera ") + 2]
                else :
                    camera_front = ""                      
            except ValueError :
                camera_back = ""
                camera_front = ""
            try:
                spcl_feat = "|".join(prod_specs_list[prod_specs_list.index(" Special Features ") + 1 : ] )
            except ValueError :
                spcl_feat = ""    
            full_spec_list = response.css("div#specificationsTab ::text").getall() 
            try :
                ref_rate = full_spec_list[full_spec_list.index("Refresh Rate") + 1]
            except ValueError :
                ref_rate = ""
            try :
                ram = full_spec_list[full_spec_list.index("RAM") + 1]   
            except ValueError :
                ram = ""
            try :
                rom = full_spec_list[full_spec_list.index("Internal Storage") + 1] 
            except :
                rom = ""
            try  :
                launch_date = full_spec_list[full_spec_list.index("Launched in:\xa0") + 1]  
            except ValueError :
                launch_date = ""       


            prod_data["prod_name"] = prod_name
            prod_data["prod_brand"] = prod_brand
            prod_data["prod_price"] = prod_price
            prod_data["prod_star"] = prod_star
            prod_data["prod_no_of_ratings"] = prod_no_of_ratings
            prod_data["product_availability"] = product_availability
            prod_data["oper_sys"] = oper_sys
            prod_data["ram"] = ram
            prod_data["in_store"] = rom
            prod_data["battery"] = battery
            prod_data["display"] = display
            prod_data["connectivity"] = connectivity
            prod_data["perform"] = perform
            prod_data["features"] = spcl_feat
            prod_data["rear_camera"] = camera_back
            prod_data["front_camera"] = camera_front
            prod_data["refresh_rate"] = ref_rate
            prod_data["prod_url"] = prod_url
            prod_data["launch_date"] = launch_date

            yield prod_data    

    
             

            

                  
