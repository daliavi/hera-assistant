import os
import jinja2
import webapp2

from service import AccountService

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


class AssistantHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainHandler(AssistantHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        if self.request.POST.get('login'):
            username = self.request.get("username")
            user = AccountService.login(username)
            self.render("user_home.html", user=user)
        elif self.request.POST.get('signup'):
            self.redirect("/signup")


class LoginHandler(AssistantHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        user = AccountService.login()
        self.render("user_home.html")


class NewUserHandler(AssistantHandler):
    def get(self):
        self.render("new_user.html")

    def post(self):
        if self.request.POST.get('signup_account'):
            first_name = self.request.get("first_name")
            self.render("new_child.html")
        else:
            self.redirect('/')


class NewDependantHandler(AssistantHandler):
    def get(self):
        self.render("new_child.html")


class AppointmentHandler(AssistantHandler):
    def get(self):
        self.render("appointment.html")


class PersonalInfoHandler(AssistantHandler):
    def get(self):
        self.render("personal_info.html")


class UserHomeHandler(AssistantHandler):
    def get(self):
        self.render("user_home.html", user="Lisa")


class SignupHandler(AssistantHandler):
    def get(self):
        self.render("signup.html")

    def post(self):
        if self.request.POST.get('signup'):
            username = self.request.get("username")
            email = self.request.get("email")
            password = self.request.get("password")
            user_id = AccountService.user_creation(username=username,
                                                password=password,
                                                email=email
                                                   )
            self.render("new_user.html", username=user_id)
        else:
            self.redirect('/')
