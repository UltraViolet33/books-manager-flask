from .. import db

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description =  db.Column(db.String(300), nullable=True)


    def __init__(self, name, description=""):
        self.name = name
        self.description = description