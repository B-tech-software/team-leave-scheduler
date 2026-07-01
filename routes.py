from flask import Blueprint, render_template
from models import Employee, LeaveRequest


main = Blueprint("main", __name__)


@main.route("/")
def index():

    employees = Employee.query.all()

    approved_requests = LeaveRequest.query.filter_by(
        status="Approved"
    ).all()

    pending_requests = LeaveRequest.query.filter_by(
        status="Pending"
    ).all()

    return render_template(
        "index.html",
        employees=employees,
        approved_requests=approved_requests,
        pending_requests=pending_requests,
    )