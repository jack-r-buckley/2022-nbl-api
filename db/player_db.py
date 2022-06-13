import pymysql

def insert_players(connection, players: list):
  query="""
  INSERT INTO Player (name, url, team_id) VALUES (%s, %s, %s)
  """
  with connection.cursor() as cursor:
    for x in players:
      try:
        cursor.execute(query, x)
      except pymysql.err.IntegrityError as ie:
        print(f"{x} already exists in Player table. Skipping")
    connection.commit()
    
def get_player_id(connection, player_url):
  with connection.cursor() as cursor:
    query=f"""
      SELECT player_id FROM Player WHERE (url='{player_url}')
    """
    cursor.execute(query)
    for x in cursor:
      result = x[0]
      return result
  
def select_players(connection):
  query="""
    SELECT * FROM Player
  """
  with connection.cursor() as cursor:
    cursor.execute(query)
    return [{
      "player_id": x[0],
      "name": x[1],
      "url": x[2],
      "team_id": x[3]
    } for x in cursor]