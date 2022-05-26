from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime



def scrape_games(driver):
  base_url="https://men.nznbl.basketball/stats/results/"
  
  driver.get(base_url)

  # wait for the schedule element to load

  WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME, "schedule-wrap"))
    )

  # generates a list of urls to box scores of completed games 
  box_scores=get_box_scores(driver)

  # returns a list of games 
  for x in box_scores:
    driver.get(x)
    WebDriverWait(driver, 15).until(
      EC.presence_of_element_located((By.CLASS_NAME, "boxscore"))
      )
    print(get_game_details(x, driver))
    # get_player_games(driver)

def get_box_scores(driver):
  results=[]
  box_scores=driver.find_elements(by=By.CLASS_NAME, value='STATUS_COMPLETE')
  for x in box_scores:
    url = x.find_element(by=By.CLASS_NAME, value='detail-r-link')
    results.append(url.get_attribute('href'))
  return results

def get_game_details(url, driver):
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

def get_player_games(url):
  print("hello")

def main():
  driver = load_webdriver()
  scrape_games(driver)

if __name__ == '__main__':
  main()