from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import threading


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

endText = '</div></div><script src="./WhatsApp_files/progress.4bd94086ece318669d91782801fa50e3.js.download"></script></body></html>'
data = ""
with open("./WhatsApp.html","r") as myFile:
    data = myFile.read()
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
driver.execute_script(open("./godwin_new.js").read())
driver.get('https://web.whatsapp.com')
time.sleep(15)
currentChat = 0
currentChatName = ""
chatElm = driver.find_elements_by_class_name('chat')[currentChat]
chatElm.click()
currentChatName = chatElm.find_elements_by_class_name('chat-title')[0].text
time.sleep(2)
# driver.find_elements_by_class_name('pane-chat-body')[0].click()

def scrollUp():
    while len(driver.find_elements_by_class_name('_1MsrQ')) != 0:
        driver.execute_script("document.getElementsByClassName('pane-chat-body')[0].scrollTo(0,0);")
        #driver.find_elements_by_class_name('pane-chat-body')[0].send_keys(Keys.ARROW_UP)
    else:
        print('Finished Scrolling: Going to next chat')
        global data
        global chatElm
        global currentChatName
        global currentChat
        global endText

        f = open(currentChatName+".html", "w",encoding='utf-8')
        f.write(data+driver.execute_script("return document.getElementById('main').innerHTML")+endText)
        f.close()
        currentChat += 1
        driver.execute_script("document.getElementsByClassName('chatlist-panel-body')[0].scrollTo(0,document.getElementsByClassName('chatlist-panel-body')[0].scrollTop + 70);");
        chatElm = driver.find_elements_by_class_name('chat')[currentChat]
        chatElm.click()
        currentChatName = chatElm.find_elements_by_class_name('chat-title')[0].text
        time.sleep(2)
        scrollUp()


scrollUp()
