import json
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
from expires import calculateDurationFromEpoch


mockDate = datetime(2025,8,14)

availableDays = []
loginDuration = [2]


def getlocalStorageObject(driver):
    # ,"inactiveAt":1719663696176,"expiresAt":1719676296157,"updatedAt":1719661896176,
    key = "NRBA_SESSION"
    the_js_script = "return window.localStorage.getItem(\'{}\')".format(key)
    localStorage = driver.execute_script(the_js_script)
    return localStorage


def dateCrawler(groups):

    for month in groups:
        datePickerGroup = month.find_element(By.TAG_NAME, 'tbody')
        days = datePickerGroup.find_elements(By.TAG_NAME, 'td')
        for day in days:
            if (day.get_attribute('data-month')):
                dayLink = day.find_element(By.TAG_NAME, 'a')
                data_day = dayLink.text
                data_month = day.get_attribute('data-month')
                data_year = day.get_attribute('data-year')
                dayFound = datetime(int(data_year), int(data_month), int(data_day))
                #print("bulunan tarih : ", dayFound)
                date_string = dayFound.strftime("%Y-%m-%d")
                # news = "Uygun Tarih Bulundu 😇 {}".format(date_string)
                # messagebox.showwarning("US Citizen Hacking", news)
                if ((len(availableDays) <= 0)):
                    availableDays.append(dayFound) 
                    messageSender("Uygun Tarih Bulundu 😇 {}".format(date_string))

                else:
                    timeDifference = (availableDays[0] - dayFound).days
                    #print("en son bulunan tarihten daha erkene cekilen gun sayısı", timeDifference)
                    if (timeDifference > 0):
                        availableDays[0] = dayFound
                        messageSender("Keşfedilen yeni tarih var! {} son bulunan tarihten {} gun daha yakın😇 ".format(date_string, timeDifference))
                    elif(timeDifference == 0):
                        print("Daha yeni bir tarih bulunamadı😢 , en yakın tarih hala {}".format(date_string))
                        #messageSender("Daha yeni bir tarih bulunamadı😢 , en yakın tarih hala {}".format(date_string))
                        pass
                    else:
                        last_avilable_day = availableDays[0]
                        string_last_day = last_avilable_day.strftime("%Y-%m-%d")
                        messageSender("😢 tarih giderek uzaklaştı. Yeni tarih {}, bir önceki tarih ise {} \'idi ".format(date_string, string_last_day))

                return True

            else:
                pass


def checkMonthByMonth(driver, wait):
    datePickerDivID = "ui-datepicker-div"
    dateNextButtonClass = "ui-datepicker-next"
    # datePickerElement = wait.until(EC.visibility_of_element_located((By.ID,datePickerDivID)))
    nextButtonClicked = True
    while (True):
        if (nextButtonClicked == True):
            datePickerElement = wait.until(EC.visibility_of_element_located((By.ID, datePickerDivID)))
            dateNextButtonElement = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, dateNextButtonClass)))
            datePickerGroupFirst = datePickerElement.find_element(By.CLASS_NAME, "ui-datepicker-group-first")
            datePickerGroupLast = datePickerElement.find_element(By.CLASS_NAME, "ui-datepicker-group-last")
            groups = [datePickerGroupFirst, datePickerGroupLast]
            # firstBody = datePickerGroupFirst.find_element(By.TAG_NAME,'tbody')
            # lastBody = datePickerGroupLast.find_element(By.TAG_NAME,'tbody')
            # days = firstBody.find_elements(By.TAG_NAME, 'td')
            if (dateCrawler(groups=groups)):
                break

            dateNextButtonElement.click()
            nextButtonClicked = False

        else:

            datePickerGroupLast = datePickerElement.find_element(By.CLASS_NAME, "ui-datepicker-group-last")
            groups = [datePickerGroupLast]
            if (dateCrawler(groups=groups)):
                break

            dateNextButtonElement = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, dateNextButtonClass)))
            dateNextButtonElement.click()

        # classNames = day.get_attribute("class").split(" ")

   # print(datePickerGroups)


