import time
from selenium import webdriver
import logging
import sys
from selenium.webdriver.common.keys import Keys
import secretThings



def main():
    #logging.debugの設定
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

    #ウィンドウの最大化　省略化
    # driver.maximize_window()

    #login
    driver.find_element_by_id("mail").send_keys(secretThings.mail)
    driver.find_element_by_id("password").send_keys(secretThings.password)
    driver.find_element_by_id("login_btn").click()

    #start e-typing
    driver.find_element_by_xpath("// *[ @ id = \"level_check_member\"] / a").click()
    time.sleep(2)
    logging.debug("move to game")

    driver.switch_to.frame('typing_content')#frameの変更　chrome内に生成されたゲーム画面に移動
    driver.find_element_by_xpath('//div[@id="start_btn"]').click()
    logging.debug("ready for game")

    time.sleep(1)

    body = driver.find_element_by_tag_name('body')
    body.send_keys(Keys.SPACE)

    time.sleep(3)
    logging.debug("GO")

    #回答
    while True:
        try:
            inputText = driver.find_element_by_xpath('//div[@id="sentenceText"]').find_elements_by_tag_name('span')[1].text
            # driver.find_element_by_tag_name('body').send_keys(inputText)
            for sendText in inputText:
                driver.find_element_by_tag_name('body').send_keys(sendText)
                time.sleep(0.01)
            logging.debug(inputText)
            time.sleep(0.7)
        except:
            break
        logging.debug("Questioons are done")
    time.sleep(3)

    #wait
    input()
    driver.quit()
    logging.debug('====DONE====')

if __name__ == "__main__":
    try:main()
    except(KeyboardInterrupt):logging.debug("keyinterrupt")
    except:logging.debug("failed")

