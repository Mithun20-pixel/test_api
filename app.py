from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Sample data
albums = [
    {"id": 1, "title": "Album 1", "artist": "Artist 1"},
    {"id": 2, "title": "Album 2", "artist": "Artist 2"}
]

posts = [
    {"id": 1, "title": "Post 1", "content": "Content 1"},
    {"id": 2, "title": "Post 2", "content": "Content 2"}
]

comments = [
    {"id": 1, "text": "Comment 1", "author": "Author 1"},
    {"id": 2, "text": "Comment 2", "author": "Author 2"}
]

# HTML Routes
@app.route('/')
def home():
    return render_template('album.html')

@app.route('/album')
def album():
    return render_template('album.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/comments')
def comments_page():
    return render_template('comments.html')

# API Routes
@app.route('/api/albums')
def get_albums():
    return jsonify(albums)

@app.route('/api/posts')
def get_posts():
    return jsonify(posts)

@app.route('/api/comments')
def get_comments():
    return jsonify(comments)

if __name__ == '__main__':
    app.run(debug=True)
