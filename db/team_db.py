import pymysql

def insert_teams(connection, teams: list):
  query="""
    INSERT INTO Team (name, url) VALUES (%s, %s)
  """
  with connection.cursor() as cursor:
    for x in teams:
      try:
        cursor.execute(query, x)
      except pymysql.err.IntegrityError as ie:
        print(f"{x} already exists in Team table. Skipping.")
    connection.commit()

def get_team_id(connection, team_name):
  query=f"""
    SELECT team_id FROM Team WHERE name='{team_name}'
  """
  with connection.cursor() as cursor:
    cursor.execute(query)
    for x in cursor:
        result = x[0]
    return result

def select_teams(connection):
  query="""
    SELECT * FROM Team
  """
  print("selection teams")

  with connection.cursor() as cursor:
    cursor.execute(query)
    for x in cursor:
      print(x)
