from flask import Flask

app = Flask(__name__)

@app.route('/')     # set route for application
                    # this is a single page application
                    # http://127.0.0.1:5000/
def index():
    return '<h1>Hello Puppy</h1>'
    # this return the string to the browser "Hello Puppy"

@app.route('/info') # http://127.0.0.1:5000/info
def info():
    return '<h1>Puppies are alright</h1>'
    # this return the string to the browser "Hello Puppy"

@app.route('/puppy/<name>')
def puppy(name):
    return "100th letter: {}".format(name[100])

if __name__ == '__main__':
    app.run(debug = True)
