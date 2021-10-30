from . import db
from datetime import datetime


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, index=True, nullable=False, default=datetime.utcnow())
    author = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Note {}'.format(self.title)