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
  with connection.cursor() as cursor:
    cursor.execute(query)
    return [{
      "score_id": x[0],
      "player_id": x[1],
      "game_id": x[2],
      "pts": x[3],
      "ast": x[4],
      "stl": x[5],
      "reb": x[6],
      "blk": x[7],
      "3pm": x[8],
      "fga": x[9],
      "fgm": x[10],
      "fta": x[11],
      "ftm": x[12],
      "tov": x[13]
    } for x in cursor]




    