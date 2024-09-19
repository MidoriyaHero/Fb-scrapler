from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options
import pandas as pd
import re
from IPython.display import clear_output
import pickle
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def ini_chrome(web_link):
    options = Options()
    
    user = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    # options.add_argument('--headless=new')
    # options.add_argument(f'user-agent={user}')
    # options.add_argument(f'--allow-third-party-cookies')
    # options.add_argument(f'--disable-web-security')
    # options.add_argument(f'--disable-incognito')
    # options.add_argument(f'--disable-site-isolation-trials')
    # options.add_argument('--no-sandbox')

    service  = Service(executable_path=r"~\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver= webdriver.Chrome(options = options,service=service)
    
    #driver = uc.Chrome(use_subprocess=True, options=options)
    driver.get(web_link)
    
    return driver

### GET COOKIE CỦA FB
# 1. Open faceboook
browser = ini_chrome("http://facebook.com")

# 2. Truy to login

txtUser = browser.find_element(by = "id", value = "email")
txtUser.send_keys("YOUR EMAIL")

txtPassword = browser.find_element(by = "id", value = "pass")
txtPassword.send_keys("YOUR PASSWORD")

txtPassword.send_keys(Keys.ENTER)

time.sleep(10)

pickle.dump(browser.get_cookies(), open("my_cookie.pkl","wb"))

browser.close()

##### LOAD COOKIES AND AUTO LOGIN
service  = Service(executable_path=r"~\chromedriver-win64\chromedriver-win64\chromedriver.exe")
browser= webdriver.Chrome(service=service)
browser.get("https://fb.com")
# 2.Load cookie from file
time.sleep(5)
cookies = pickle.load(open("my_cookie.pkl","rb"))
for cookie in cookies:
    browser.add_cookie(cookie)

# 3. Refresh the browser
browser.get("https://fb.com")
browser.close()
