import string
from datetime import datetime
from random import choices
from flask import request
from .extensions import db 

class Link(db.Model):
    __tablename__='link'
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    # suffix = db.Column(db.String(6),unique=True)
    short_url = db.Column(db.String(6), unique=True)
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_link()
        # short_url = Link(short_url=short_url)
        # db.session.add(short_url)
        # db.session.commit()

    def generate_short_link(self):
        # suffix_url= request.form['suffix_url']
        # suffix=Link(suffix=suffix_url)
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=6))

        link = self.query.filter_by(short_url=short_url).first()
        
        if link:
           
            return self.generate_short_link()
        
        return short_url