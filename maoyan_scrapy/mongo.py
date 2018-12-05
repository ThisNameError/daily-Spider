from mongoengine import *


class Movie(Document):
    title = StringField(max_length=512)
    actor = StringField(max_length=512)
    time = StringField(max_length=512)
