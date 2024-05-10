from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import init_driver as id


def data_scraping_product_names(url_list):
    product_names_dict = {"product_name": [],
                          "product_image": []}
    display = 0
    for url in url_list:
        print(display)

        driver = id.init_driver(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h3')))
        html_part = driver.execute_script(
            'var element =document.querySelector("body > sm-root > div > main > sm-product > article > sm-product-detail-page > div.product-detail-page.ng-star-inserted > div.product-detail-wrapper"); if (element) {return element.outerHTML;} else {return null;} ')
        soup = BeautifulSoup(html_part, "html.parser")
        product_image = soup.find('img').get('src')
        product_name = soup.find('h3').text
        product_names_dict["product_name"].append(product_name)
        product_names_dict["product_image"].append(product_image)
        driver.quit()

        display += 1


    return product_names_dict;