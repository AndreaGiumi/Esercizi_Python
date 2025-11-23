from flask import Flask, url_for

app = Flask(__name__)

@app.route('/user/<string:nome>')
def home(nome: str) -> str:
    return f"<h3>{nome} sei bella</h3>"


@app.route('/user/<string:username>')
def show_user_profile(username: str) -> str:
    return f"Profilo di {username}"

@app.route('/post/<int:post_id>')
def show_post(post_id: int) -> int:
    return f"Post {post_id}"

@app.route('/user/<string:username>/age/<int:age>')
def how_user_profile(username: str, age: int) -> str:
    return f"Profilo di {username}: {age} anni"


app.run(debug=True)