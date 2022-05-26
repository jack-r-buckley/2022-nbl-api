from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_player_scores(driver, url):
  driver.get(url)

  WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME, "table-wrap"))
  )
  scores=[]
  player_tables = driver.find_elements(by=By.TAG_NAME, value="tbody")
  for table in player_tables:
    player_rows = table.find_elements(by=By.TAG_NAME, value="tr")
    for row in player_rows:
      row_data = row.find_elements(by=By.TAG_NAME, value="td")
      scores.append({
        "player_url": row_data[1].find_element(by=By.TAG_NAME, value="a").get_attribute("href").strip(),
        "pts": int(row_data[3].get_attribute("data-sort-value")),
        "fgm": int(row_data[7].get_attribute("data-sort-value")),
        "fga": int(row_data[8].get_attribute("data-sort-value")),
        "3pm": int(row_data[10].get_attribute("data-sort-value")),
        "fta": int(row_data[13].get_attribute("data-sort-value")),
        "ftm": int(row_data[14].get_attribute("data-sort-value")),
        "ast": int(row_data[16].get_attribute("data-sort-value")),
        "reb": int(row_data[19].get_attribute("data-sort-value")),
        "stl": int(row_data[20].get_attribute("data-sort-value")),
        "blk": int(row_data[21].get_attribute("data-sort-value")),
        "tov": int(row_data[22].get_attribute("data-sort-value")),
      })
  return scores