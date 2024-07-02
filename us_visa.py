
from tkinter import *
from tkinter import messagebox
from datetime import date, datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from discord import messageSender

availableDays = []


datePickerDivID = "ui-datepicker-div"
datePickerNextButton = "ui-datepicker-next"


def dateCrawler(groups):
   
    for month in groups:
        datePickerGroup = month.find_element(By.TAG_NAME,'tbody')
        days = datePickerGroup.find_elements(By.TAG_NAME, 'td')
        for day in days:
            if(day.get_attribute('data-month')):
                dayLink = day.find_element(By.TAG_NAME,'a')
                data_day = dayLink.text
                data_month = day.get_attribute('data-month')
                data_year = day.get_attribute('data-year')
                dayFound = datetime(int(data_year),int(data_month),int(data_day))
                print(dayFound)
                date_string = dayFound.strftime("%Y-%m-%d")
                news = "Uygun Tarih Bulundu 😇 {}".format(date_string)
                messagebox.showwarning("US Citizen Hacking", news)
                if(len(availableDays) <= 0):
                    availableDays.append(dayFound)
                else:
                   timeDifference =  availableDays[0] - dayFound
                   if(timeDifference > 0):
                       print("yeni tarih bulundu")
                       availableDays[0] = dayFound
                return True
                        
            else:
                pass




def checkMonthByMonth():
    print("checkMonthByMonth calisti")
    datePickerDivID = "ui-datepicker-div"
    dateNextButtonClass = "ui-datepicker-next"
    #datePickerElement = wait.until(EC.visibility_of_element_located((By.ID,datePickerDivID)))
    nextButtonClicked = True
    while(True):
        if(nextButtonClicked == True):
            datePickerElement = wait.until(EC.visibility_of_element_located((By.ID,datePickerDivID)))
            dateNextButtonElement = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,dateNextButtonClass)))
            datePickerGroupFirst = datePickerElement.find_element(By.CLASS_NAME,"ui-datepicker-group-first")
            datePickerGroupLast = datePickerElement.find_element(By.CLASS_NAME,"ui-datepicker-group-last")
            groups = [datePickerGroupFirst,datePickerGroupLast]
            #firstBody = datePickerGroupFirst.find_element(By.TAG_NAME,'tbody')
            #lastBody = datePickerGroupLast.find_element(By.TAG_NAME,'tbody')
            #days = firstBody.find_elements(By.TAG_NAME, 'td')
            if (dateCrawler(groups=groups)):
                break
            
            dateNextButtonElement.click()
            nextButtonClicked = False
           
        else:
           
            datePickerGroupLast = datePickerElement.find_element(By.CLASS_NAME,"ui-datepicker-group-last")
            groups = [datePickerGroupLast]
            if(dateCrawler(groups=groups)):
                break

            dateNextButtonElement = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,dateNextButtonClass)))
            dateNextButtonElement.click()
           

    
           
        #classNames = day.get_attribute("class").split(" ")
        

        
   # print(datePickerGroups)
    



def tarihBul():
    count = 0
    randevuTarihInputID = "appointments_consulate_appointment_date"
   # datePickerDivID = "ui-datepicker-div"
    randevuTarihInputElement = wait.until(EC.element_to_be_clickable((By.ID,randevuTarihInputID)))
    
    randevuTarihInputElement.click()
    #datePickerElement = wait.until(EC.presence_of_element_located((By.ID,datePickerDivID)))
    #tumTarihler = driver.find_elements(By.TAG_NAME,'td')
    #checkMonthByMonth()
   
def randevuZamanla():
    
    konsulateLeftID = "consulate_left"
    konsoloslukElement = wait.until(EC.element_to_be_clickable((By.ID,konsulateLeftID)))
    
    consulateAddressID = "appointments_consulate_address" 
    consulateAddressElement = wait.until(EC.invisibility_of_element_located((By.ID,consulateAddressID)))
    selectElement = wait.until(EC.element_to_be_clickable((By.TAG_NAME,"select")))
    #selectElement.click()
    clickableOptions = wait.until(EC.element_to_be_clickable((By.TAG_NAME,"option")))
    options = konsoloslukElement.find_elements(By.TAG_NAME,"option")
    time.sleep(2)
    if(consulateAddressElement):
        for option in options:
            if(option.text == "Istanbul"):
                time.sleep(1)
                selectElement.click()
                time.sleep(1)
                option.click()
                time.sleep(1)
                selectElement.click()
                
    
    #istanbulOption = next(option for option in options if option.text == "Istanbul")
    #driver.implicitly_wait(2)
    #istanbulOption.click()

    


def basvuruSahibiSec():
    devametXpath = "/html/body/div[4]/main/div[3]/form/div[2]/div/input"
    devamEtElement = wait.until(EC.element_to_be_clickable((By.XPATH,devametXpath)))
    devamEtElement.click()


def currentState():
    devamEtXpath = "/html/body/div[4]/main/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/ul/li/a"
    devamEtElement = wait.until(EC.element_to_be_clickable((By.XPATH,devamEtXpath)))
    devamEtElement.click()
 

def randevuYenile():
    randevuYenidenZamanla1Xpath = "/html/body/div[4]/main/div[2]/div[2]/div/section/ul/li[4]/a"
    randevuYenidenZamanla2Xpath = "/html/body/div[4]/main/div[2]/div[2]/div/section/ul/li[4]/div/div/div[2]/p[2]/a"
    yenidenZamanla1Element = wait.until(EC.element_to_be_clickable((By.XPATH,randevuYenidenZamanla1Xpath)))
    yenidenZamanla1Element.click()
    yenidenZamanla2Element = wait.until(EC.element_to_be_clickable((By.XPATH,randevuYenidenZamanla2Xpath)))
    yenidenZamanla2Element.click()



def login():
    pass

def main_program(username, password):
    
    emailXpath = "/html/body/div[5]/main/div[3]/div/div[1]/div/form/div[1]/input"
    passwordXpath = "/html/body/div[5]/main/div[3]/div/div[1]/div/form/div[2]/input"
    checkboxXpath = "/html/body/div[5]/main/div[3]/div/div[1]/div/form/div[3]/label"
    loginXpath = "/html/body/div[5]/main/div[3]/div/div[1]/div/form/p[1]/input"
    emailElement = wait.until(EC.presence_of_element_located((By.XPATH,emailXpath)))
    passwordElement =  wait.until(EC.presence_of_element_located((By.XPATH,passwordXpath)))
    checkboxElement =  wait.until(EC.element_to_be_clickable((By.XPATH,checkboxXpath)))
    loginElement =  wait.until(EC.element_to_be_clickable((By.XPATH,loginXpath)))
    #element = driver.find_element_by_xpath(emailXpath)
    emailElement.send_keys(username)
    passwordElement.send_keys(password)
    checkboxElement.click()
    loginElement.click()
    currentState()
    randevuYenile()
    basvuruSahibiSec()
    randevuZamanla()
    tarihBul()
    checkMonthByMonth()
    time.sleep(10)




driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
driver.get('https://ais.usvisa-info.com/tr-tr/niv/users/sign_in')
main_program("mehmetalperdilek@hotmail.com","MAD1990**")











