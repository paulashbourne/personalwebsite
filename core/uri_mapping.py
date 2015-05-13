from tornado.web import URLSpec, StaticFileHandler
import handlers as h

URI_MAPPING = [
    URLSpec(r'/', h.HomePageHandler),
    URLSpec(r'/about', h.AboutPageHandler),
    URLSpec(r'/projects', h.ProjectsPageHandler),
    URLSpec(r'/contact', h.ContactPageHandler),
    URLSpec(r'/password', h.PasswordPageHandler),
    URLSpec(r'/static/(.*)', StaticFileHandler, {'path': 'static/'}),
    URLSpec(r'.*', h.ErrorPageHandler),
]
