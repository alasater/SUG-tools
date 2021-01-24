from selenium import webdriver
import datetime
import time

class sugController:
    def __init__(self,username,password,signupname,cutoff_date_early,cutoff_date_late):
        self.username = username
        self.password = passord
        self.driver = webdriver.Chrome()
        self.signup = signupname
        self.date_early = cutoff_date_early
        self.date_late = cutoff_date_late

    def getDriver(self):
        return self.driver

    def login(self):
        self.driver.get("https://signupgenius.com/register")
        uspace = self.driver.find_element_by_id("email")
        uspace.clear()
        uspace.send_keys(self.username)

        pspace = self.driver.find_element_by_id("pword")
        pspace.clear()
        pspace.send_keys(self.username)

        self.driver.find_element_by_name("submit").click()

    def homepage2Edit(self):
        # Click the edit button corresponding to the requested signup

        # Click the "Sign Ups tab" just in case
        self.driver.find_element_by_xpath("//*[@id=\"signups\"]/div[1]/svg").click()
        time.sleep(0.5)

        # Click the "Created" tab just in case
        self.driver.find_element_by_xpath("//*[@id=\"memPgCenter\"]/div/div[2]/div/ul/li[1]/a").click()
        time.sleep(0.5)

        # Find the correct signup object to click
        signups = self.driver.find_elements_by_xpath("//*[@id=\"signUpLists\"]/div[1]/div/div/table/tbody/tr")
        i = 1
        for su in signups:
            if self.signup in su.text:
                break
            else:
                i += 1

        # Click the edit button
        edit_button = self.driver.find_element_by_xpath("//*[@id=\"signUpLists\"]/div[1]/div/div/table/tbody/tr[" + str(i) + "]/td[4]/div/div[1]/a")
        self.driver.execute_script("arguments[0].scrollIntoView();", edit_button)
        edit_button.click()

    def edit2Slots(self):
        # At this point we can make the window fullscreen
        tab_buttons = self.driver.find_element_by_class_name("btn-tabs")
        tab_buttons = tab_buttons.find_elements_by_css_selector("*")
        tab_buttons[1].click()
        time.sleep(0.5)
        self.driver.fullscreen_window()

    def backDelete(self):
        #Assume are on the editing page of the correct signup. Delete dates before the cutoff date

        while True:
            # Click the select multiple dates and "show 50" button just in case
            self.driver.find_element_by_xpath( "//*[@id=\"wizardStepContainer\"]/form/div/div[2]/div/div/div/table[1]/thead/tr[2]/th[3]/span/a/span").click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("//*[@id=\"wizardStepContainer\"]/form/div/div[2]/div/div/div/table[2]/tfoot/tr/td/div/div[3]/ng-include/items-per-page/ul/li[4]").click
            time.sleep(0.5)

            # Run through all the dates/times, if it is before the requested start time, select the delete button
            signup_slots = self.driver.find_elements_by_xpath("//*[@id=\"wizardStepContainer\"]/form/div/div[2]/div/div/div/table[1]/tbody/tr")
            i = 0
            didnt_find_any_days = True
            for slot in signup_slots:
                i += 1
                slot_text = slot.text.split()
                slot_datestr = slot_text[0].split("/")
                slot_date = datetime.date(int(slot_datestr[2]), int(slot_datestr[0]), int(slot_datestr[1]))
                if slot_date < self.date_early:
                    chk = slot.find_element_by_xpath("//*[@id=\"wizardStepContainer\"]/form/div/div[2]/div/div/div/table[1]/tbody/tr[" + str(i) + "]/td[3]/span/label")
                    self.driver.execute_script("arguments[0].scrollIntoView();", chk)
                    chk.click()
                    didnt_find_any_days = False

            if didnt_find_any_days:
                break

            # Now that we've selected all the dates we want, press the delete button
            delete_button = self.driver.find_element_by_xpath("//*[@id=\"wizardStepContainer\"]/form/div/div[2]/div/div/div/table[1]/thead/tr[1]/th[1]/div/div/div[2]/span/button[3]")
            self.driver.execute_script("arguments[0].scrollIntoView();", delete_button)
            delete_button.click()
            time.sleep(0.5)

            # Now press the delete button on the popup page
            yesdel = self.driver.find_element_by_xpath("//*[@id=\"wizardStepContainer\"]/form/div/div[2]/div[1]/div/div/div[3]/div[4]/div/div/button")
            self.driver.execute_script("arguments[0].scrollIntoView();", yesdel)
            time.sleep(0.5)
            yesdel.click()
            time.sleep(2)

    def forwardAdd(self):
        #Assume we are on the signup edit page, add signups up to the cutoff_date_late

        # Click "Add Dates"
        self.driver.find_element_by_xpath("//*[@id=\"wizardStepContainer\"]/form/div/div[2]/div/div/div/table[1]/thead/tr[1]/th[1]/div/div/div[3]/span/button").click()
        time.sleep(0.5)

        # Click "Add Time Slots"
        self.driver.find_element_by_xpath("//*[@id=\"wizardStepContainer\"]/form/div/div[2]/div[1]/div/div/div[2]/div/div/div/span[3]/button").click()
        time.sleep(0.5)

        # Enter the start date

        # Enter the late date

        # Enter the time range
        self.driver.find_element_by_xpath("//*[@id=\"ts_starttime\"]/div/div[1]/input").send_keys("6")
        self.driver.find_element_by_xpath("//*[@id=\"ts_endtime\"]/div/div[1]/input").send_keys("6")

        # Select "PM" from the dropdown menu
        self.driver.find_element_by_xpath("//*[@id=\"ts_endtime\"]/div/div[3]/div/button").click()
        self.driver.find_element_by_xpath("//*[@id=\"ts_endtime\"]/div/div[3]/div/ul/li/a").click()

        # Set the Time slot increment
        self.driver.find_element_by_xpath("//*[@id=\"ts_incrementtime\"]").send_keys("2")
        self.driver.find_element_by_xpath("//*[@id=\"ts_incrementunit\"]").click()

        # Click "Add Time Slot"
        self.driver.find_element_by_xpath("//*[@id=\"rd_ts_save\"]").click()

    def extent(self):
        # Figure out the start/end dates that are currently in the signup


        return(first_date,last_date)