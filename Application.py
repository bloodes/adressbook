from selenium import webdriver

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(0)

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()

    def create_new_group(self, group):  # Принимает объекти типа Group
        driver = self.driver
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_css_selector('input[name="new"]').click()
        driver.find_element_by_name("group_name").send_keys(group.group_name)
        driver.find_element_by_name("group_header").send_keys(group.group_header)
        driver.find_element_by_name("group_footer").send_keys(group.group_footer)
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("group page").click()

    def create_new_contact(self, contact):         # Принимает объекти типа Contact
        driver = self.driver
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").send_keys(contact.middlename)
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_css_selector("input[name='submit']").click()
        driver.find_element_by_link_text("home page").click()

    def login(self, name, password):      # Принимает логин и пароль.
        driver = self.driver
        self.open_home_page()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("user").send_keys(name)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_css_selector("input[type='submit']").click()

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()