from .team_db import get_team_id

def insert_games(connection, games: list):
  query="""
    INSERT INTO Game (date, URL, home_team_id, home_score, away_team_id, away_score)
    VALUES (%s, %s, %s, %s, %s, %s);
  """
  with connection.cursor() as cursor:
    for x in games:
      cursor.execute(query, x)

def format_games_for_db(games: list):
  home_team_id=get_team_id(x["home_team"])
  away_team_id=get_team_id(x["away_team"])

  return [(
    x["date"], x["url"], home_team_id, x["home_score"], away_team_id, x["away_score"]
  ) for x in games]

