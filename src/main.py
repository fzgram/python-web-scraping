from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import StaleElementReferenceException

import os
import time

def is_download_complete(download_dir):
    while True:
        files = os.listdir(download_dir)
        if not files:  # No files in the directory
            time.sleep(1)  # Wait before checking again
            continue
        for filename in files:
            if filename.endswith('.crdownload'):  # Check for incomplete downloads
                break
        else:
            # No .crdownload files found, download is complete
            return True
        time.sleep(1)  # Wait before checking again

def get_data(url: str):
    browser_options = ChromeOptions()
    browser_options.headless = True
    
    download_dir = r"C:\Users\h\Downloads"
    print('your download dir: ', download_dir)

    browser_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,  # Set the download directory
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    
    driver = Chrome(options=browser_options)
    driver.get(url)
    
    # iframe = driver.find_element(By.TAG_NAME, "iframe")
    # driver.switch_to.frame(iframe)

    # wait = WebDriverWait(driver, 10)
    # element = wait.until(EC.element_to_be_clickable((By.ID, "_idJsp2:_idJsp11")))
    
    # print(driver.page_source)
    
    tab = driver.find_element(By.CSS_SELECTOR, 'a#_idJsp5\\:_idJsp14')
    tab.click()
    download_btns_count = len(driver.find_elements(By.LINK_TEXT, "Изтегли броя"))
    
    text = open("./requirements.txt")
    page_count = text.readline().strip().split('=')[1].strip()
    page_count = int(page_count)
    print('page counts: ', page_count)
    text.close()
    
    i = 0
    while i < page_count:
        for j in range(download_btns_count):
            #  because the element is Re-located
            print(f"start {i*download_btns_count + j +1}")
            download_btns = driver.find_elements(By.LINK_TEXT, "Изтегли броя")
            download_btns[j].click()
            print("btn cliked")
            
            popup = driver.find_element(By.PARTIAL_LINK_TEXT, '.rtf')
            popup.click()
            print("popup cliked")
            
            # wait until download has completed.
            is_download_complete(download_dir)
            
            close_btn = driver.find_element(By.CSS_SELECTOR, "img[src='/DVWeb/img/exit.gif'][onclick='hideDownloadModalPanel()']")
            close_btn.click()
            print(f"end {i*download_btns_count + j +1}")
            
        i += 1
        next_btn = driver.find_element(By.LINK_TEXT, "Следваща.. »")
        next_btn.click()
    
    # for book in books:
    #     title = book.find_element(By.CSS_SELECTOR, "h3 > a")
    #     price = book.find_element(By.CSS_SELECTOR, ".price_color")
    #     stock = book.find_element(By.CSS_SELECTOR, ".instock.availability")
    #     book_item = {
    #         'title': title.get_attribute("title"),
    #         'price': price.text,
    #         'stock': stock.text
    #     }
    #     data.append(book_item)

    time.sleep(10)
    driver.quit()


def main():
    get_data("https://dv.parliament.bg/DVWeb/broeveList.faces")
    print("OK")


if __name__ == '__main__':
    main()
