from selenium import webdriver
import datetime
import time
#def SUG_delete_previous(driver,start_date):

#def SUG_extend_dates(driver,end_date):

user_email = "lasaterclan@gmail.com"
user_pword = "Retrograd3#3"
homepage = "https://signupgenius.com"
loginpage = homepage + "/register"
signupname = "AlanSignup"
cutoff_date = datetime.date(2021,1,1)

driver = webdriver.Chrome()
driver.get(loginpage)

username = driver.find_element_by_id("email")
username.clear()
username.send_keys(user_email)

password = driver.find_element_by_id("pword")
password.clear()
password.send_keys(user_pword)

driver.find_element_by_name("submit").click()

# Find the edit button for the requested signup
signups = driver.find_elements_by_xpath("//*[@id=\"signUpLists\"]/div[1]/div/div/table/tbody/tr")
i = 1
for su in signups:
    if signupname in su.text:
        break
    else:
        i += 1
driver.find_element_by_xpath("//*[@id=\"signUpLists\"]/div[1]/div/div/table/tbody/tr[" + str(i) + "]/td[4]/div/div[1]/a").click()
time.sleep(2)

# Navigate to slots menu and select multiple dates
tab_buttons = driver.find_element_by_class_name("btn-tabs")
tab_buttons = tab_buttons.find_elements_by_css_selector("*")
tab_buttons[1].click()
time.sleep(2)
multiple_dates_box = driver.find_element_by_xpath("//*[@id=\"wizardStepContainer\"]/form/div/div[2]/div/div/div/table[1]/thead/tr[2]/th[3]/span/a/span").click()
driver.find_element_by_xpath("//*[@id=\"wizardStepContainer\"]/form/div/div[2]/div/div/div/table[2]/tfoot/tr/td/div/div[3]/ng-include/items-per-page/ul/li[4]")

# Run through all the dates/times, if it is before the requested start time, select the delete button
signup_slots = driver.find_elements_by_xpath("//*[@id=\"wizardStepContainer\"]/form/div/div[2]/div/div/div/table[1]/tbody/tr")

i = 0
for slot in signup_slots:
    i += 1
    slot_date = datetime.date(int(slot.text[6:10]),int(slot.text[0:2]),int(slot.text[3:5]))
    if slot_date < cutoff_date:
        chk = slot.find_element_by_xpath("//*[@id=\"wizardStepContainer\"]/form/div/div[2]/div/div/div/table[1]/tbody/tr[" + str(i) + "]/td[3]/span/label")
        chk.location_once_scrolled_into_view
        chk.click()


driver.find_element_by_xpath("//*[@id=\"wizardStepContainer\"]/form/div/div[2]/div/div/div/table[1]/thead/tr[1]/th[1]/div/div/div[2]/span/button[3]").click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@id=\"wizardStepContainer\"]/form/div/div[2]/div[1]/div/div/div[3]/div[4]/div/div/button").click()
driver.close()