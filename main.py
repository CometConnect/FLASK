from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "Alex"
    age = "12"
    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():
    name = "Mark"
    age = 40
    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mother")
def mother():
    name = "Erica"
    age = 37
    return render_template('mother.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/friend")
def friend():
    name = "Victor"
    age = 12
    return render_template('friend.html' , name = name , age = age)

if __name__  ==  '__main__':
    app.run(debug=True)