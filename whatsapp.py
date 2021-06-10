from selenium import webdriver
def whatsapp(name,msg,count):
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')
    input('Press any key after scanning QR code.')
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_class_name("_1Plpp")
    for i in range(count):
        print(i)
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name("_35EW6")
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
            msg_box = driver.find_element_by_class_name("_1Plpp")
            for i in range(count):
                print(i)
                msg_box.send_keys(msg)
                button = driver.find_element_by_class_name("_35EW6")
                button.click()
        elif(k=='n' or k=='N'):
            log_out = driver.find_elements_by_class_name('rAUz7')
            log_out[2].click()
            pp = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[6]/div')
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
