from selenium import webdriver
import time

class InternetSpeedTwitterBot:
    def __init__(self, driven_path):
        self.driver = webdriver.Chrome(executable_path=driven_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go = self.driver.find_element_by_class_name("start-text")
        go.click()
        time.sleep(60)
        self.down = float(self.driver.find_element_by_class_name("download-speed").text)
        self.up = float(self.driver.find_element_by_class_name("upload-speed").text)
        return self.down, self.up

    def tweet_at_provider(self, Promised_down, Promised_up, email, password):
        if Promised_down > self.down or Promised_up > self.up:
            self.driver.get("https://twitter.com/login")

            email_field = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
            email_field.send_keys(email)
            password_field = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
            password_field.send_keys(password)
            login = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
            login.click()

            # Twitting
            time.sleep(10)
            text = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div')
            text.send_keys(f"The speed of the internet is {self.down} for downloading and the uploading speed is {self.up}")
            visibility = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div/span/span')
            visibility.click()
            time.sleep(2)
            only_me = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[3]')
            only_me.click()
            time.sleep(5)
            tweet_btn = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
            tweet_btn.click()

