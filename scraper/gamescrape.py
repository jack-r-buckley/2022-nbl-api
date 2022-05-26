from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime



def scrape_box_score_urls(driver):
  base_url="https://men.nznbl.basketball/stats/results/"
  driver.get(base_url)

  WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME, "schedule-wrap"))
    )

  results=[]
  box_scores=driver.find_elements(by=By.CLASS_NAME, value='STATUS_COMPLETE')
  return [x.find_element(by=By.CLASS_NAME, value='detail-r-link').get_attribute('href') for x in box_scores]



  
def scrape_game_details(driver, url):
  driver.get(url)
  WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME, "boxscore"))
    )

  home = driver.find_element(by=By.CLASS_NAME, value="home-wrapper")
  away = driver.find_element(by=By.CLASS_NAME, value="away-wrapper")
  date = driver.find_element(by=By.CLASS_NAME, value="match-time").find_element(by=By.TAG_NAME, value="span").get_attribute("innerText").strip()
  game = {
    "url": url,
    "home_team": home.find_element(by=By.TAG_NAME, value="a").get_attribute("title").strip(),
    "home_score": int(home.find_element(by=By.CLASS_NAME, value="score").get_attribute("innerText").strip()),
    "away_team": away.find_element(by=By.TAG_NAME, value="a").get_attribute("title").strip(),
    "away_score": int(away.find_element(by=By.CLASS_NAME, value="score").get_attribute("innerText").strip()),
    "date": datetime.strptime(date, "%d %b %Y, %I:%M %p")
  }
  return game
