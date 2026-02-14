import main

# Use the cursor from main
cur = main.cur

print("=== Testing Users ===\n")
u = main.Users(None, "Alice", "Alice@example.com", "976694211", "Player")
u.create_user()
print("Users after insert:", u.list_users())
u.user_id = "1"
u.user_name = "Alice Updated"
u.update_user()
print("Users after update:", u.list_users())
u.delete_user()
print("Users after delete:", u.list_users())

print("\n=== Testing Teams ===\n")
t = main.Teams(None, "Warriors", 5, "Chess", "Alice")
t.create_team()
print("Teams after insert:", t.list_teams())
t.team_id = "1"
t.team_name = "Warriors Updated"
t.update_team()
print("Teams after update:", t.list_teams())
t.delete_team()
print("Teams after delete:", t.list_teams())

print("\n=== Testing Games ===\n")
g = main.Games(None, "Chess", "Strategy")
g.add_game()
print("Games after insert:", g.list_games())
g.game_id = "1"
g.game_name = "Chess Updated"
g.update_game()
print("Games after update:", g.list_games())
g.delete_game()
print("Games after delete:", g.list_games())

print("\n=== Testing Matches ===\n")
m = main.Matches(None, 1, 1, 1, "2026-02-20", "Scheduled")
m.add_match()

# Get the last inserted match_id
last_id = cur.execute("SELECT MAX(match_id) FROM matches").fetchone()[0]
m.match_id = last_id

print("Matches after insert:", m.list_matches())

# Update
m.round_no = 2
m.scheduled_at = "2026-02-21"
m.status = "Completed"
m.update_match()
print("Matches after update:", m.list_matches())

# Delete
m.delete_match()
print("Matches after delete:", m.list_matches())
