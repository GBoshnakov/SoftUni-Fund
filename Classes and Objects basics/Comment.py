class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes

comment = Comment(username= "user1", content="I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)

print(comment)