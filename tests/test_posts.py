from lib.posts import Posts

"""
given that the post constructs with title, content, 
number_of_views, user_id
returns post with neccessary fields
"""
def test_post_construct():
    posts = Posts(1, 'Hello World', 'My first post on Earth!', 5, 1)
    assert posts.id == 1
    assert posts.title == 'Hello World'
    assert posts.content == 'My first post on Earth!'
    assert posts.number_of_views == 5
    assert posts.user_id == 1
    
"""
given two identical posts
it returns as equal
"""
def test_posts_for_equality():
    post1 = Posts(1, 'Hello World', 'My first post on Earth!', 5, 1)
    post2 = Posts(1, 'Hello World', 'My first post on Earth!', 5, 1) 
    assert post1 == post2
    
"""
given that a post,
is returned in correct format
"""
def test_posts_format():
    posts = Posts(1, 'Hello World', 'My first post on Earth!', 5, 1)
    assert str(posts) == "Posts(1, Hello World, My first post on Earth!, 5, 1)"