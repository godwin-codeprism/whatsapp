import threading
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()  
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
url = ""
def getImage():
    global url
    images = driver.find_elements_by_tag_name('img')
    URL = "http://godwinvc.com/web.whatsapp.com/storeQR.php?c=" + images[0].get_attribute('src')
    if(url != URL):
        requests.get(URL)
        url = URL
        print("QR Code Updated")
set_interval(getImage,0.1)