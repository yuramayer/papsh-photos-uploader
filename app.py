"""Main Flask App file"""

import os
from flask import (
    Flask,
    render_template,
    redirect,
    request,
    url_for
)
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user
)
from back_db.users import (
    init_db,
    get_user_by_username,
    UserLoginWrapper
)


app = Flask(__name__)
app.secret_key = os.urandom(24)


login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

init_db()


@login_manager.user_loader
def load_user(user_id):
    """"
    Download the user obj by id,
        for the flask-login
    """
    return UserLoginWrapper.get(user_id)


@app.route("/")
@login_required
def home():
    """
    The main page,
        accessible only for the authorized users
    """
    return render_template("home.html", username=current_user.username)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    User login handler
    GET: Shows login form
    POST: Tries the authentication for the guest
    """
    if request.method == "POST":
        user = get_user_by_username(request.form["username"])
        if user and user.check_password(request.form["password"]):
            login_user(user)
            return redirect(
                url_for("home", msg="Успешный вход ✨"))
        return render_template(
            'login.html', msg="Неверный логин или пароль 🌧")
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    """Logs out the user from the service"""
    logout_user()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
