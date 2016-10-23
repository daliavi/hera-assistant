"""service.py """

from __future__ import division
from collections import namedtuple
from google.appengine.ext import ndb
from collections import Counter
import operator
import itertools
from datetime import datetime, timedelta
import logging
from models import ParentAccount, ChildInformation

class AccountService(object):
    # game handling methods
    @classmethod
    def create_parent_account(cls):
        p = ParentAccount(username='lisa.benett',
                          password='lisa.howard',
                          email='lisa.howard@gmail.com',
                          first_name='Lisa',
                          last_name='Howard',
                          birthday='07/09/1981',
                          gender='F',
                          company='Unicorn',
                          position='Developer',
                          insurance='Kaiser',
                          insurance_number='123456789',
                          home_address='2443 117yh ave, San Francisco',
                          work_address='655 Mongomery, San Francisco',
                          emergency_phone_number='4154154155',
                          personal_phone_number='4155428868'
                          )
        p.put()
        return

    @classmethod
    def create_child_info(cls):
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
        ''' check user credentials on login'''
        user = ParentAccount.query(ParentAccount.username == username).get()
        return user.first_name

    @classmethod
    def user_creation(cls, username, email, password):
        p = ParentAccount(username=username,
                          password=password,
                          email=email,
                          first_name='Lisa')
        user_key = p.put()
        user_id = user_key.id()

        return user_id
