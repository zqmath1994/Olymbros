import  tornado.httpserver
import  tornado.ioloop
import  tornado.options
import  tornado.web
import  pandas as pd
import  os
from tornado.options import define, options
define("port", default=9002, help="run on the given port", type=int)
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class UploadHandler(tornado.web.RequestHandler):
    def get(self):
        file_path = self.get_argument("file");
        data = pd.read_csv(file_path,nrows=10)
        json_data = data.to_json()
        print json_data
        self.write(json_data)

if __name__ ==  "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r"/", IndexHandler),(r"/upload",UploadHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
