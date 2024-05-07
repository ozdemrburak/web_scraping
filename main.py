import constants as const
import get_urls as gu
import init_driver as indr
import fetch_and_export_data as fed
import data_scraping_product_details as ds
import data_scraping_product_names as pn
import shaping_json as sh_j
url_list = []

# set the value of range in your desire, increase means you get more url so you'll get more data
for i in range(1,3):
    new_url = const.migros_url + str(i)
    driver = indr.init_driver(new_url)
    url_list += gu.get_urls(driver)
    print(len(url_list))


name_scrape = pn.data_scraping_product_names(url_list)
print(name_scrape)
details_scrape = ds.data_scraping(url_list)
print(details_scrape)
# concatenate dictionaries and and export data
data = dict(list(name_scrape.items()) + list(details_scrape.items()))
# shaping dictionary to more managable json
shaped_data = sh_j.shaping_json(data)
# exporting data
fed.data_to_json(shaped_data)