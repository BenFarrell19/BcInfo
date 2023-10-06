from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)



driver.get('https://avalanche.org/#/current')
sleep(2)
elem = driver.find_element_by_xpath('//*[@id="ndm-map"]/div[1]/div/div/div[2]/div[2]/div/div[4]/div/div/div/div[1]/div/div/div/div[1]/div[1]')
print(elem.text)

'''
driver.find_element(By.CSS_SELECTOR, "#ndm-zoom-out > i").click()
sleep(1)
driver.get_screenshot_as_file("screenshot.png")
driver.quit()
print('screenshot saved')

# collecting color values
from PIL import Image

input_image = Image.open("screenshot.png")
pixel_map = input_image.load()
width, height = input_image.size
'''
