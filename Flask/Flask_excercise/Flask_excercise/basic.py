from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/requirementchecks')
def Username_check():
    username = request.args.get('Username')
    upper=False
    lower=False
    num=False
    for i in username:
        if i.isupper()==True:
            upper = True
        if i.islower()==True:
            lower = True
    if username[-1] in "1234567890":
        num=True

    print("upper:{}".format(upper))
    print("lower:{}".format(lower))
    print("num:{}".format(num))

    return render_template("requirementcheck.html",upper=upper,lower=lower,num=num,username=username)




if __name__ == '__main__':
    app.run(debug=True)
