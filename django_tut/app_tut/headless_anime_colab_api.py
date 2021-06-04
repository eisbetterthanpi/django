
def setup_anime_colab():
    from selenium import webdriver
    from selenium_stealth import stealth
    import time
    # https://stackoverflow.com/questions/66209119/automation-google-login-with-python-and-selenium-shows-this-browser-or-app-may
    options = webdriver.ChromeOptions()

    # og fthem(linux server)
    WINDOW_SIZE = "1920,1080"
    options.add_argument("--headless")
    options.add_argument("--window-size=%s" % WINDOW_SIZE)
    options.add_argument('--no-sandbox')

    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    # https://stackoverflow.com/questions/51046454/how-can-we-use-selenium-webdriver-in-colab-research-google-com
    # options.add_argument("--disable-web-security")
    # # options.add_argument("--user-data-dir=true")
    # options.add_argument("--allow-running-insecure-content")
    options.add_argument('--user-data-dir=F:/selflearn/user-data-django')

    # chrome_options.add_argument("user-data-dir=C:/Users/matth/AppData/Local/Google/Chrome/User Data/") #for same as local own
    CHROMEDRIVER_PATH = 'C:/Users/matth/AppData/Local/Programs/Python/Python37/Lib/site-packages/selenium/webdriver/chromedriver.exe'

    driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)
    # driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options, chrome_options=options)

    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

    driver.get('https://colab.research.google.com/drive/1GPgQZGxFgQp9vJbaLJTp9rB-PEhECbXO')

    # time.sleep(3)
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains

    # print(driver.title)
    # driver.find_element_by_xpath("command='runall'").click() #this is from 1
    WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, "(//colab-run-button)[1]")))
    driver.find_element_by_xpath("(//colab-run-button)[1]").click() #[this] is from 1

    # <colab-dialog class="yes-no-dialog" # <paper-dialog role="dialog" # #shadow-root (open) # usage limits usage-limit
    try:
        driver.find_element_by_xpath("//div[@class='usage limits usage-limit']")
        print("usage limit? :)")
    except: # NoSuchElementException
        # import sys
        # print("nope",sys.exc_info())
        pass

    return driver


# while True:
def run_anime_colab(driver, high="a"):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    # print(driver.title)
    # document.getElementsByClassName("monaco-editor").item(2).click()
    # https://stackoverflow.com/questions/41040985/unable-to-get-the-text-inside-the-monaco-editor-using-protractor
    node = driver.find_element_by_xpath("(//div[contains(@class,'editor-scrollable')])[2]") #1,2,3
    node.click()
    # this.monaco.editor.getModels()[2].setValue("terra")
    driver.execute_script('this.monaco.editor.getModels()[arguments[0]].setValue(arguments[1])', 3, 'tap="'+high+'"') #1,3,5 #set input tap
    driver.find_element_by_xpath("(//colab-run-button)[2]").click() #run update tap value
    # time.sleep(3)

    driver.find_element_by_xpath("(//colab-run-button)[3]").click()
    WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, "//div[@class='outputview']/iframe")))
    iframe=driver.find_element_by_xpath("//div[@class='outputview']/iframe")
    driver.switch_to.frame(iframe)
    # WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, "//div[@class='output_subarea output_image']/img")))
    # img = driver.find_element_by_xpath("//div[@class='output_subarea output_image']/img").get_attribute("src")
    WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, "(//div[@class='output_subarea output_image'])[1]/img")))
    img1 = driver.find_element_by_xpath("(//div[@class='output_subarea output_image'])[1]/img").get_attribute("src")
    WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, "(//div[@class='output_subarea output_image'])[2]/img")))
    img2 = driver.find_element_by_xpath("(//div[@class='output_subarea output_image'])[2]/img").get_attribute("src")
    # print(img1[:100])
    # print(img2[:100])

    driver.switch_to.default_content()
    return img1,img2


# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# driver.quit()
