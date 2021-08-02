from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd

chromedriver_path = 'chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('username')
password = webdriver.find_element_by_name('password')
password.send_keys('password')

#xpath bisa didapat dengan inspect element
button_login = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button/div')
button_login.click()
sleep(3)

notnow = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications

#list hashtag yang postnya mau di like
#ini like top post di masing2 post
hashtag_list = ['teknikinformatika']
tag = -1
for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    sleep(5)
    # klik thumbnail pertama
    first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    
    first_thumbnail.click()
    sleep(randint(1,2))    

    #sampai 10 post supaya tidak terlalu banyak
    try:        
        for x in range(1,10):
            #klik like
            button_like = webdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
            button_like.click()
            # button_next = webdriver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a')
            button_next = webdriver.find_element_by_link_text('Next') #klik next post
            button_next.click()
            sleep(randint(1,10))    #diberi jeda agar tidak terlalu seperti bot
    except:
        continue