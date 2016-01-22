import tornado.ioloop
import tornado.web
from core.uri_mapping import URI_MAPPING

settings = {
    'debug' : True
}

paulashbourne = tornado.web.Application(
    URI_MAPPING,
    **settings
)

if __name__ == "__main__":
    print "Server starting..."
    paulashbourne.listen(8888)
    print "Server listening on port 8888"
    tornado.ioloop.IOLoop.instance().start()
