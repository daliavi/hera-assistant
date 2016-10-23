import webapp2
import logging
from handlers import NewUserHandler, MainHandler, NewDependantHandler, LoginHandler, AppointmentHandler, SignupHandler,\
    PersonalInfoHandler, UserHomeHandler

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LoginHandler),
    ('/newuser', NewUserHandler),
    ('/newdependant', NewDependantHandler),
    ('/appointment', AppointmentHandler),
    ('/signup', SignupHandler),
    ('/personalinfo', PersonalInfoHandler),
    ('/userhome', UserHomeHandler)
], debug=True)

