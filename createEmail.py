from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import string
import time
import tempMail


driver = webdriver.Firefox()
driver.get("https://mail.protonmail.com/create/new?language=en")
time.sleep(5)
print(driver.title)
assert "Signup" in driver.title

def gMail():
    session = GuerrillaMailSession()
    print(session.get_session_state()['email_address'])
    print(session.get_email_list()[0].guid)

def enterForm(username,password):
    #Enters Fields and Subits
    iframe = driver.find_element_by_class_name('top')
    driver.switch_to.frame(iframe)
    username_form = driver.find_element_by_id('username')
    username_form.send_keys(username)
    driver.switch_to.default_content()
    password_form = driver.find_element_by_id('password')
    passwordConfirm_form = driver.find_element_by_id('passwordc')
    password_form.send_keys(password)
    password_form.send_keys("\n")
    passwordConfirm_form.send_keys(password)
    iframe = driver.find_element_by_class_name('bottom')
    driver.switch_to.frame(iframe)
    recoverymail = driver.find_element_by_id("notificationEmail")
    recoverymail.send_keys("waborej@marketlink.info")
    submitBtn = driver.find_element_by_name('submitBtn')
    time.sleep(5)
    submitBtn.send_keys(Keys.RETURN)
    time.sleep(5)
    # submitBtn = driver.find_element_by_id("confirmModalBtn")
    # submitBtn.click()
    #driver.close()
    emailRadio = driver.find_element_by_id("id-signup-radio-email")
    '''
    Get selenium to be able to click on the radios for email.
    '''
    print(emailRadio.is_selected())
    time.sleep(5)
    emailVerifyInput = driver.find_element_by_id("emailVerification")
    tempEmail = tempMail.getVerify()
    print(tempEmail)
    emailVerifyInput.send_keys()
    emailVerifyInput.send_keys(Keys.RETURN)

def generateCreds():
    creds = ['','']
    ascii_string = string.ascii_letters
    lower,upper = ascii_string.split('z')
    lower+='z'
    #username
    for i in range(8):
        creds[0] += ''.join(random.choice(ascii_string))
    #password
    for i in range(8):
        creds[1] += ''.join(random.choice(lower+upper+string.digits+string.punctuation))
    return creds

def main():
    creds = generateCreds()

    enterForm(creds[0],creds[1])
    # gMail()
main()
