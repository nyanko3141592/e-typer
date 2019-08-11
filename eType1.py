import time
from selenium import webdriver
import logging
import sys
import secretThings


def main():
    #logging.debugの設定　省略可能
    try:debugLevel = int(sys.argv[1])
    except:debugLevel = 0

    if debugLevel == 1:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.CRITICAL)

    #chromeを開く
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://www.e-typing.ne.jp/member/")
    logging.debug("show browser of eTyping")

    #login
    driver.find_element_by_id("mail").send_keys(secretThings.mail)
    driver.find_element_by_id("password").send_keys(secretThings.password)
    driver.find_element_by_xpath("//*[@id=\"login_btn\"]").click()


    driver.quit()
    logging.debug('====DONE====')

if __name__ == "__main__":
    try:main()
    except(KeyboardInterrupt):logging.debug("keyinterrupt")
    except:pass

