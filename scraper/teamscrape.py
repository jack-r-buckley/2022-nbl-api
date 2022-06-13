from re import T
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

def scrape_team_names(driver):
  base_url="https://men.nznbl.basketball/stats/results/?WHurl=%2Fstandings%3F"
  team_name_id_string="team-name-full" 
  team_table_id_string="standings"

  driver.get(base_url)

  WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME, team_table_id_string))
    )

  teams = driver.find_elements(by=By.CLASS_NAME, value=team_name_id_string)
  return [
    {
      "team_name": x.get_attribute("innerText").strip(), 
      "team_url": x.find_element_by_xpath("..").get_attribute("href")
    } 
    for x in teams]

