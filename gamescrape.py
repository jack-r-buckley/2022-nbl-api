from selenium import webdriver 
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os


def main():
  base_url="https://men.nznbl.basketball/stats/results/"
  chrome_options = Options()

  # use only one of these lines. use in headless unless debugging, it is much faster.\

  # chrome_options.add_argument("--window-size=1920x1080")
  chrome_options.add_argument("--headless")

  # initiate chrome driver, get webpage, wait for the schedule element to load
  driver = webdriver.Chrome(options=chrome_options, executable_path=os.getcwd()+'/chromedriver.exe')
  driver.get(base_url)
  WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME, "schedule-wrap"))
    )
  # generate list of urls to box scores of completed games 
  box_scores=get_box_scores(driver)

  # go to each box score and return the game details and the player's lines
  for x in box_scores:
    driver.get(x)
    WebDriverWait(driver, 15).until(
      EC.presence_of_element_located((By.CLASS_NAME, "boxscore"))
      )
    print(get_game_details(driver))
    # get_player_games(driver)

def get_box_scores(driver):
  results=[]
  box_scores=driver.find_elements(by=By.CLASS_NAME, value='STATUS_COMPLETE')
  for x in box_scores:
    url = x.find_element(by=By.CLASS_NAME, value='detail-r-link')
    results.append(url.get_attribute('href'))
  return results

def get_game_details(driver):
  home = driver.find_element(by=By.CLASS_NAME, value="home-wrapper")
  away = driver.find_element(by=By.CLASS_NAME, value="away-wrapper")
  date = driver.find_element(by=By.CLASS_NAME, value="match-time").find_element(by=By.TAG_NAME, value="span").get_attribute("innerText").strip()
  game = {
    "home": {
      "team": home.find_element(by=By.TAG_NAME, value="a").get_attribute("title").strip(),
      "score": int(home.find_element(by=By.CLASS_NAME, value="score").get_attribute("innerText").strip())
    },
    "away": {
      "team": away.find_element(by=By.TAG_NAME, value="a").get_attribute("title").strip(),
      "score": int(away.find_element(by=By.CLASS_NAME, value="score").get_attribute("innerText").strip())
    },
    "date": datetime.strptime(date, "%d %b %Y, %I:%M %p")
  }
  return game

def get_player_games(url):
  print("hello")



if __name__ == '__main__':
  main()