from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
input('Press any key after scanning QR code.')
log_out = driver.find_elements_by_class_name('_3j8Pd')
log_out[2].click()
input('Press any key after menu opened.')
x = driver.find_elements_by_class_name('_3zy-4 Sl-9e')
x[5].click()
