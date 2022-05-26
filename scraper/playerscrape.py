from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_team_players(driver, url):
  driver.get(url)
  WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME, "team-players-table"))
    )
  players_table=driver.find_element(by=By.CLASS_NAME, value="team-players-table")
  players=players_table.find_elements(by=By.TAG_NAME, value="a")
  return [x.get_attribute("innerText").strip() for x in players]
  


  