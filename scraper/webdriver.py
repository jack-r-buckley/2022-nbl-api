from selenium import webdriver 
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

def load_webdriver():
  chrome_options = Options()

  # use only one of these lines. use headless unless you need to the window, it is much faster.

  # chrome_options.add_argument("--window-size=1920x1080")
  chrome_options.add_argument("--headless")
  service = Service(executable_path=os.getcwd()+"/chromedriver.exe")
  driver = webdriver.Chrome(service=service, options=chrome_options)  
  return driver


if __name__ == "__main__":
  load_webdriver()