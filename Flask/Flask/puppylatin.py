
"""
!= y > add "y"
== y > add "iful"

"/"
Welcome! Go to /puppy_latin/name to see your name in puppy latin!

"/puppy_latin/name"
hi rufus your puppylatin name is spottiful
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')     # set route for application
                    # this is a single page application
                    # http://127.0.0.1:5000/
def index():
    return '<h1>Welcome! Go to /puppy_latin/name to see your name in puppy latin!</h1>'
    # this return the string to the browser "Hello Puppy"


@app.route('/puppy_latin/<name>')
def puppy(name):
    latin = ''
    if name[-1] != "y":
        latin = name+"y"

    elif name[-1] == "y":
        latin = name[:-1]+"iful"

    return "<h1>Hi {}, your puppy latin name is {}</h1>".format(name,latin)

if __name__ == '__main__':
    app.run(debug = True)
