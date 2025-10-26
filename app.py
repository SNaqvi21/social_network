from lib.user import User
from lib.database_connection import DatabaseConnection
from lib.user_repository import UserRepository

# Connect to the database
connection = DatabaseConnection()
connection.connect() 

# Seed with some seed data
connection.seed("seeds/social_network.sql") # popultes the 

# Retrieve all users
user_repository = UserRepository(connection)
users = user_repository.all()

# # List them out
for user in users:
    print(f"User({user.id}, {user.email}, ({user.username})")

# Retrieve all albums
user_repository = UserRepository(connection)
users = user_repository.all()

# List the albums out
# for album in albums:
#     print(f"{album.id}:'{album.title}'({album.release_year})|{album.artist_id}")