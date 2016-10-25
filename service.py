"""service.py """

from __future__ import division
from google.appengine.ext import ndb

from models import ParentAccount, ChildInformation

class AccountService(object):
    @classmethod
    def create_parent_account(cls):
        # TODO: validate input, hash password, create account, make sure username is unique
        p = ParentAccount(username='lisa.benett',
                          password='psw',
                          email='lisa.howard1980@gmail.com',
                          first_name='Lisa',
                          last_name='Howard',
                          birthday='07/09/1981',
                          gender='F',
                          company='Unicorn',
                          position='Developer',
                          insurance='Kaiser',
                          insurance_number='123456789',
                          home_address='San Francisco',
                          work_address='San Francisco',
                          emergency_phone_number='123123123',
                          personal_phone_number='321321321'
                          )
        p.put()
        return

    @classmethod
    def create_child_info(cls):
        # TODO validate input, create account
        c = ChildInformation(
            '''
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
            '''
                          )
        c.put()
        return

    @classmethod
    def login(cls, username):
        # TODO validate input, check password, loginin, save cookies
        user = ParentAccount.query(ParentAccount.username == username).get()
        return user.first_name

    @classmethod
    def user_creation(cls, username, email, password):
        # temp method to have a name
        p = ParentAccount(username=username,
                          password=password,
                          email=email,
                          first_name='Lisa')
        user_key = p.put()
        user_id = user_key.id()

        return user_id
