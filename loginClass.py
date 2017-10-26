"""This doc is created by Godwin vinny carole"""
import time
import threading
from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.keys import Keys


class Login():
    def __init__(self, driver):
        self.endText = '</div></div><script src="./WhatsApp_files/progress.4bd94086ece318669d91782801fa50e3.js.download"></script></body></html>'
        self.htmlData = self.get_html_data()
        if(driver == None):
            self.driver = self.open_driver()
            print("Driver is undefined")
        else:
            self.driver = driver
            print("Driver is defined")
        time.sleep(15)
        self.t1 = ""
        self.timer = 0
        self.currentChat = 0
        self.currentChatName = ""
        self.chatElm = self.driver.find_elements_by_class_name('chat')[
            self.currentChat]
        self.chatElm.click()
        self.currentChatName = self.chatElm.find_elements_by_class_name(
            'chat-title')[0].text
        time.sleep(2)
        self.max_time = 250
        self.time_passed = 0
        self.scrollUp()

    def get_html_data(self):
        with open("./WhatsApp.html", "r") as my_file:
            data = my_file.read()
        return data

    def open_driver(self):
        driver = webdriver.Chrome()
        driver.get('https://web.whatsapp.com')
        driver.execute_script(open("./godwin_new.js").read())
        driver.get('https://web.whatsapp.com')
        return driver

    def scrollUp(self):
        #self.time_passed = 0
        self.t1 = threading.Thread(target=self.Timer)
        self.t1.start()
        print("Thread Started")
        while len(self.driver.find_elements_by_class_name('_1MsrQ')) != 0 and self.time_passed < self.max_time:
            self.driver.execute_script(
                "document.getElementsByClassName('pane-chat-body')[0].scrollTo(0,0);")
            if(self.currentChatName == "Godwin"):
                print(self.currentChatName + "Skipped");
                self.time_passed = self.max_time
        else:
            if(len(self.driver.find_elements_by_class_name('_1MsrQ')) == 0):
                self.time_passed = -2
            else:
                self.time_passed = 0
            f = open(self.currentChatName + ".html", "w", encoding='utf-8')
            f.write(self.htmlData + self.driver.execute_script(
                "return document.getElementById('main').innerHTML") + self.endText)
            f.close()
            self.currentChat += 1
            self.chatElm = self.driver.find_elements_by_class_name('chat')[
                self.currentChat]
            self.chatElm.click()
            self.driver.execute_script(
                "document.getElementsByClassName('chatlist-panel-body')[0].scrollTo(0,document.getElementsByClassName('chatlist-panel-body')[0].scrollTop + 70);")
            self.currentChatName = self.chatElm.find_elements_by_class_name(
                'chat-title')[0].text
            time.sleep(2)
            self.scrollUp()

    def Timer(self):
        while self.time_passed < self.max_time and self.time_passed != -1:
            time.sleep(1)
            self.time_passed += 1
            print(self.time_passed)
        else:
            if(self.time_passed == -1):
                self.time_passed = 0
                print('Finished Scrolling: Going to next chat')
            else:
                print("Time up")
