from lib.user import User

"""
User constructs with an id, email and username
"""
def test_user_constructs():
    user = User(1, 'superman@solitude.com', 'Superman')
    assert user.id == 1
    assert user.email == 'superman@solitude.com'
    assert user.username == 'Superman'
    
    
"""
Given two identical records, 
it returns them as equal
"""
def test_two_records_for_equal_value():
    user1 = User(1, 'superman@solitude.com', 'Superman')
    user2 = User(1, 'superman@solitude.com', 'Superman')
    assert user1 == user2
    
    
"""
Given the output,
it returns it nicely formatted
"""
def test_correct_formatting():
    user = User(1, 'Test Email', 'Test Username')
    assert str(user) == "User(1, Test Email, Test Username)"