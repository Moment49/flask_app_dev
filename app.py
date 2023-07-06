# from flask import Flask, render_template, url_for, redirect
# from flask_script import Manager
# from flask_bootstrap import Bootstrap
# from flask_moment import Moment
# from datetime import datetime


# app = Flask(__name__)
# manager = Manager(app)
# bootstrap = Bootstrap(app)
# moment = Moment(app)



# @app.route('/')
# def index():
#     return render_template('index.html', current_time=datetime.utcnow())
#     # user_agent = request.headers.get('User-Agent')
#     # return f'<h1>Your browser is {user_agent}</!h1>'
#     # return '<h1>Bad request</h1>', 400
#     # return '<h1>Bad requepst</h1>'

# # @app.route('/')
# # def index():
# # The make_response object and set cookie method
# #     # response = make_response("<h2>This document has a cookie!</h2>")
# #     # response.set_cookie('answer', '42')
# #     # return response
# # Redirect response object
# #     return redirect('https://wwww.facebook.com')
    # return render_template('index.html', current_time=datetime.utcnow())

# # # Dynamic route
# # @app.route('/user/<name>')
# # def user(name):
# #     return f"<h1>Hello, {name.lower()} </h1>" 

# # Using the abort response object
# # def load_user(id):
# #     return f'user Id is {id}'

# # @app.route('/user/<id>')
# # def get_user(id):
# #     user = load_user(id)
# #     if not user:
# #         abort(404)
# #     return f'<h1>Hello, {user}</h1>'

# @app.route('/user/<name>')
# def user(name):
#     if name == 'invalid':
#         return redirect(url_for('page_not'))
#     else:
#         return render_template('user.html', name=name)

# # @app.route('/item/')
# # def item():
# #     pack = 'Milk'
# #     return render_template('test.html', item=pack)

# #Handling custo errors pages
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# @app.route('/error-404')
# def page_not():
#     return render_template('404.html'), 404

# # @app.errorhandler(500)
# # def internal_server_error(e):
# #     return render_template('500.html'), 500


# if __name__ == '__main__':
#     app.run(debug=True)
#     # manager.run()