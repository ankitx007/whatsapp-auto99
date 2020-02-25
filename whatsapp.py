from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
name = input('Enter the name of the user or group: ')
msg = input('Enter the message: ')
count = int(input('Enter the count: '))
input('Press any key after scanning QR code.')
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
msg_box = driver.find_element_by_class_name("_13mgZ")
for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name("_3M-N-")
    button.click()