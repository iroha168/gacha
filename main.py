from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import nose.tools as nose
import string
import random
import csv

class Gacha:
    def exe(self):
        self.wait.until(ec.presence_of_all_elements_located)
        prize_img = self.driver.find_element_by_id('won_the_prize_img')
        next_img = prize_img.get_attribute('src')
        if next_img + '\n' not in self.nimgs:
            self.nimgs.append(next_img.strip() + '\n')

            print(next_img.strip())
            return True
        return False

    def f(self):
        user_agent = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36'
        pjs_path = 'node_modules/phantomjs/bin/phantomjs'
        dcap = {
            "phantomjs.page.settings.userAgent" : user_agent,
            'marionette' : True
        }
        m = open('mails.txt', 'r')
        mail_addresses = m.readlines()
        for mail_address in mail_addresses:
            #mail_address = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(10)])+'@gmail.com'

            self.driver = webdriver.PhantomJS(executable_path=pjs_path, desired_capabilities=dcap)
            url = 'https://ragnarok.skylinematrix.com/lot/lottery/lottery.html'
            self.driver.get(url)

            self.wait = WebDriverWait(self.driver, 5)
            self.wait.until(ec.presence_of_all_elements_located)

            btn = self.driver.find_element_by_class_name('yu_yue')
            btn.click()
            self.wait.until(ec.presence_of_all_elements_located)
            mail = self.driver.find_element_by_id('tail_username')
            mail_address = mail_address.lower()
            print(mail_address)
            mail.clear()
            mail.send_keys(mail_address)
            mail_submit = self.driver.find_element_by_id('tail_submit')
            mail_submit.click()
            self.wait.until(ec.presence_of_all_elements_located)
            btn.click()
            self.wait.until(ec.presence_of_all_elements_located)
            onemore = self.driver.find_element_by_id('won_the_prize_button_continue')

            with open('img.txt', 'r') as f:
                self.nimgs = f.readlines()

            for i in range(10):
                """
                if i == 10 or ( i > 10 and i % 5 == 0):
                    self.driver.find_element_by_css_selector('.tc_share > p:nth-child(1)')
                    self.wait.until(ec.presence_of_all_elements_located)
                    self.driver.find_element_by_css_selector('.tc_close')
                    self.wait.until(ec.presence_of_all_elements_located)
                    btn.click()
                    self.wait.until(ec.presence_of_all_elements_located)
                    print(i)
                """
                try:
                    onemore.click()
                except Exception:
                    break
                if(self.exe()):
                    return

            f.close()

            with open('img.txt', 'w') as f:
                for img in self.nimgs:
                    f.write(img)

gacha = Gacha()
gacha.f()
