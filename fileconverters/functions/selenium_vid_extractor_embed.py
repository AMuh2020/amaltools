from selenium import webdriver, common
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def get_vid_src(url):
    options = Options()
    options.add_argument('--headless=new')
    # options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.163 Mobile Safari/537.36')
    
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    # while driver.current_url != url:
    #     driver.execute_script('return window.document.referrer')

    delay = 30
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, "video")))
    vid_src = myElem.get_attribute("src")
    if vid_src == "" or vid_src == None:
        print("here")
        vid_src = myElem.get_attribute("innerHTML")
        vid_src = myElem.find_element(By.TAG_NAME, "source").get_attribute("src")
    print(vid_src)
    driver.quit()
    return vid_src

# production version
# def get_vid_src(url):
#     try:
#         service = Service(executable_path=r'/usr/bin/chromedriver')

#         options = webdriver.ChromeOptions()
#         options.add_argument('--headless=new')
#         options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.163 Mobile Safari/537.36')

#         driver = webdriver.Chrome(service=service, options=options)

#         driver.get(url)
#         if driver.current_url != url:
#             driver.execute_script('return window.document.referrer')

#         delay = 30
#         myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, "video")))
#         vid_src = myElem.get_attribute("src")
#         if vid_src == "" or vid_src == None:
#             # print("here")
#             vid_src = myElem.get_attribute("innerHTML")
#             vid_src = myElem.find_element(By.TAG_NAME, "source").get_attribute("src")
#         # print(vid_src)
#         driver.quit()
#         return vid_src
#     except common.exceptions.TimeoutException or common.exceptions.NoSuchElementException:
#         print("This page didnt have a video on it")
#         return "This page didnt have a video on it"
#     except Exception as e:
#         print("error:{}".format(e))
#         return "error"

