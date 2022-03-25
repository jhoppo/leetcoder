def booking():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    # user_info = [[self.names[i], self.sAmAccountNames[i], self.Emails[i]] for i in range(len(self.Emails))]
    web1922 = "https://1922.gov.tw/"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(web1922)
    return driver
    # click login button
    driver.switch_to.frame("TopLevelFrame")
    driver.switch_to.frame("topframe")
    driver.find_element_by_xpath(
        "/html/body/div/table/tbody/tr[@class='clsBackYellow']/td[@class='clsDeviceStatusLink']/a[@class='clsLogin']").click()
    time.sleep(5)
    # key in login
    driver.switch_to.frame("TopLevelFrame")
    driver.switch_to.frame("Loginframe")
    driver.find_element_by_name("USERNAME").send_keys("admin")
    driver.find_element_by_name("PASS").send_keys("123456")
    driver.find_element_by_name("Login").click()
    time.sleep(10)
    driver.switch_to.frame("TopLevelFrame")
    driver.switch_to.frame("topframe")
    driver.find_element_by_id("REGISTRATION-anchor").click()
    time.sleep(3)
    # click AddressBook
    driver.switch_to.default_content()
    driver.switch_to.frame("TopLevelFrame")
    driver.switch_to.frame("SubMenu")
    driver.find_element_by_id("AddressBook").click()
    time.sleep(3)
    for the_user in user_info:
        # click add new contacts
        driver.switch_to.default_content()
        driver.switch_to.frame("TopLevelFrame")
        driver.switch_to.frame("contents")
        driver.switch_to.frame("fraTitle")
        driver.find_element_by_name("btnLdapAdd").click()
        time.sleep(3)
        # key in new contact's data
        driver.switch_to.default_content()
        driver.switch_to.frame("TopLevelFrame")
        driver.switch_to.frame("contents")
        driver.switch_to.frame("fraList")
        driver.find_element_by_id("NAME").send_keys(the_user[0])
        driver.find_element_by_id("FURIGANA").send_keys(the_user[1][0])
        driver.find_element_by_name("EMAIL").send_keys(the_user[2])
        driver.find_element_by_id("SEL_DEST").send_keys("分享")
        # click save new contact
        driver.switch_to.default_content()
        driver.switch_to.frame("TopLevelFrame")
        driver.switch_to.frame("contents")
        driver.switch_to.frame("fraTitle")
        driver.find_element_by_name("btnSave").click()
        time.sleep(3)
    # click share settings
    driver.switch_to.default_content()
    driver.switch_to.frame("TopLevelFrame")
    driver.switch_to.frame("contents")
    driver.switch_to.frame("fraTitle")
    driver.find_element_by_id("SHAREDSETT").click()
    time.sleep(3)
    # click sync
    driver.switch_to.default_content()
    driver.switch_to.frame("TopLevelFrame")
    driver.switch_to.frame("contents")
    driver.switch_to.frame("fraList")
    driver.switch_to.frame("fraTitle")
    driver.find_element_by_id("btnSynAll").click()
    # click I am sure
    driver.switch_to.alert.accept()
    time.sleep(10)
    driver.close()
    return