from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import time

def login(log, psswd):
    driver.get("https://memeus.ru/fresh")
    login = driver.find_element_by_xpath("//*[@data-src='/static/images/ee33e8a5171867d3645fa6652317d244.svg']")
    login.click()
    username = driver.find_element_by_id('email')
    username.click()
    username.send_keys(log)
    password = driver.find_element_by_id('pass')
    password.click()
    password.send_keys(psswd)
    login = driver.find_element_by_id('loginbutton')
    login.click()
    driver.get("https://memeus.ru/fresh")
def clicker(timeout):
    while True:
        try:
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            elements = driver.find_elements_by_xpath("//*[@data-src='/static/images/c6fa4cb55a44486e78d54c06bc755e54.svg']")
            for eachItem in elements:
                elements.pop().click()
                time.sleep(3)
            
            time.sleep(timeout)
            driver.get("https://memeus.ru/fresh")
        except selenium.common.exceptions.ElementClickInterceptedException:
            print('Error! Refreshing page.')
            driver.get("https://memeus.ru/fresh")
            continue
        
    #driver.close()
if __name__ == "__main__":
    lg = str(input('Введите имя пользователя: '))
    pss = str(input('Введите пароль: '))
    to = int(input('Введите время на обновление страницы: '))
    driver = webdriver.Firefox(executable_path=r'C:\Python36\geckodriver.exe') # При необходимости изменить путь до драйвера
    login(lg, pss)
    clicker(to)
