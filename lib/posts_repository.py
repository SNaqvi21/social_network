from lib.posts import Posts
class PostsRepository:
    def __init__(self, connection):
        self._connection = connection
        
    def all(self):
        rows = self._connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows:
            post = Posts(row['id'], row['title'], row['content'], row['number_of_views'], row['user_id'])
            posts.append(post)
        return posts