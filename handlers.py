import tornado.web

class HomePageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/home.html")

class AboutPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/about.html")

class ProjectsPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/projects.html")

class ContactPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/contact.html")

class PasswordPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/password.html")

class ErrorPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Error")
