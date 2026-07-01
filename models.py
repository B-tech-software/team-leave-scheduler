from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Employee(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    team = db.Column(db.String(50), nullable=False)

    leave_requests = db.relationship(
        "LeaveRequest",
        back_populates="employee",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<Employee {self.name}>"


class LeaveRequest(db.Model):
    __tablename__ = "leave_requests"

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employees.id"),
        nullable=False,
    )
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    status = db.Column(
        db.String(100),
        nullable=False,
        default="Pending",
    )

    employee = db.relationship(
        "Employee",
        back_populates="leave_requests",
    )

    def __repr__(self):
        return f"<LeaveRequest {self.employee_id} {self.start_date} {self.status}>"


class PublicHoliday(db.Model):
    __tablename__ = "public_holidays"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Holiday {self.name}>"
