from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return render_template('index.html')
    # user_agent = request.headers.get('User-Agent')
    # return f'<h1>Your browser is {user_agent}</!h1>'
    # return '<h1>Bad request</h1>', 400
    # return '<h1>Bad request</h1>'

# @app.route('/')
# def index():
# The make_response object and set cookie method
#     # response = make_response("<h2>This document has a cookie!</h2>")
#     # response.set_cookie('answer', '42')
#     # return response
# Redirect response object
#     return redirect('https://wwww.facebook.com')

# # Dynamic route
# @app.route('/user/<name>')
# def user(name):
#     return f"<h1>Hello, {name.lower()} </h1>" 

# Using the abort response object
# def load_user(id):
#     return f'user Id is {id}'

# @app.route('/user/<id>')
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return f'<h1>Hello, {user}</h1>'



if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()