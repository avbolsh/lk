from flask import render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from . import auth
from .forms import LoginForm
from app.models import User


@auth.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(snils=form.snils.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(url_for("main.index"))
        flash("Неверный СНИЛС или пароль")
    return render_template("auth/login.html", form=form)


@auth.route("/logout/")
@login_required
def logout():
    logout_user()
    flash("Вы успешно вышли из личного кабинет сотрудника")
    return redirect(url_for("main.index"))