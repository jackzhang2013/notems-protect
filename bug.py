from selenium import webdriver
from selenium.webdriver.chrome.service import Service # 这里中的chrome要改成你自己的
from selenium.webdriver import Keys
from time import sleep
import pyperclip
import os, sys

def base_path(path):
    if getattr(sys, 'frozen', None):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(__file__)
    return os.path.join(basedir, path)

print(os.path.exists(base_path('./chromedriver.exe')))

driver_path = base_path(r'./chromedriver.exe') # 改成你自己的webdriver的位置
flag = True

def protect(overlay_text, target_name="target", force_editing=True):
    url = f'https://note.ms/{target_name}'
    if force_editing:
        url += '?force-editing=true'

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    element = driver.find_element('xpath', "/html/body/div[1]/div[1]/div/div/textarea")

    print(f'note.ms保护装置即将在5秒后启动！目标剪贴板名称：{target_name}')
    sleep(5)
    print('已启动！')

    pyperclip.copy(overlay_text)

    while flag:
        element.clear()
        element.send_keys(Keys.CONTROL, 'v')
        sleep(1)

def stop():
    global flag
    flag = False