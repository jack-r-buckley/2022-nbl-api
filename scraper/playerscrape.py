from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_team_players(driver, url):
  driver.get(url.replace("%3F", "%2Froster"))
  WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME, "roster-table"))
    )
  players_table=driver.find_element(by=By.CLASS_NAME, value="roster-table")
  players=players_table.find_elements(by=By.CLASS_NAME, value="text-cell")
  filtered_players=[]
  for x in players:
    urls = x.find_elements(by=By.TAG_NAME, value="a")
    if len(urls) == 2:
      filtered_players.append(urls[1])
    else:
      filtered_players.append(urls[0])
  return [{
    "name": x.get_attribute("innerText").strip(),
    "url": x.get_attribute("href").strip()
  } for x in filtered_players]
  