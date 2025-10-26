from lib.user_repository import UserRepository
from lib.user import User


"""
given the seeds data.
returns all records
"""
def test_get_all_users(db_connection):
    db_connection.seed('seeds/social_network.sql')
    
    user_repository = UserRepository(db_connection)
    users = user_repository.all()
    assert users == [
        User(1, 'superman@solitude.com', 'Superman'),
        User(2, 'batman@batcave.com', 'Batman'),
        User(3, 'aquaman@atlantis.com', 'Aquaman'),
        User(4, 'wonderwoman@amazon.com', 'Wonderwoman'),
        User(5, 'flash@flash.com', 'Barry')
]
    
    
"""
given we call the find method
returns one record
"""
def test_find_method(db_connection):
    db_connection.seed('seeds/social_network.sql')
    user_repository = UserRepository(db_connection)
    result = user_repository.find(1)
    assert result == User(1, 'superman@solitude.com', 'Superman')
    
    
"""
given we call the create method
creates a new record
"""
def test_create_record(db_connection):
    db_connection.seed('seeds/social_network.sql')
    user_repository = UserRepository(db_connection)
    user_repository.create(User(None, 'spiderman@spidermail.com', 'Spider Man'))
    
    result = user_repository.all()
    assert result == [
        User(1, 'superman@solitude.com', 'Superman'),
        User(2, 'batman@batcave.com', 'Batman'),
        User(3, 'aquaman@atlantis.com', 'Aquaman'),
        User(4, 'wonderwoman@amazon.com', 'Wonderwoman'),
        User(5, 'flash@flash.com', 'Barry'),
        User(6, 'spiderman@spidermail.com', 'Spider Man'),
    ] 
    
    
"""
given we want to delete a
it returns the list wihtout the deleted record
"""
def test_delete_method(db_connection):
    db_connection.seed('seeds/social_network.sql')
    user_repository = UserRepository(db_connection)
    
    user_repository.delete(6)
    result = user_repository.all()
    assert result == [
        User(1, 'superman@solitude.com', 'Superman'),
        User(2, 'batman@batcave.com', 'Batman'),
        User(3, 'aquaman@atlantis.com', 'Aquaman'),
        User(4, 'wonderwoman@amazon.com', 'Wonderwoman'),
        User(5, 'flash@flash.com', 'Barry'),
    ]