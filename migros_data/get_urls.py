#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def get_urls(driver):
    temp_url_list = []
    url_list = []
    while True:
        try:
            html_part = driver.execute_script(
                "var element = document.querySelector('body > sm-root > div > main > sm-product > article > sm-list > div > div.content.mdc-layout-grid__inner > div.products.mdc-layout-grid__cell--span-10-phone.mdc-layout-grid__cell--span-12-tablet.mdc-layout-grid__cell--span-9-desktop > div.mdc-layout-grid__inner.product-cards.list.ng-star-inserted'); if (element) {return element.outerHTML;} else {return null;}")

            if not html_part:
                break  # Eğer element bulunamadıysa döngüden çık

            soup = BeautifulSoup(html_part, "html.parser")
            links = soup.find_all('a', href=True)

            for link in links:
                url = link.get('href')
                if url is not None and url not in temp_url_list:
                    temp_url_list.append(url)

            for url in temp_url_list:
                url_list.append("https://www.migros.com.tr/" + url)

            if len(url_list) > 1:
                driver.quit()
                break

        except Exception as e:
            print("Error:", e)
            break

    return url_list
