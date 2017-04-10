from selenium import webdriver
ff = "C:\\Users\\DELL\\Downloads\\geckodriver.exe"
email = input('Enter you E-mail')
password = input('Enter your password')
browser = webdriver.Firefox(executable_path=ff)
browser.get('https://facebook.com')
emailElem = browser.find_element_by_id('email')
emailElem.send_keys(email)
passwordElem = browser.find_element_by_id('pass')
passwordElem.send_keys(password)
login = browser.find_element_by_id('loginbutton')
login.click()
