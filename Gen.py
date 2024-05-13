from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import names
from seleniumwire import webdriver
import random
import string 
import time
from selenium.common.exceptions import NoSuchElementException 
import re
import requests
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from onlinesimru import GetFree, GetRent, GetProxy, GetUser, GetNumbers
from onlinesimru import Driver

def gen_name():
    full_name = names.get_full_name().split(" ")
    return full_name[0]+full_name[1]+"_"+''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))



def get_h_id ():
    site_key='4c672d35-0701-42b2-88c3-78380b0db560'
    page_url='https://discord.com/'
    global key
    key = ''
    sol = f"http://2captcha.com/in.php?key={key}&method=hcaptcha&sitekey={site_key}&pageurl={page_url}"
    res = requests.get(sol)
    id = re.findall("OK\|+?(\d+)", str(res.text))
    if res.status_code == 200:
        return id[0]

def auth_number():
    driver = Driver('085f5ed1480a942b6c4eed371d762c94').numbers()
    get = driver.get('Discord')
    print(get)
    state = driver.state()
    return state

def setting():
    username = gen_name()
    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
    
    

    options = {
    'proxy': {
    'http': 'http://fachi1234_gmail_com:6a73f506d4@84.54.11.14:30010',
    'https': 'https://fachi1234_gmail_com:6a73f506d4@84.54.11.14:30010',
    #'no_proxy': 'localhost,127.0.0.1,dev_server:8080'
    }
}

    driver = webdriver.Firefox(seleniumwire_options=options)
    return driver,password,username

def fill_form():
    
    settings = setting()
    driver = settings[0]
    password = settings[1]
    username = settings[2]

    driver.get("https://discord.com/register")
    time.sleep(5)


    def solve():
        id = get_h_id()
        print("Solving Captcha. Can take upto a minute.")
        while True:
            time.sleep(5)
            resq = requests.get(f"http://2captcha.com/res.php?key={key}&action=get&id="+str(id))
            if resq.text != "CAPCHA_NOT_READY":
                tokens = resq.text.split("|")
                #print("Token:", tokens[1])
                token = tokens[1]
                driver.execute_script(
                    f"document.querySelector('iframe').parentElement.parentElement.__reactProps$.children.props.onVerify('{token}')"
                )   
                time.sleep(20)
                break

    driver.find_element(by=By.NAME , value="email").send_keys("s")

    driver.find_element(by=By.NAME , value="username").send_keys(username)

    driver.find_element(by=By.NAME , value="password").send_keys(password)
    print(password)
    Month = driver.find_element(by=By.CLASS_NAME, value='month-1Z2bRu')
    Month.click()
    time.sleep(1)
    random_month = random.randrange(0,11)
    driver.find_element(by=By.XPATH, value=f'id("react-select-2-option-{random_month}")').click()

    driver.find_element(by=By.CLASS_NAME, value="day-1uOKpp").click()
    time.sleep(1)
    random_Day = random.randrange(0,27)
    driver.find_element(by=By.XPATH, value=f'id("react-select-3-option-{random_Day}")').click()

    driver.find_element(by=By.CLASS_NAME, value="year-3_SRuv").click()
    time.sleep(1)
    random_Year = random.randrange(18,30)
    driver.find_element(by=By.XPATH, value=f'id("react-select-4-option-{random_Year}")').click()

    driver.find_element(by=By.CLASS_NAME, value="contents-3ca1mk").click()

    time.sleep(3)
    
    
    url_count = 0
    while url_count == 0:
        url = driver.current_url
        if str(url) == "https://discord.com/register":
            solve()
        else:
            url_count += 1

    input("Press Enter")


    
fill_form()