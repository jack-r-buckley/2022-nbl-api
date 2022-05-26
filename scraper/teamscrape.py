from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

def scrape_team_names(driver):
  base_url="https://men.nznbl.basketball/stats/results/?WHurl=%2Fstandings%3F"

  driver.get(base_url)

  WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME, "standings"))
    )

  teams = driver.find_elements(by=By.CLASS_NAME, value="team-name-full")
  return [
    {
      "team_name": x.get_attribute("innerText").strip(), 
      "team_url": x.find_element_by_xpath("..").get_attribute("href")
    } 
    for x in teams]


if __name__ == "__main__":
  main()
