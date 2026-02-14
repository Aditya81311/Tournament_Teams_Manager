import sqlite3

conn = sqlite3.connect("database.db")

cur = conn.cursor()

class Data_base():
    def user_table(self):
        cur.execute('''
        CREATE TABLE IF NOT EXISTS  users(
              user_id INTEGER  PRIMARY KEY AUTOINCREMENT,
              user_name VARCHAR NOT NULL ,
              user_email VARCHAR UNIQUE NOT NULL,
              user_phone VARCHAR (12) UNIQUE,
              user_role VARCHAR NOT NULL
              )
        ''')
        print("Table Crated ")
    def team_table(self):
        cur.execute(''' 
          CREATE TABLE IF NOT EXISTS  teams(
               team_id INTEGER  PRIMARY KEY AUTOINCREMENT,
               team_name VARCHAR (100) UNIQUE NOT NULL,
               number_members INTEGER  NOT NULL ,
               game VARCHAR  NOT NULL,
               team_captain VARCHAR NOT NULL
           ) 
            ''')
        print("Table Crated ")
    def team_member(sef):
        cur.execute('''
        CREATE TABLE IF NOT EXISTS team_members(
        team_id INTEGER  PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER  NOT NULL,
        join_date DATE NOT NULL,
        is_captain  BOOL NOT NULL,
        FOREIGN KEY (team_id) REFERENCES teams(team_id),
        FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
        ''')


    def games_table(self):
        cur.execute('''
        CREATE TABLE IF NOT EXISTS  games(
               game_id INTEGER  PRIMARY KEY AUTOINCREMENT,
               game_name VARCHAR  NOT NULL,
               game_gener VARCHAR NOT NULL
        )
        ''')
        print("Table Crated ")
    def tournament_table(self):
        cur.execute('''
        CREATE TABLE IF NOT EXISTS tournaments (
            tournament_id INTEGER  PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            game_id INTEGER  NOT NULL,
            FOREIGN KEY (game_id) REFERENCES games(game_id)
        )
        ''')
    def matches_table(self):
        cur.execute('''
        CREATE TABLE IF NOT EXISTS matches (
            match_id INTEGER  PRIMARY KEY AUTOINCREMENT,
            tournament_id INTEGER  NOT NULL,
            match_no INTEGER  NOT NULL,
            round_no INTEGER  NOT NULL,
            scheduled_at DATE NOT NULL,
            status VARCHAR(20) NOT NULL,
            FOREIGN KEY (tournament_id) REFERENCES tournaments(tournament_id)
        )
        ''')
        print("Table Crated ")

    def leader_board_table(self):
        cur.execute('''
        CREATE TABLE leader_board(
        tournament_id INTEGER  ,
        team_id INTEGER   NOT NULL,
        match_id INTEGER   NOT NULL,
        played INTEGER  NOT NULL,
        wins INTEGER  NOT NULL,
        score_for VARCHAR NOT NULL,
        score_aginst VARCHAR NOT NULL,
        updated DATE NOT NULL,

        FOREIGN KEY (tournament_id) REFERENCES tournaments(tournament_id),
        FOREIGN KEY (team_id) REFERENCES teams(team_id),
        FOREIGN KEY (match_id) REFERENCES matches(match_id)
        )
        ''')
if __name__ == "__main__":
    create_tables = Data_base()
    create_tables.user_table()
    create_tables.team_table()
    create_tables.team_member()
    create_tables.games_table()
    create_tables.tournament_table()
    create_tables.matches_table()
    create_tables.leader_board_table()