def tarihBul(driver, wait):

    randevuTarihInputID = "appointments_consulate_appointment_date"
   # datePickerDivID = "ui-datepicker-div"
    randevuTarihInputElement = wait.until(EC.element_to_be_clickable((By.ID, randevuTarihInputID)))

    randevuTarihInputElement.click()
    # datePickerElement = wait.until(EC.presence_of_element_located((By.ID,datePickerDivID)))
    # tumTarihler = driver.find_elements(By.TAG_NAME,'td')
    # checkMonthByMonth()


def randevuZamanla(driver, wait):

    konsulateLeftID = "consulate_left"
    konsoloslukElement = wait.until(EC.element_to_be_clickable((By.ID, konsulateLeftID)))

    consulateAddressID = "appointments_consulate_address"
    consulateAddressElement = wait.until(EC.invisibility_of_element_located((By.ID, consulateAddressID)))
    selectElement = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "select")))
    # selectElement.click()
    clickableOptions = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "option")))
    options = konsoloslukElement.find_elements(By.TAG_NAME, "option")
    time.sleep(4)
    if (consulateAddressElement):
        for option in options:
            if (option.text == "Istanbul"):
                time.sleep(1)
                selectElement.click()
                time.sleep(2)
                option.click()
                time.sleep(2)
                selectElement.click()

    # istanbulOption = next(option for option in options if option.text == "Istanbul")
    # driver.implicitly_wait(2)
    # istanbulOption.click()


def basvuruSahibiSec(driver, wait):
    devametXpath = "/html/body/div[4]/main/div[3]/form/div[2]/div/input"
    devamEtElement = wait.until(EC.element_to_be_clickable((By.XPATH, devametXpath)))
    devamEtElement.click()


def randevuYenidenZamanla(driver, wait):
    randevuYenidenZamanla1Xpath = "/html/body/div[4]/main/div[2]/div[2]/div/section/ul/li[4]/a"
    randevuYenidenZamanla2Xpath = "/html/body/div[4]/main/div[2]/div[2]/div/section/ul/li[4]/div/div/div[2]/p[2]/a"
    yenidenZamanla1Element = wait.until(EC.element_to_be_clickable((By.XPATH, randevuYenidenZamanla1Xpath)))
    yenidenZamanla1Element.click()
    yenidenZamanla2Element = wait.until(EC.element_to_be_clickable((By.XPATH, randevuYenidenZamanla2Xpath)))
    yenidenZamanla2Element.click()


def mevcutDurum(driver, wait):
    devamEtXpath = "/html/body/div[4]/main/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/ul/li/a"
    devamEtElement = wait.until(EC.element_to_be_clickable((By.XPATH, devamEtXpath)))
    devamEtElement.click()



def checkReLoginAsk(driver, wait):
    alertXpath = "/html/body/div[7]/div[2]/div"
    alertClass = "alert"

    alertButtonOKXpath = "/html/body/div[7]/div[3]/div/button"
    alertClass = "ui-button"
    try:
        alertBool = driver.find_element(By.XPATH, alertXpath)
    except:
        print("element yok")
    else:
        alertButton = wait.until(EC.element_to_be_clickable((By.XPATH,alertButtonOKXpath)))
        alertButton.click()

def login(username, password, driver, wait):

    emailXpath = "/html/body/div[5]/main/div[3]/div/div[1]/div/form/div[1]/input"
    passwordXpath = "/html/body/div[5]/main/div[3]/div/div[1]/div/form/div[2]/input"
    checkboxXpath = "/html/body/div[5]/main/div[3]/div/div[1]/div/form/div[3]/label"
    loginXpath = "/html/body/div[5]/main/div[3]/div/div[1]/div/form/p[1]/input"
    emailElement = wait.until(EC.presence_of_element_located((By.XPATH, emailXpath)))
    passwordElement = wait.until(EC.presence_of_element_located((By.XPATH, passwordXpath)))
    checkboxElement = wait.until(EC.element_to_be_clickable((By.XPATH, checkboxXpath)))
    loginElement = wait.until(EC.element_to_be_clickable((By.XPATH, loginXpath)))
    # element = driver.find_element_by_xpath(emailXpath)
    emailElement.send_keys(username)
    passwordElement.send_keys(password)
    checkboxElement.click()
    loginElement.click()
    #checkReLoginAsk(driver=driver,wait=wait)

