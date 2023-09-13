from selenium import webdriver

# Create a new instance of the Edge driver
# (I have used MSEdge and typed its driver path )
driver = webdriver.Edge("C:/Users/hitma/Downloads/msedgedriver.exe")

# Navigate to the login page of Quora
driver.maximize_window()
driver.get("https://www.quora.com/")

# Find the username and password fields and enter the credentials
driver.find_element_by_xpath("//input[@id='email']").send_keys("russianboy897@gmail.com")
driver.find_element_by_xpath("//input[@id='password']").send_keys("Ab12c3d4")

# Find the login button and click it
driver.find_element_by_xpath("//button[@type='button']").click()

# Close the browser window
# driver.quit()
