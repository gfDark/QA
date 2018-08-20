import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

rand_int = str(random.randint(300, 10000))

#my_email = 'darkdno0+{0}@gmail.com'.format(rand_int) старый формат - форматировани

my_email = f'darkdno0+{rand_int}@gmail.com' # новый формат форматирования

login_random = str(random.randint(10000, 100000))
LOGIN = f"LordAvenusOleg{login_random}"
PASSWORD = "12345678aA"

driver = webdriver.Chrome() # Firefox IE

driver.maximize_window() # на весь экран 

driver.get("https://hotline.ua/register/") # навигация
time.sleep(1) # ожидание в 1 секунду


# Поиск полей
email_field = driver.find_element_by_xpath('//*[@id="reg-form"]/div/div/div[1]/input')
login_field = driver.find_element_by_xpath('//*[@id="reg-form"]/div/div/div[2]/input')
password_field = driver.find_element_by_xpath('//*[@id="passw1"]')
register_button = driver.find_element_by_xpath('//*[@id="submit-button"]')

# заполняем поля
email_field.send_keys(my_email)
login_field.send_keys(LOGIN)
password_field.send_keys(PASSWORD)
register_button.click() # клик


text_after_registration = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div[1]/p[1]').text # аттрибут .text для считывания текста
formated_text = text_after_registration.split(" ")[0]
#print(formated_text)

if formated_text == 'Дла':
	print("Регистрация успешна!")
	driver.close()
else:
	print("Что-то пошло не так!")

time.sleep(3)









