from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import init_driver as id
from  IPython.display import clear_output


def data_scraping(url_list):
    data = {
        "İşletme Kayıt No": [],
        "Net Miktar (g/ml)": [],
        "İçindekiler": [],
        "Alerjen Uyarısı": [],
        "Gıda İşletmecisi / Üretici / İthalatçı / Dağıtıcı": []
    }

    display = 0
    max_length = 0
    for url in url_list:
        clear_output(wait=True)
        print(display)
        display += 1

        driver = id.init_driver(url)
        element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Ürün Bilgileri")]')))

        if element:
            driver.execute_script("arguments[0].click();", element)

        html_part = driver.execute_script(
            'var element = document.querySelector(".product-description"); if (element) {return element.outerHTML;} else {return null;} ')
        soup = BeautifulSoup(html_part, "html.parser")
        details = soup.find_all('p')
        temp_data = {key: [] for key in data.keys()}

        for option in details:
            strong_tags = option.find_all('strong', string=["İşletme Kayıt No", "Net Miktar (g/ml)", "İçindekiler",
                                                            "Alerjen Uyarısı",
                                                            "Gıda İşletmecisi / Üretici / İthalatçı / Dağıtıcı"])

            for tag in strong_tags:
                text_after_strong = tag.find_next_sibling(string=True)
                temp_data[tag.text].append(text_after_strong.strip())

        for key, value in temp_data.items():
            max_length = max(max_length, len(value))

        # Geçici verileri ana veriye aktarırken eksik verileri boş dize ile dolduralım
        for key, value in temp_data.items():
            data[key].extend(value + ["Bilgi Yok"] * (max_length - len(value)))

        driver.quit()

    return data
