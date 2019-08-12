import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import secretThings

def login(driver):
    driver.find_element_by_css_selector("#mail").send_keys(secretThings.mail)
    driver.find_element_by_css_selector("#password").send_keys(secretThings.password)
    driver.find_element_by_css_selector("#login_btn").click()

def startEtyping(driver):
    #start e-typing
    driver.find_element_by_css_selector("#level_check_member > a").click()
    time.sleep(2)

    driver.switch_to.frame('typing_content')#frameの変更　chrome内に生成されたゲーム画面に移動
    driver.find_element_by_xpath('//div[@id="start_btn"]').click()

    time.sleep(1)

    body = driver.find_element_by_tag_name('body')
    body.send_keys(Keys.SPACE)

    time.sleep(3)

def solveQuestions(driver):
    global questionFlag
    try:
        inputText = driver.find_element_by_xpath('//div[@id="sentenceText"]').find_elements_by_tag_name('span')[1].text
        for sendText in inputText:
            driver.find_element_by_tag_name('body').send_keys(sendText)
            time.sleep(0.01)
        time.sleep(0.7)
    except:
        questionFlag = False
        time.sleep(3)

def main():
    global questionFlag
    questionFlag = True

    #chromeを開く
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://www.e-typing.ne.jp/member/")

    #login
    login(driver)

    #ウィンドウの最大化　省略化
    driver.maximize_window()

    #start e-typing
    startEtyping(driver)

    #回答
    while questionFlag:
        solveQuestions(driver)

    #wait
    input()
    driver.quit()

if __name__ == "__main__":
    main()

