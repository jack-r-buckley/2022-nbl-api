from dotenv import load_dotenv
import os
import pymysql

def connect_to_db():
  load_dotenv()
  db_config={
      "host": os.getenv("HOST"),
      "user": "admin",
      "database": os.getenv("DATABASE"),
      "password": os.getenv("PASSWORD")
    }
  return pymysql.connect(**db_config)


def create_db(connection, database): 

    with connection.cursor() as cursor:
      cursor.execute(
    """
    CREATE DATABASE IF NOT EXISTS {};
    """.format(database))
    connection.commit()

def create_tables(connection):
    queries = [
    "SET FOREIGN_KEY_CHECKS=0",
    """
    DROP TABLE IF EXISTS Team;  
    """,
    """
    CREATE TABLE IF NOT EXISTS Team (
      team_id INT AUTO_INCREMENT NOT NULL,
      name VARCHAR(255) UNIQUE,
      url VARCHAR(255),
      PRIMARY KEY (team_id)
    ) ENGINE=INNODB;
    """,
    """
    DROP TABLE IF EXISTS Game;  
    """,
    """
    CREATE TABLE IF NOT EXISTS Game (
      game_id INT AUTO_INCREMENT NOT NULL,
      date DATETIME,
      URL VARCHAR(255),
      home_team_id INT NOT NULL,
      away_team_id INT NOT NULL,
      home_score INT,
      away_score INT,
      PRIMARY KEY (game_id),
      FOREIGN KEY(home_team_id) REFERENCES Team(team_id) ON DELETE CASCADE,
      FOREIGN KEY(away_team_id) REFERENCES Team(team_id) ON DELETE CASCADE
    ) ENGINE=INNODB;
    """,
    """
    DROP TABLE IF EXISTS Player;
    """,
    """
    CREATE TABLE IF NOT EXISTS Player (
      player_id INT AUTO_INCREMENT NOT NULL,
      name VARCHAR(255) UNIQUE,
      team_id INT,
      PRIMARY KEY (player_id),
      FOREIGN KEY (team_id) REFERENCES Team(team_id) ON DELETE CASCADE
    ) ENGINE=INNODB;
    """,
    """
    DROP TABLE IF EXISTS Score;
    """,
    """
    CREATE TABLE IF NOT EXISTS Score (
      score_id INT AUTO_INCREMENT NOT NULL,
      player_id INT,
      game_id INT,
      pts INT,
      stl INT,
      reb INT,
      blk INT,
      3pm INT,
      fga INT,
      fgm INT,
      fta INT,
      ftm INT,
      PRIMARY KEY (score_id),
      FOREIGN KEY(player_id) REFERENCES Player(player_id) ON DELETE CASCADE,
      FOREIGN KEY(game_id) REFERENCES Game(game_id) ON DELETE CASCADE
    ) ENGINE=INNODB;
    """,
    "SET FOREIGN_KEY_CHECKS=0"
    ]

    with connection.cursor() as cursor:
      for x in queries:
        cursor.execute(x)


def describe_table(connection, table):
    with connection.cursor() as cursor:
      cursor.execute( """
        DESCRIBE {};
      """.format(table))
      for x in cursor:
        print(x)



def main():
  cx = connect_to_db()
  create_tables(cx)
  describe_table(cx, "Game"),
  describe_table(cx, "Player"),
  describe_table(cx, "Team"),
  describe_table(cx, "Score")
  


if __name__ == '__main__':
  main()


