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
    print(i)
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name("_3M-N-")
    button.click()
while(1):
    print('Do you want to send message again?')
    k = input("If yes enter 'Y' or 'y' and for no enter 'N' or 'n': ")
    if k == 'y' or k == 'Y':
        name = input('Enter the name of the user or group: ')
        msg = input('Enter the message: ')
        count = int(input('Enter the count: '))
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()
        msg_box = driver.find_element_by_class_name("_13mgZ")
        for i in range(count):
            print(i)
            msg_box.send_keys(msg)
            button = driver.find_element_by_class_name("_3M-N-")
            button.click()
    elif(k=='n' or k=='N'):
        print('Thank you for using.')
        log_out = driver.find_elements_by_class_name('_3j8Pd')
        log_out[2].click()
        pp = driver.find_element_by_class_name('_3zy-4 Sl-9e')
        pp[0].click()
        break
    else:
        print('Invalid Input')
        break
