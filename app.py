from flask import Flask, request

app = Flask(__name__)

# ALL OF THESE ARE GET REQUEST
# The @ is called a decorator
# The home route
@app.route("/")
def home_page():
    html = """
    <html>
        <body>
            <h1>Home Page</h1>
            <p>Welcome to my home page</p>
            <a href='/hello'>Go to hello page</a>
        </body>
    </html>
    """
    return html


# The @ is called a decorator
@app.route('/hello')
def say_hello():
    html = """
    <html>
        <body>
            <h1>Hello!</h1>
            <p>This is the hello page</p>
        </body>
    </html>
    """
    return html
    

@app.route('/goodbye')
def say_bye():
    return "GOOD BYE!!!"
 
# handling query strings for GET requests
@app.route('/search')
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1>Search results for: {term}</h1> <p>Sorting by: {sort}</p>"


# POST REQUEST
# @app.route("/post", methods=["POST"])
# def post_demo():
#     return "YOU MADE A POST REQUEST!"

# @app.route("/post", methods=["GET"])
# def get_demo():
#     return "YOU MADE A GET REQUEST!"

# This is a GET request
@app.route('/add-comment')
def add_comment_form():
    return """
    <h1>Add Comment</h1>
    <form method="POST">
        <input type='text' placeholder='comment' name='comment'/>
        <input type='text' placeholder='username' name='username'/>
        <button>Submit</button>
    </form>
    """

# This is a POST request
# You can send both GET and POST requests to the same url/path
@app.route('/add-comment', methods=["POST"])
def save_comment():
    comment = request.form["comment"]
    username = request.form["username"]
    return f"""
        <h1>SAVED YOUR COMMENT</h1>
        <ul>
            <li>Username:{username}</li>
            <li>Comment:{comment}</li>
        </ul>
    """
    

# DYNAMIC PATH VARIABLES
@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f"<h1>Browsing the {subreddit} subreddit</h1>"

# Having multiple variables within a single route
@app.route("/r/<subreddit>/comments/<int:post_id>")
def show_comments(subreddit, post_id):
    return f"<h1>Viewing comments for post with id: {post_id} from the {subreddit} Subreddit</h1>"

POSTS = {
    1: "I like chicken tenders",
    2: "I hate mayo",
    3: "Double rainbow all the way",
    4: "YOLO OMG (kill me)"
}

@app.route('/posts/<int:id>')
def find_post(id):
    # post = POSTS[id]
    post = POSTS.get(id, "Post not found")
    return f"<p>{post}</p>"


# URL PARAMS VS QUERY PARAMS
# This is a URL parameter ---> /shop/<toy> 
    # Feels more like "subject of page", the <toy> variable is the subject
# This is a Query parameter ---> /shop?toy=elmo
    # Feels more like "extra info about page", like a modifier, often used when coming from form