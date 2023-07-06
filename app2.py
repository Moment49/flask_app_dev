from flask import Flask, render_template, url_for, redirect, session, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
# from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))


app2 = Flask(__name__)
app2.config['SECRET_KEY'] = 'hard to guess string'
app2.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app2.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# Additional extensions to enable dev
db = SQLAlchemy(app2)
manager = Manager(app2)
bootstrap = Bootstrap(app2)
moment = Moment(app2)


@app2.route('/', methods = ['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
     
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name')
            
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))
  

# Creating the form
class NameForm(FlaskForm):
    name = StringField('Enter your name to login?', validators=[DataRequired()])
    submit = SubmitField('submit')

# Role and User model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>'


if __name__ == '__main__':
    app2.run(debug=True) 