def loginExpire(driver):
    localStorageObject = getlocalStorageObject(driver=driver)
    json_data = json.loads(localStorageObject)
    expiresEpoch = json_data["inactiveAt"]
    kalanSure = calculateDurationFromEpoch(expiresEpoch)
    loginDuration[0] = kalanSure


def checkReLoginAsk(driver, wait):
    alertXpath = "/html/body/div[7]/div[2]/div"
    alertClass = "alert"

    alertButtonOKXpath = "/html/body/div[7]/div[3]/div/button"
    alertClass = "ui-button"
    try:
        alertBool = driver.find_element(By.XPATH, alertXpath)
    except:
        print("element yok")
    else:
        alertButton = wait.until(EC.element_to_be_clickable((By.XPATH,alertButtonOKXpath)))
        alertButton.click()


def noLoginNeed(driver, wait):
    basvuruSahibiSec(driver=driver, wait=wait)
    randevuZamanla(driver=driver, wait=wait)
    tarihBul(driver=driver, wait=wait)
    checkMonthByMonth(driver=driver, wait=wait)


def all_steps_of_program(driver, wait):
    driver = driver
    wait = wait
    login("me....dilek@hotmail.com","M....0**", driver=driver, wait=wait)
    mevcutDurum(driver=driver, wait=wait)
    # check localstorage
    loginExpire(driver=driver)
    randevuYenidenZamanla(driver=driver, wait=wait)
    basvuruSahibiSec(driver=driver, wait=wait)
    randevuZamanla(driver=driver, wait=wait)
    tarihBul(driver=driver, wait=wait)
    checkMonthByMonth(driver=driver, wait=wait)


def main_program():

    try:
    
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 6)
        counter = 0
        while True:
           
            try:
                print("loginDuration : ",loginDuration[0])
                
                if ((loginDuration[0] <= 2)):
                    driver.get('https://ais.usvisa-info.com/tr-tr/niv/users/sign_in')
                    checkReLoginAsk(driver=driver,wait=wait)
                    wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "mainContent")))
                    all_steps_of_program(driver=driver, wait=wait)
                    counter = 0
                    # driver.close()
                elif(counter >= 3):
                    print("coutner 4 olduuuu")
                    driver.quit()
                    loginDuration[0] = 0
                    counter = 0
                    break
                else:
                    print("appoitment gelsin")
                    driver.get('https://ais.usvisa-info.com/tr-tr/niv/schedule/58100733/appointment')
                    wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "mainContent")))
                    noLoginNeed(driver=driver, wait=wait)
                    counter = counter + 1

            except Exception as e:
               
                string_e = str(e)
                print("stringe : ", string_e)
                errorMessage = "exception1 {}".format(string_e)
                #messageSender(errorMessage)
                loginDuration[0] = 0
                counter = 0
                driver.quit()
                
                break
       
    except Exception as e:
        print("7")
        # print("there is an exception2 happened : ",e)
        string_e = str(e)
        errorMessage = "exception2 {}".format(string_e)
        #messageSender(errorMessage)
        loginDuration[0] = 0
        counter = 0
    else:
        loginDuration[0] = 0
        counter = 0
        main_program()


main_program()


# driver = webdriver.Chrome()
# wait = WebDriverWait(driver,10)
# driver.get('https://ais.usvisa-info.com/tr-tr/niv/users/sign_in')


#  driver = webdriver.Chrome()
#     wait = WebDriverWait(driver,10)
#     driver.get('https://ais.usvisa-info.com/tr-tr/niv/users/sign_in')
