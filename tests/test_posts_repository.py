from lib.posts_repository import PostsRepository
from lib.posts import Posts

def test_all(db_connection):
    posts_repository = PostsRepository(db_connection)
    posts = posts_repository.all()
    assert len(posts) == 5
    assert posts == [
        Posts(1, 'Hello World', 'My first post on Earth!', 5, 1),
        Posts(2, "I am Batman", "I am rich and I am Batman", 12, 2),
        Posts(3, 'My favorite book', 'Just finished reading Waterworld', 8, 3),
        Posts(4, 'Weekend plans', 'Saving the world!', 3, 4),
        Posts(5, 'NEWS FLASH!', 'I want to run in the Olympics', 3, 5)
    ]