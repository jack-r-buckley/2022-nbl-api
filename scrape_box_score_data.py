from unittest import TestSuite
import db
import scraper

def main():
  driver=scraper.load_webdriver()
  print("Webdriver loaded")

  connection = db.connect_to_db()
  print("Database connection established")
  print("Generating box score URLs")

  box_score_urls=scraper.scrape_box_score_urls(driver)
  print(f"{len(box_score_urls)} URLs found")

  filtered_box_score_urls = db.delete_duplicate_game_urls(connection, box_score_urls)
  print(f"{len(filtered_box_score_urls)} URLs are not in DB.")

  if len(filtered_box_score_urls) == 0:
    print("exiting")
    return

  for x in filtered_box_score_urls:
    game_data = scraper.scrape_game_details(driver, x)
    print(f"getting data for game between {game_data['home_team']} and {game_data['away_team']}")
    home_team_id = db.get_team_id(connection, game_data["home_team"])
    away_team_id = db.get_team_id(connection, game_data["away_team"])
    player_scores = scraper.scrape_player_scores(driver, x) 
    game_id = db.insert_game(connection, db.format_game_for_db(game_data, home_team_id, away_team_id))
    
    if (game_id != None):
      player_scores_formatted=[]
      for score in player_scores:
        player_id = db.get_player_id(connection, score["player_url"])
        player_scores_formatted.append(db.format_score_for_db(score, player_id, game_id))
      db.insert_scores(connection, db.delete_duplicate_scores(connection, player_scores_formatted))


def test():
  driver=scraper.load_webdriver()
  connection = db.connect_to_db()
  url = "https://men.nznbl.basketball/stats/results/?&WHurl=%2Fcompetition%2F31602%2Fmatch%2F2026811%2Fboxscore%3F"
  game_id = db.get_game_id(connection, url)
  player_scores = scraper.scrape_player_scores(driver, url)
  player_scores_formatted=[]
  for score in player_scores:
      player_id = db.get_player_id(connection, score["player_url"])
      player_scores_formatted.append(db.format_score_for_db(score, player_id, game_id))
  print(player_scores_formatted)
  print(db.delete_duplicate_scores(connection, player_scores_formatted))


    


if __name__ == "__main__":
  main()