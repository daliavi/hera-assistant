"""models.py - File describing data models."""

from google.appengine.ext import ndb


class ParentAccount(ndb.Model):
    username = ndb.StringProperty()
    password = ndb.StringProperty()
    email = ndb.StringProperty()
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    birthday = ndb.StringProperty()
    gender = ndb.StringProperty()
    company = ndb.StringProperty()
    position = ndb.StringProperty()
    insurance = ndb.StringProperty()
    insurance_number = ndb.StringProperty()
    home_address = ndb.StringProperty()
    work_address = ndb.StringProperty()
    emergency_phone_number = ndb.StringProperty()
    personal_phone_number = ndb.StringProperty()
    children = ndb.KeyProperty(kind='ChildInformation', repeated=True)


class ChildInformation(ndb.Model):
    parent_account = ndb.KeyProperty(kind='ParentAccount')
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    birthday = ndb.StringProperty()
    birth_place = ndb.StringProperty()
    insurance = ndb.StringProperty()
    insurance_number = ndb.StringProperty()
    home_address = ndb.StringProperty()
    school_address = ndb.StringProperty()
    gender = ndb.StringProperty()
    emergency_phone_number = ndb.StringProperty()
