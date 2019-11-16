from build import build_app
from middleware import proxyable

app = build_app()


@app.route("/")
def root():
    return "Hello, World!"


@app.route("/user")
def user_index():
    return "Users"


@app.route("/user/<username>")
@proxyable
def user_show(username):
    return "User %s" % username


@app.route("/post")
def post_index():
    return "Posts"


@app.route("/post/<int:post_id>")
@proxyable
def post_show(post_id):
    return "Post %d" % post_id
