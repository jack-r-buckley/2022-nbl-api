import db

def main():
  connection = db.connect_to_db()
  db.select_players(connection)
  db.select_teams(connection)

if __name__ == "__main__":
  main()
