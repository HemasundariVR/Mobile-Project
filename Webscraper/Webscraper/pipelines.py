# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WebscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        ## prod_no_of_ratings --> integer
        try:
            adapter["prod_no_of_ratings"] = int(adapter.get("prod_no_of_ratings").replace(",",""))
        except ValueError :
            adapter["prod_no_of_ratings"] = 0

        ## rear_camera --> float
        try :
            adapter["rear_camera"] = float(adapter.get("rear_camera").split()[0])
        except IndexError :
            adapter["rear_camera"] = 0.0

        ## front_camera --> float
        try :
            adapter["front_camera"] = float(adapter.get("front_camera").split()[0])
        except IndexError :
            adapter["front_camera"] = 0.0


        ## in_store --> float
        try :
            rom_as_str = adapter.get("in_store")
            if "MB" in rom_as_str:
                adapter["in_store"] = float(adapter.get("in_store").split()[0])/1024
            else:
                adapter["in_store"] = float(adapter.get("in_store").split()[0])
        except IndexError :
            adapter["in_store"] = 0.0     


        ## ram --> float
        try :
            ram_as_str = adapter.get("ram")
            if "MB" in ram_as_str :
                adapter["ram"] = float(adapter.get("ram").split()[0])/1024
            else:
                adapter["ram"] = float(adapter.get("ram").split()[0])
        except IndexError :
            adapter["ram"] = 0.0


        ## refresh_rate --> integer
        try :
            adapter["refresh_rate"] = int(adapter.get("refresh_rate").replace("Hz",""))  
        except ValueError :
            adapter["refresh_rate"] = 60  


        ## items --> lowercase
        lower_case_keys = ["prod_name","prod_brand","product_availability","oper_sys","battery","connectivity","perform","features"]
        for dict_key in lower_case_keys :
            adapter[dict_key] = adapter.get(dict_key).lower()


        ## display --> in cm spec
        adapter["display"] = float(adapter.get("display")[adapter.get("display").find("(")+ 1:adapter.get("display").find(")")].replace("cm","").strip())


        ## product_availability --> [in\out of] stock 
        stock_key = adapter.get("product_availability").split(":")[1].strip()
        if stock_key == "out of stock" :
            adapter["product_availability"] = stock_key 
        else :
            adapter["product_availability"] = "in stock" 


        ## launch_date --> from today --> no_of_days
        import datetime
        try :
            lan_date_str = adapter.get("launch_date")
            lan_date_date = datetime.datetime.strptime(lan_date_str,"%B %Y").date()
            today = datetime.datetime.today().date()
            adapter["launch_date"] = (today - lan_date_date).days
        except ValueError :
            adapter["launch_date"] = None


        ## battery --> capacity

        try:
            adapter["capacity"] = float(adapter.get("battery").split()[0])
        except:
            adapter["capacity"] = None

        
        ## battery --> fast charge

        try:
            charger = adapter.get("battery").split()
            if "fast" in charger or "super" in charger or "flash" in charger or "turbo" in charger or "quick" in charger or "hyper" in charger or "warp" in charger or "dart" in charger or "pump" in charger or "sonic" in charger:
                adapter["fast_charge"] = "yes"
            else:
                adapter["fast_charge"] = "no" 
        except:
            adapter["fast_charge"] = None  
   

                        
            
               
        return item
