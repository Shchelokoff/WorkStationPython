import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

"""запуск браузера Chrome"""
driver = webdriver.Chrome(executable_path='C:\\Users\\shche\\PycharmProjects\\pythonSelenium\\chromedriver.exe')
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
print('браузер Chrome запущен')

"""авторизация"""
loggin1 = 'standard_user'
password_all = 'secret_sauce'
username = driver.find_element(By.XPATH, "//*[@id='user-name']")
username.send_keys(loggin1)
print('ввод логина')
password = driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys(password_all)
print('ввод пароля')
password.send_keys(Keys.RETURN)
print('в поле для ввода пароля клавиатурой нажали ENTER')

"""помещаем в корзину первый товар"""
product1 = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
value_Product1 = product1.text
print(f'название первого продукта: {value_Product1}')
price_Product1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_Product1 = price_Product1.text
print(f'цена первого продукта: {value_price_Product1}')
button_add_to_cart_product1 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
button_add_to_cart_product1.click()
print('добавили в корзину первый товар')

"""помещаем в корзину второй товар"""
action = ActionChains(driver)
Photo_red_T_short = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[6]/div[2]')
action.move_to_element(Photo_red_T_short).perform()
time.sleep(4)
print(f'скроллим до фото второго товара')
product2 = driver.find_element(By.XPATH, '//*[@id="item_3_title_link"]/div')
value_Product2 = product2.text
print(f'название второго продукта: {value_Product2}')
price_Product2 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div')
value_price_Product2 = price_Product2.text
print(f'цена второго продукта: {value_price_Product2}')
button_add_to_cart_product2 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
button_add_to_cart_product2.click()
print('добавили в корзину второй товар')

"""информация о товарах в корзине"""
button_cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
button_cart.click()
print('перешли в корзину')
cart_product1 = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
cart_value_Product1 = cart_product1.text
print(f'название первого продукта в корзине: {cart_value_Product1}')
assert value_Product1 == cart_value_Product1
print(f'название первого товара в корзине идентично названию на главной странице')
cart_price_Product1 = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
cart_value_price_Product1 = cart_price_Product1.text
print(f'цена первого продукта в корзине: {cart_value_price_Product1}')
assert value_price_Product1 == cart_value_price_Product1
print(f'цена первого товара в корзине идентична цене на главной странице')
cart_product2 = driver.find_element(By.XPATH, '//*[@id="item_3_title_link"]/div')
cart_value_Product2 = cart_product2.text
print(f'название второго продукта в корзине: {cart_value_Product2}')
assert value_Product2 == cart_value_Product2
print(f'название второго товара в корзине идентично названию на главной странице')
cart_price_Product2 = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
cart_value_price_Product2 = cart_price_Product2.text
print(f'цена второго продукта в корзине: {cart_value_price_Product2}')
assert value_price_Product2 == cart_value_price_Product2
print(f'цена второго товара в корзине идентична цене на главной странице')

"""вводим данные пользователя для покупки"""
button_checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
button_checkout.click()
print('перешли на страницу ввода данных пользователя для покупки')
f_name = 'naruto'
s_name = 'uzumaki'
p_code = 'konoha'
first_name = driver.find_element(By.XPATH, '//*[@id="first-name"]')
first_name.send_keys(f_name)
print('ввод имени')
second_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
second_name.send_keys(s_name)
print('ввод фамилии')
postal_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
postal_code.send_keys(p_code)
print('ввод адреса')
button_continue = driver.find_element(By.XPATH, '//*[@id="continue"]')
button_continue.click()
print('перешли на страницу для покупки')

"""проверка на соответствие расчётной стоимости товаров с фактической без учёта доставки"""
end_price_product1 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_end_price_product1 = end_price_product1.text
end_price_product1_del_symbol_dollar = value_end_price_product1.replace('$', '')
end_price_product2 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_end_price_product2 = end_price_product2.text
end_price_product2_del_symbol_dollar = value_end_price_product2.replace('$', '')
end_price_item_total = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[5]')
value_end_price_item_total = end_price_item_total.text
summ = float(end_price_product1_del_symbol_dollar) + float(end_price_product2_del_symbol_dollar)
print(f'рассчётная стоимость товаров без учёта доставки: {summ}')
end_price_item_total_del_symbol_dollar = value_end_price_item_total.replace('Item total: $', '')
end_price_item_total_del_symbol_dollar = float(end_price_item_total_del_symbol_dollar)
print(f'фактическая стоимость товаров без учёта доставки: {end_price_item_total_del_symbol_dollar}')
assert summ == end_price_item_total_del_symbol_dollar
print(f'расчётная стоимость товаров соответствует фактической без учёта доставки')
button_finish = driver.find_element(By.XPATH, '//*[@id="finish"]')
button_finish.click()
print('перешли на страницу подтверждающую совершение покупки')