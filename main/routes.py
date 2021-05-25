from flask import Blueprint, url_for, redirect, render_template, request
from main.forms import LoginForm, RegistrationForm

from user import User

from dbhelper import DBHelper
from passwordhelper import PasswordHelper

from flask_login import login_user
from flask_login import logout_user


DB = DBHelper()
PH = PasswordHelper()


main = Blueprint('main', __name__)


@main.route("/")
def home():
    return render_template("home.html", loginform=LoginForm(), registrationform=RegistrationForm())


@main.route("/login", methods=["POST"])
def login():
    form = LoginForm(request.form)
    if form.validate():
        stored_user = DB.get_user(form.loginemail.data)
        if stored_user and PH.validate_password(form.loginpassword.data, stored_user['salt'], stored_user['hashed']):
            user = User(form.loginemail.data)
            login_user(user, remember=True)
            return redirect(url_for('tables.account'))
        form.loginemail.errors.append("Email or password invalid")
    return render_template("home.html", loginform=form, registrationform=RegistrationForm())


@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))


@main.route("/register", methods=["POST"])
def register():
    form = RegistrationForm(request.form)
    if form.validate():
        if DB.get_user(form.email.data):
            form.email.errors.append("Email address already registered")
            return render_template("home.html", loginform=LoginForm(), registrationform=form)
        salt = PH.get_salt()
        hashed = PH.get_hash(form.password2.data + salt)
        DB.add_user(form.email.data, salt, hashed)
        return render_template("home.html", loginform=LoginForm(), registrationform=form,
                               onloadmessage="Registration successful. Please log in.")
    return render_template("home.html", loginform=LoginForm(), registrationform=form)
