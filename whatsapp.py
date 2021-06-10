from selenium import webdriver
def whatsapp(name,msg,count):
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')
    input('Press any key after scanning QR code.')
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_class_name("_2A8P4")
    for i in range(count):
        print(i)
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name("_1E0Oz")
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
            msg_box = driver.find_element_by_class_name("_2A8P4")
            for i in range(count):
                print(i)
                msg_box.send_keys(msg)
                button = driver.find_element_by_class_name("_1E0Oz")
                button.click()
        elif(k=='n' or k=='N'):
            log_out = driver.find_elements_by_class_name('_1XaX-')
            log_out[2].click()
            pp = driver.find_element_by_xpath('//span[aria-label="Log out"]')
            pp.click()
            print('You have been logged out. Thank you for using.')
            break
        else:
            print('Invalid Input')
            break


name = input('Enter the name of the user or group: ')
msg = input('Enter the message: ')
count = int(input('Enter the count: '))
whatsapp(name,msg,count)
