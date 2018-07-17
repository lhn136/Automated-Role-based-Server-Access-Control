from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # name = "Nhat"
    # letters = list(name)
    # pup_dictionary={'Nhat':10,'Loc':11}
    user_login_in =True
    return render_template('basic.html',user_login_in=user_login_in)

if __name__ == '__main__':
    app.run(debug=True)
