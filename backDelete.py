from selenium import webdriver
import datetime
import time

def SUGbackDelete(user_email,user_password,signupname,cutoff_date):

    # Login to SignupGenius
    homepage = "https://signupgenius.com"
    loginpage = homepage + "/register"

    driver = webdriver.Chrome()
    driver.get(loginpage)

    username = driver.find_element_by_id("email")
    username.clear()
    username.send_keys(user_email)

    password = driver.find_element_by_id("pword")
    password.clear()
    password.send_keys(user_password)

    driver.find_element_by_name("submit").click()

    # Click the edit button corresponding to the requested signup
    driver.find_element_by_xpath("//*[@id=\"memPgCenter\"]/div/div[2]/div/ul/li[1]/a").click()
    signups = driver.find_elements_by_xpath("//*[@id=\"signUpLists\"]/div[1]/div/div/table/tbody/tr")
    i = 1
    for su in signups:
        if signupname in su.text:
            break
        else:
            i += 1
    edit_button = driver.find_element_by_xpath("//*[@id=\"signUpLists\"]/div[1]/div/div/table/tbody/tr[" + str(i) + "]/td[4]/div/div[1]/a")
    driver.execute_script("arguments[0].scrollIntoView();", edit_button)
    edit_button.click()
    driver.fullscreen_window()
    time.sleep(1)

    # Navigate to slots menu and select the "multiple dates" options
    tab_buttons = driver.find_element_by_class_name("btn-tabs")
    tab_buttons = tab_buttons.find_elements_by_css_selector("*")
    tab_buttons[1].click()
    time.sleep(1)


    while True:
        # Clik the select multiple dates and "show 50" button just in ase
        driver.find_element_by_xpath("//*[@id=\"wizardStepContainer\"]/form/div/div[2]/div/div/div/table[1]/thead/tr[2]/th[3]/span/a/span").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[@id=\"wizardStepContainer\"]/form/div/div[2]/div/div/div/table[2]/tfoot/tr/td/div/div[3]/ng-include/items-per-page/ul/li[4]").click
        time.sleep(0.5)
        # Run through all the dates/times, if it is before the requested start time, select the delete button
        signup_slots = driver.find_elements_by_xpath("//*[@id=\"wizardStepContainer\"]/form/div/div[2]/div/div/div/table[1]/tbody/tr")

        i = 0
        didnt_find_any_days = True
        for slot in signup_slots:
            i += 1
            slot_text = slot.text.split()
            slot_datestr = slot_text[0].split("/")
            slot_date = datetime.date(int(slot_datestr[2]),int(slot_datestr[0]),int(slot_datestr[1]))
            if slot_date < cutoff_date:
                chk = slot.find_element_by_xpath("//*[@id=\"wizardStepContainer\"]/form/div/div[2]/div/div/div/table[1]/tbody/tr[" + str(i) + "]/td[3]/span/label")
                driver.execute_script("arguments[0].scrollIntoView();", chk)
                chk.click()
                didnt_find_any_days = False

        if didnt_find_any_days:
            driver.close()
            break

        delete_button = driver.find_element_by_xpath("//*[@id=\"wizardStepContainer\"]/form/div/div[2]/div/div/div/table[1]/thead/tr[1]/th[1]/div/div/div[2]/span/button[3]")
        driver.execute_script("arguments[0].scrollIntoView();", delete_button)
        delete_button.click()
        time.sleep(0.5)
        #input("Please check to see if proper dates were selected. Press enter to delete.")

        yesdel = driver.find_element_by_xpath("//*[@id=\"wizardStepContainer\"]/form/div/div[2]/div[1]/div/div/div[3]/div[4]/div/div/button")
        driver.execute_script("arguments[0].scrollIntoView();", yesdel)
        time.sleep(0.2)
        yesdel.click()
        time.sleep(2)


user_email = ""
user_pword = ""
signupname = "Mako"
cutoff_date = datetime.date(2021,1,15) # Y, M, D

SUGbackDelete(user_email,user_pword,signupname,cutoff_date)