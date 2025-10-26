from lib.user import User
class UserRepository:
    def __init__(self, connection):
        self._connection = connection
        
        
    def all(self):
        rows = self._connection.execute('SELECT * FROM users;')
        users = []
        for row in rows:
            user = User(row['id'], row['email'], row['username'])
            users.append(user)
        return users
    
    
    def find(self, user_id):
        rows = self._connection.execute('SELECT * FROM users WHERE id = %s', [user_id])
        row = rows[0]
        return User(row['id'], row['email'], row['username'])
    
    
    def create(self, user):
        self._connection.execute('INSERT INTO users (email, username) VALUES (%s, %s)', [user.email, user.username])
        return None
    
    
    def delete(self, user_id):
        self._connection.execute('DELETE FROM users WHERE id = %s;', [user_id])
        return None