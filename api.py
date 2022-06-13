from fastapi import FastAPI
import db

app = FastAPI()

@app.get("/games")
def get_games():
    connection = db.connect_to_db()
    games = db.select_games(connection)
    return games

@app.get("/players")
def get_players():
    connection = db.connect_to_db()
    players = db.select_players(connection)
    return players

@app.get("/scores")
def get_scores():
    connection = db.connect_to_db()
    scores = db.select_scores(connection)
    return scores

@app.get("/teams")
def get_teams():
    connection = db.connect_to_db()
    teams = db.select_teams(connection)
    return teams