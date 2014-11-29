import tornado.ioloop
import tornado.web
from core.uri_mapping import URI_MAPPING

paulashbourne = tornado.web.Application(URI_MAPPING)

if __name__ == "__main__":
    paulashbourne.listen(80)
    tornado.ioloop.IOLoop.instance().start()
