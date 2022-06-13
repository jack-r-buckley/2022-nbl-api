import pymysql

def insert_scores(connection, scores: list):
  query="""
  INSERT INTO Score (player_id, game_id, pts, ast, stl, reb, blk, 3pm, fga, fgm, fta, ftm, tov) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
  """
  with connection.cursor() as cursor:
    for x in scores:
      cursor.execute(query, x)

    connection.commit()

def format_score_for_db(score, player_id, game_id):
  return (player_id, game_id, score["pts"], score["ast"], score["stl"], score["reb"], score["blk"], score["3pm"], score["fga"], score["fgm"], score["fta"], score["ftm"], score["tov"])

def delete_duplicate_scores(connection, scores: list):
  query=f"""
  SELECT player_id, game_id FROM Score
  """
  existing_scores=[]
  with connection.cursor() as cursor:
    cursor.execute(query)
    for x in cursor:
      existing_scores.append((x[0], x[1]))
  filtered_scores=list(filter(lambda x: ((x[0], x[1]) not in existing_scores), scores))
  return filtered_scores
      

def select_scores(connection):
  query="""
    SELECT * FROM Score
  """
  print("selecting scores")
  with connection.cursor() as cursor:
    cursor.execute(query)
    for x in cursor:
      print(x)



    