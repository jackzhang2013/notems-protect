from selenium import webdriver
from selenium.webdriver.chrome.service import Service # 这里中的chrome要改成你自己的
from selenium.webdriver import Keys
from time import sleep
import pyperclip

driver_path = r'D:\software\Miniconda\envs\font\chromedriver-win64\chromedriver-win64\chromedriver.exe' # 改成你自己的webdriver的位置

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

    while True:
        element.clear()
        element.send_keys(Keys.CONTROL, 'v')
        sleep(1)