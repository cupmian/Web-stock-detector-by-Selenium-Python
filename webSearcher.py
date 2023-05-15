from selenium import webdriver
from threading import Timer
import time
import requests


def send_wechat(msg):
    # 微信获取pushplus的token
    token = '5d55e646a0b54695a3df37889cb89d5c'
    title = '电脑推送通知'
    content = msg
    template = 'html'
    url = f"https://www.pushplus.plus/send?token={token}&title={title}&content={content}&template={template}"
    print(url)
    r = requests.get(url=url)
    print(r.text)


def button_detector_johntama(driver):
    win1 = driver.window_handles[3]
    driver.switch_to.window(win1)
    print(driver.current_url)
    press = driver.find_element_by_class_name('ec-blockBtn--action')
    print(press.text)

    if press.is_enabled():
        send_wechat("雀魂BD补货了请查看！")
        print("success1")
        return None

    return True


def button_detector_arknights(driver):
    win2 = driver.window_handles[1]
    driver.switch_to.window(win2)
    print(driver.current_url)
    press = driver.find_element_by_class_name('ec-blockBtn--action')
    print(press.text)

    if press.is_enabled():
        send_wechat("明日方舟3rdBOX补货了请查看！")
        print("success2")
        return None

    return True


def button_detector_namie(driver):
    win3 = driver.window_handles[2]
    driver.switch_to.window(win3)
    print(driver.current_url)
    press = driver.find_element_by_class_name('state-instock')
    print(press.text)

    if press.text != "-":
        send_wechat("Namie画册补货了请查看！")
        print("success2")
        return None

    return True


if __name__ == "__main__":
    wd = webdriver.Chrome(r'H:\Chromedriver\chromedriver.exe')
    wd.get('https://www.google.com/')

    # 获得网页句柄.句柄打开序号和具体在数组中排列顺序为逆序，加入新网页时注意从上往下添加
    wd.execute_script('window.open("https://www.melonbooks.co.jp/detail/detail.php?product_id=1731298")')
    wd.execute_script('window.open("https://shop.yostar.co.jp/products/detail/553")')
    wd.execute_script('window.open("https://shop.yostar.co.jp/products/detail/328")')

    # wd.switch_to.window(wd.window_handles[1])
    # print(wd.current_url)

    while button_detector_johntama(wd) and button_detector_arknights(wd) and button_detector_namie(wd):
        time.sleep(10)
