import db
import scraper

def main():
  driver=scraper.load_webdriver()
  connection = db.connect_to_db()
  box_score_urls=scraper.scrape_box_score_urls(driver)
  for x in box_score_urls:
    game_data = scraper.scrape_game_details(driver, x)
    player_scores = scraper.scrape_player_scores(driver, x) 
    home_team_id = db.get_team_id(connection, game_data["home_team"])
    away_team_id = db.get_team_id(connection, game_data["away_team"])
    game_id = db.insert_game(connection, db.format_game_for_db(game_data, home_team_id, away_team_id))
    player_scores_formatted=[]
    for score in player_scores:
      player_id = db.get_player_id(connection, score["player_url"])
      player_scores_formatted.append(db.format_score_for_db(score, player_id, game_id))
    db.insert_scores(connection, player_scores_formatted)


def test():
  driver=scraper.load_webdriver()
  url = "https://men.nznbl.basketball/stats/results/?WHurl=%2Fcompetition%2F31602%2Fmatch%2F2026809%2Fboxscore%3F"
  print(scraper.scrape_game_details(driver, url))
  # box_score_urls = scraper.scrape_box_score_urls(driver)
  # for x in box_score_urls:
  #   print(scraper.scrape_game_details(driver, x))
    


if __name__ == "__main__":
  main()