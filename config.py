import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" +
        os.path.join(BASE_DIR, "instance", "leave_scheduler.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "leave-scheduler-secret-key"