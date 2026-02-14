import sqlite3

conn = sqlite3.connect("database.db")

cur = conn.cursor()

class Users():
    def __init__(self,user_id,name,email,phone,role):
            self.user_id = user_id
            self.user_name  = name
            self.user_email =  email
            self.user_phone = phone
            self.user_role  = role
    def create_user(self):
        cur.execute('''
          INSERT INTO users(user_name ,
            user_email, 
            user_phone, 
            user_role) VALUES(
            ?,?,?,?
            ) 
        ''',(self.user_name ,
            self.user_email, 
            self.user_phone, 
            self.user_role ))
        conn.commit()

    def list_users(self):
        user = cur.execute('''
        SELECT * from users 
            ''')
        return user.fetchall()

    def update_user(self):

        cur.execute('''
            UPDATE users
            SET user_name = ?,
            user_email = ? , 
            user_phone = ?, 
            user_role = ? 
            WHERE user_id = ?''',(self.user_name ,self.user_email, self.user_phone, self.user_role,self.user_id))
        conn.commit()

    def delete_user(self):
        cur.execute('''
        DELETE FROM users WHERE user_id = ?
        ''',(self.user_id))
        conn.commit()

class Teams():
    def __init__(self,team_id,team_name,number_members,game,team_captain):
               self.team_id = team_id
               self.team_name = team_name
               self.number_members = number_members
               self.game = game
               self.team_captain = team_captain
    def create_team(self):
        cur.execute('''
            INSERT INTO teams(team_name,
            number_members
            ,game,
            team_captain) 
            VALUES(?,?,?,?)
        ''',( self.team_name,
              self.number_members,
              self.game,
              self.team_captain))
        conn.commit()
    
    def list_teams(self):
        team = cur.execute('''
        SELECT * from teams
            ''')
        return team.fetchall()

    def update_team(self):

        cur.execute('''
            UPDATE teams SET team_name = ?,
            number_members = ?
            ,game = ?,
            team_captain = ? 
            WHERE team_id = ?
        ''',( self.team_name,
              self.number_members,
              self.game,
              self.team_captain,self.team_id))
        conn.commit()

    def delete_team(self):
        cur.execute('''
        DELETE FROM teams WHERE team_id = ?
        ''',(self.team_id))
        conn.commit()
  
class Games():
    def __init__(self,game_id,game_name,game_gener):
        self.game_id = game_id
        self.game_name = game_name
        self.game_gener = game_gener
    
    def add_game(self):
        cur.execute('''
        INSERT INTO games(game_name,game_gener)
        VALUES(?,?)
        ''',(self.game_name,self.game_gener))
        conn.commit()
    
    def list_games(self):
        game = cur.execute(''' 
        SELECT * FROM games
        ''')
        return game.fetchall()
  
    def update_game(self):
        cur.execute('''
        UPDATE games SET game_name = ?,game_gener = ? 
         WHERE game_id = ?
        ''',(self.game_name,self.game_gener,self.game_id))
        conn.commit()

    def delete_game(self):
        cur.execute('''
        DELETE FROM games WHERE game_id = ?
        ''',(self.game_id))
        conn.commit()
class Matches():
    def __init__(self,match_id,tournament_id,match_no ,round_no ,scheduled_at,status ):
        self.match_id = match_id
        self.tournament_id = tournament_id
        self.match_no = match_no
        self.round_no = round_no 
        self.scheduled_at = scheduled_at
        self.status = status
    def add_match(self):
        cur.execute('''
        INSERT INTO matches(tournament_id ,match_no  ,round_no  ,scheduled_at ,status )
        VALUES(?,?,?,?,?)
        ''',(self.tournament_id ,self.match_no  ,self.round_no  ,self.scheduled_at ,self.status ))
        conn.commit()

    def list_matches(self):
        list_match = cur.execute('''
        SELECT * FROM matches
        ''').fetchall()
        return list_match
    def update_match(self):
        cur.execute('''
        UPDATE matches SET round_no  = ? ,scheduled_at = ?,status = ?
        WHERE match_id = ?
        ''',(self.round_no ,self.scheduled_at ,self.status,self.match_id))
        conn.commit()

    def delete_match(self):
        cur.execute('''
        DELETE FROM matches WHERE match_id = ?
        ''',(self.match_id,))
        conn.commit()

class leader_board():
    def __init__(self):
        pass


def delete_all_users():
    # Delete all rows from every table
    cur.execute("DELETE FROM users")
    cur.execute("DELETE FROM teams")
    cur.execute("DELETE FROM team_members")
    cur.execute("DELETE FROM games")
    cur.execute("DELETE FROM tournaments")
    cur.execute("DELETE FROM matches")
    cur.execute("DELETE FROM leader_board")

    conn.commit()

    


def get_table_names(db_path):
    try:
        # Connect to SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Query to get all table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

        # Extract table names into a list
        tables = [row[0] for row in cursor.fetchall()]

        return tables

    except sqlite3.Error as e:
        print("Error while fetching tables:", e)
        return []
    finally:
        if conn:
            conn.close()
if __name__  == "__main__":
    
    db_file = "database.db"
    table_list = get_table_names(db_file)
    print("Tables in database:", table_list)


    # user  = users("alice","alice@gmail.com","919378467732","captain")
    # user.create_user()
    # user = cur.execute('''
    # SELECT * FROM users
    # ''')
    # print(user.fetchall())
    # conn.close()

    # delete_all_users()
   