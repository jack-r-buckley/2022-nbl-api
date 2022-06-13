import db

def display_db_data():
  connection = db.connect_to_db()
  db.select_teams(connection)
  db.select_players(connection)
  db.select_games(connection)
  db.select_scores(connection)


if __name__ == "__main__":
  display_db_data()