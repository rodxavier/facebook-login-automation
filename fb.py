import random
import string

from selenium import webdriver

import settings
from image_steg import encrypt_image, decrypt_image

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.binary_location=settings.CHROME_EXE
    if settings.MAXIMIZED:
        options.add_argument('--start-maximized')
    if settings.INCOGNITO:
        options.add_argument('--incognito')
    browser = webdriver.Chrome(executable_path=settings.CHROME_DRIVER_PATH, chrome_options=options)
    browser.get('http://facebook.com')

    passwd = decrypt_image(settings.IMAGE_PATH)
    browser.execute_script('document.getElementById("email").value = "%s";' % (settings.EMAIL))
    browser.execute_script('document.getElementById("pass").value = "%s";' % passwd)
    browser.find_element_by_id('login_form').submit()

    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    passwd_length = random.randint(settings.MIN_PASSWORD_LENGTH, settings.MAX_PASSWORD_LENGTH)
    new_passwd = ''.join(random.choice(chars) for x in range(passwd_length))
    encrypt_image(settings.IMAGE_PATH, new_passwd)
    browser.get('https://www.facebook.com/settings?tab=account&section=password&view')
    browser.execute_script('document.getElementById("password_old").value = "%s";' % (passwd))
    browser.execute_script('document.getElementById("password_new").value = "%s";' % (new_passwd))
    browser.execute_script('document.getElementById("password_confirm").value = "%s";' % (new_passwd))
    browser.find_element_by_id('password_old').submit()
