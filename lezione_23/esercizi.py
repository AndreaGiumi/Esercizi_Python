from flask import Flask, url_for

app = Flask(__name__)

@app.route('/square/<int:num>')
def square(num: int) -> str: 
    return f"<p>{num**2}</p>"

@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int) -> str: 
    return f"<p>{a + b}</p>"

@app.route('/user/<string:nome>')
def benvenuto(nome: str) -> str:
    return f"Benvenuto {nome}"

@app.route('/')
def about() -> str:
    return "<p>Ciao sono Andrea ho 28 anni e vengo dalla città più bella di tutte <strong>CASSINO!!!!</strong></p>"

@app.route('/homepage/')
def homepage():
    print(url_for('about'))
    print(url_for('benvenuto', nome="Andrea")) 
    return "Controlla la console per gli URL generati"

if __name__ == '__main__':
    app.run(debug=True)