from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

#create application
app = Flask(__name__)


#create secret key; string can be anything must be secure
app.config['SECRET_KEY'] = 'nhatster'


#create form and inherit
class InfoForm(FlaskForm):
    '''
    Flask form that grab information about puppies
    inhert from Flask Form
    '''
    breed = StringField("What Breed are you?") # atrb
    submit = SubmitField("Submit") # submit button

@app.route('/', methods=['GET','POST']) #routed to home page
def index():
    breed = False # set breed attribute

    form = InfoForm()

    if form.validate_on_submit():
        '''
        grab the information from form.breed.data from the InfoForm
        form.x.data
        x = attribute you need
        '''
        breed = form.breed.data

        form.breed.data = '' # reset the form.breed.data

    return render_template('index.html',form=form, breed=breed)

if __name__ == '__main__':
    app.run(debug=True)
