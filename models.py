from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy

class Employee(db.model):
    __tablename__="employees"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    team=db.Column(db.String(50),nullable=False)
     
    leave_requests=db.relationships(
        "LeaveRequests",
        back_populates="employee"
        cascade="all,delete-orphan"

     )
def __repr__(self):
    return f"<Employee{self.name}>"

class LeaveRequest(db.model):
    __tablename__="leave_requests"

    id=db.Column(db.Interger,primary_key=True)
    employee_id=db.Column(
        db.Interger,
        db.Foreign_key("employee.id")
        nullable="False"

    )
start_date=db.Column(db.Date,nullable=False)
end_date=db.Column(db.Date,nullable=False)
status=db.Column(
    db.String(100),
    nullable=False,
    default="Pending"
)
employee=db.relationship(
  "Employee",
  back_populates="leave_requests"

)
def __repr__(self):
    return (f"<LeaveRequest{self.employee_id}"
            f"{self.start_Date} {self.Status}>"
    )
class PublicHoliday(db.Model):
    __tablename__="Public_Holidays"
    id=db.Column(db.Integer,primary_key=True)
    date=db.Column(db.Date,nullsble=False,unique=True
                   
                   )
    name=db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return f"<Holiday{self.name}>"
