import time
from selenium import webdriver
import logging
import sys


def main():
    try:debugLevel = int(sys.argv[1])
    except:debugLevel = 0

    if debugLevel == 1:
        logging.basicConfig(level=logging.DEBUG)
    elif debugLevel == 2:
        logging.basicConfig(level= logging.WARNING)
    else:
        logging.basicConfig(level=logging.CRITICAL)

    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://www.e-typing.ne.jp/member/")
    logging.debug("show browser of eTyping")
    driver.find_element_by_id("#mail").send_keys("strings")
    try:
        # driver.find_element_by_xpath('//div[@id="start_btn"]').click()
        # start
        start_button1 = driver.find_element_by_xpath("//a[@title='腕試しレベルチェック']")
        start_button1.click()
        logging.debug("click is succeeded")
    except:
        driver.quit()
        logging.debug("click is failed")
    time.sleep(10)

    # try:
    #     driver.find_element_by_xpath("").click()
    #     logging.debug("click is succeeded")
    # except:
    #     logging.debug("=====click is failed=====")
    #     driver.quit()

    # text = driver.find_element_by_css_selector('#register-email')
    # print(text.get_attribute("placeholder"))
    # textのときは.text
    # それ以外は.get_attribute
    driver.quit()
    logging.debug('====DONE====')

if __name__ == "__main__":
    try:main()
    except(KeyboardInterrupt):pass
    except:pass

