import tornado.ioloop
import tornado.web
import datetime

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("Time:",datetime.datetime.now())
        print(self.request.body)
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()