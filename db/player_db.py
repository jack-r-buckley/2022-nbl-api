import pymysql

def insert_players(connection, players: list):
  query="""
  INSERT INTO Player (name, team_id) VALUES (%s, %s)
  """
  with connection.cursor() as cursor:
    for x in players:
      try:
        cursor.execute(query, x)
      except pymysql.err.IntegrityError as ie:
        print(f"{x} already exists in Player table. Skipping")
    connection.commit()
    
  
def select_players(connection):
  query="""
    SELECT * FROM Player
  """
  print("selection players")
  with connection.cursor() as cursor:
    cursor.execute(query)
    for x in cursor:
      print(x)
