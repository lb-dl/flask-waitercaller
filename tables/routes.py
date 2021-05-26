from flask import Blueprint, url_for, redirect, render_template, request
from .forms import CreateTableForm

from dbhelper import DBHelper
from bitlyhelper import BitlyHelper
from qrhelper import QRHelper

from flask_login import login_required
from flask_login import current_user

import config

DB = DBHelper()
BH = BitlyHelper()
QR = QRHelper()


tables = Blueprint('tables', __name__)


@tables.route("/account")
@login_required
def account():
    tables = DB.get_tables(current_user.get_id())
    return render_template("account.html", createtableform=CreateTableForm(), tables=tables)


@tables.route("/account/deletetable")
@login_required
def account_deletetable():
    tableid = request.args.get("tableid")
    DB.delete_table(tableid)
    return redirect(url_for('tables.account'))


@tables.route("/account/createtable", methods=["POST"])
@login_required
def account_createtable():
    form = CreateTableForm(request.form)
    if form.validate():
        tableid = DB.add_table(form.tablenumber.data, current_user.get_id())
        owner = current_user.email
        table_num = DB.get_table(tableid)["number"]
        new_url = BH.shorten_url(config.base_url + "newrequest/" + str(tableid))
        QR.make_qrcode(new_url, owner, table_num)
        DB.update_table(tableid, new_url)
        return redirect(url_for('tables.account'))
    return render_template("account.html", createtableform=form, tables=DB.get_tables(current_user.get_id()))
