from selenium import webdriver
from time import sleep
import getpass

class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        driver = self.driver
        self.driver.get('http://github.com')
        sleep(2)

        signin = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]")
        signin.click()

        email_in = driver.find_element_by_xpath('//*[@id="login_field"]')
        email_in.send_keys("goncalo.s.and@gmail.com")

        pw_in = driver.find_element_by_xpath('//*[@id="password"]')
        pw = getpass.getpass("give me your password:")
        pw_in.send_keys(pw)

        login_btn = driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[8]')
        login_btn.click()


    def open_codepad(self):
        self.driver.get('http://codepad.org')

    def select_python(self):
        login_btn = self.driver.find_element_by_xpath('//*[@id="editor-form"]/table/tbody/tr[2]/td[1]/nobr[10]/label/input')
        login_btn.click()

    def write_in_textarea(self, text="print('Hello World')"):
        text_area = self.driver.find_element_by_id('textarea')
        text_area.send_keys(text)

    def submit(self):
        try:
            submit_btn = self.driver.find_element_by_xpath('//*[@id="editor-form"]/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr/td[3]/button')
        except:
            submit_btn = self.driver.find_element_by_xpath('//*[@id="editor-form"]/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr/td[3]/input')
        submit_btn.click()

    def open_imgur(self):
        self.driver.get('https://imgur.com/')



    def take_a_screenshot(self):
        self.driver.save_screenshot("screenshot.png")

    def close(self):
        self.driver.close()