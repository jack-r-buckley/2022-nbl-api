import scraper
import db

def main():
  driver = scraper.load_webdriver()
  connection = db.connect_to_db()
  teams = scraper.scrape_team_names(driver)
  db.insert_teams(connection, [(x["team_name"], x["team_url"]) for x in teams])
  for x in teams:
    players=scraper.scrape_team_players(driver, x["team_url"])
    team_id=db.get_team_id(connection, x["team_name"])
    db.insert_players(connection, [(x["name"], x["url"], team_id) for x in players])

def test():
  driver = scraper.load_webdriver()
  url = "https://men.nznbl.basketball/stats/results/?WHurl=%2Fteam%2F146683%3F"
  scraper.scrape_team_players(url)  
if __name__ == "__main__":
  main()