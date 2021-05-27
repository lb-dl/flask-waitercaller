import datetime

from flask import Blueprint, url_for, redirect, render_template, request
from sql.dbhelper import DBHelper
from flask_login import login_required
from flask_login import current_user

DB = DBHelper()


users = Blueprint('users', __name__)


@users.route("/newrequest/<tid>")
def new_request(tid):
    if DB.add_request(tid, datetime.datetime.now()):
        return "Your request has been logged and a waiter will be with you shortly"
    return "There is already a request waiting for this table. A waiter will be there ASAP"


@users.route("/dashboard")
@login_required
def dashboard():
    now = datetime.datetime.now().replace(microsecond=0)
    requests = DB.get_requests(current_user.get_id())
    for req in requests:
        deltaseconds = (now - req['time']).seconds
        req['wait_minutes'] = "{}.{}".format((deltaseconds/60), str(deltaseconds % 60).zfill(2))

    return render_template("dashboard.html", requests=requests)


@users.route("/dashboard/resolve")
@login_required
def dashboard_resolve():
    request_id = request.args.get("request_id")
    DB.delete_request(request_id)
    return redirect(url_for('users.dashboard'))
