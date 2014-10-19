import tornado.ioloop
import tornado.web
import tornado.options
from core.uri_mapping import URI_MAPPING

paulashbourne = tornado.web.Application(URI_MAPPING)

if __name__ == "__main__":
    tornado.options.options['log_file_prefix'].set('/opt/logs/paulashbourne.log')
    tornado.options.parse_command_line()
    paulashbourne.listen(80)
    tornado.ioloop.IOLoop.instance().start()
