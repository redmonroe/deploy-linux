
from datetime import date, datetime
from hashlib import md5
from time import time
from flask import current_app, request, url_for
from app import db
from sqlalchemy import or_, and_, extract, between
from flask_sqlalchemy import SQLAlchemy


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    name = db.Column(db.String)
    inorex = db.Column(db.String)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        spacer = '**'
        return f'{self.name:-^40} {spacer:>2} {self.inorex:^20}'


cat = Categories()
cat.name = 'test'
db.session.add(cat)
db.session.commit()

result = Categories.query.all()
for item in result:
    print(item)