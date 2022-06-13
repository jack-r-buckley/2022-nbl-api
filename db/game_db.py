import pymysql

def insert_game(connection, game):
  query="""
    INSERT INTO Game (date, URL, home_team_id, home_score, away_team_id, away_score)
    VALUES (%s, %s, %s, %s, %s, %s);
  """
  with connection.cursor() as cursor:
    # try:
      cursor.execute(query, game)
      cursor.execute("SELECT LAST_INSERT_ID();")
      connection.commit()
      for x in cursor:
        return x[0]
    # except pymysql.err.IntegrityError as ie:
    #   print ("Game already exists in db. Skipping")

def format_game_for_db(game, home_team_id, away_team_id):
  return (game["date"], game["url"], home_team_id, game["home_score"], away_team_id, game["away_score"]) 

def select_games(connection):
  query="""
    SELECT * FROM Game
  """
  print("selecting games")
  with connection.cursor() as cursor:
    cursor.execute(query)
    for x in cursor:
      print(x)

def get_game_id(connection, url):
  query=f"""
    SELECT game_id FROM Game WHERE (url = '{url}')
  """
  with connection.cursor() as cursor:
    cursor.execute(query)
    for x in cursor:
      return x[0]

def delete_duplicate_game_urls(connection, url_list):
  query = """
    SELECT URL from Game;
  """
  with connection.cursor() as cursor:
    cursor.execute(query)
    urls = [x[0] for x in cursor]
    return list(filter(lambda x: x not in urls, url_list))
