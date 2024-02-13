import praw

reddit = praw.Reddit(
    client_id='Hl-XfrsTKGbYiQTUDQCACg',
    client_secret="-nnMfnVu0V5OvGJMWP3MB0DdFQgJsw",
    user_agent="u/BeniFissha",
)

subreddit = reddit.subreddit("python")

top_posts = subreddit.top(limit=10)
new_posts = subreddit.new(limit=10)

for post in top_posts:
    print("--------------------------------")
    print("Title: ", post.title)
    print("Id- ",post.id)
    print("Author: ", post.author)
    print("url: ", post.url)
    print("Score: ", post.score)
    print("Comment count: ", post.num_comments)

post = reddit.submission(id="iehths")

comments = post.comments
for comment in comments[:5]:

    print("Comment body- ", comment.body)
