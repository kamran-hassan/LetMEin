from selenium import webdriver
import time
import sys
from os import system



#type you own user name and profile path of firefox  YOU CAN FIND BY TYPING "about:profiles" in your URL area and enter

profile = webdriver.FirefoxProfile(r"C:\Users\YOURUSERNAME\AppData\Roaming\Mozilla\Firefox\Profiles\4yjgz4vv.default-release")
driver = webdriver.Firefox(firefox_profile=profile)
driver.get('https://web.whatsapp.com/')

#Chnage The name Accordingly

AdminList = ['Kamran Airtel']

#it Will log the details to a text file
def LogUpdate(data):
    f = open('logBook.txt','a')
    f.write(time.strftime("%m/%d/%Y, %H:%M:%S") + ": " + data+"\n")
    f.close()


#can be used to clear all the Whats APP chat, I have Not used it anywhere but you may use
def resetInsQueue(d):
    d.find_element_by_xpath('//span[@title = "{}"]'.format(chat)).click()
    d.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/header/div[3]/div/div[2]/div').click()
    d.find_element_by_xpath('/html/body/div[1]/div[1]/span[4]/div/ul/div/div/li[5]/div[1]').click()
    d.find_element_by_xpath('/html/body/div[1]/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/div').click()
    LogUpdate("Clearing the Chat")

#Here Comes the final loop Which runs contineously

Inmeeting = False
old_msg = ""
while True:
    time.sleep(1)
    system('cls')
    for chat in AdminList:
        try:
            driver.find_element_by_xpath('//span[@title = "{}"]'.format(chat)).click()
            instruction = driver.find_elements_by_xpath('//div[@class="_1Gy50"]')


            i = instruction[-1]
            print("Recieved the Instruction :"+i.text)
            s = i.text

            
            if(s.startswith('>>>>>') and s.count('>')==5 and Inmeeting):
                if(s.split(" ")[1] == "END"):
                    Inmeeting = False
                    driver2.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[6]/span/button/i').click()
                    driver2.close();
                    print("\nLeaving the meeting.....'")
                    LogUpdate("Leaving the meeting\n\n\n\n\n")

            
            elif(s.startswith('>>>') and s.count('>')==3 and Inmeeting):
                print('replying to the chat')
                new_msg = s[3:]
                if(old_msg != new_msg):
                    old_msg = new_msg
                    LogUpdate("Replying to the chat with the message= "+new_msg)
                    time.sleep(1)
                    driver2.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[2]/div/div/div[3]/span/button/i[1]').click()
                    time.sleep(1)
                    driver2.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[4]/div[2]/div[2]/div/div[4]/div/div[1]/div[1]/textarea').send_keys(new_msg)
                    time.sleep(1)
                    driver2.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[4]/div[2]/div[2]/div/div[4]/span/button/i').click()
                    time.sleep(1)
                    driver2.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[4]/div[2]/div[1]/div[2]/div/span/button/i').click()
                        #resetInsQueue(driver);

            elif(s.startswith('>') and s.count('>')==1 and Inmeeting==False):
                print('joing meeting')
                link = s.split(" ")[1]
                LogUpdate("joing a meeting with Link ={} ".format(link))
                driver2 = webdriver.Firefox(firefox_profile=profile)
                driver2.get(link)
                time.sleep(10)
                driver2.find_element_by_xpath('/html/body/div/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
                time.sleep(1)
                driver2.find_element_by_xpath('/html/body/div/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div').click()
                time.sleep(1)
                driver2.find_element_by_xpath('/html/body/div/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div/div[1]/span/span').click()
                Inmeeting = True


        except:
            print('Instruction Queue is empty Or some excepion happens.\n')
            print("Whew!", sys.exc_info()[0], "occurred.")

                
                    

