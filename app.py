from flask import Flask, render_template
from config import Config
from models import db, Employee



app = Flask(__name__)
app.config.from_object(Config)
db.init_app

@app.route("/")
def home():
    manager_name="Blessing"

    return render_template("index.html", manager_name=manager_name,
                           company="Imaging Solutions",
                           days="30",employees=["Bee,Jee","Ree","Tee","lee"]
                        
                        
                           
                           
                           
                           )

 @app.route("/add-Employee")
def add-Employee():
employee=Employee(
    name="Blessing"
    team="Engineering"
)
db.session.add(employee)
db.session.commit()
return "Employee added succsfuly"




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
