import tornado.ioloop
import tornado.web
import datetime

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("Time:",datetime.datetime.now())
        print(self.request.body)
        print(self.request)
        self.write("01 03 00 00 00 02 c4 0b")

    def post(self):
        print("Time:",datetime.datetime.now())
        print(self.request.body)
        print(self.request)
        self.write("01 03 00 00 00 02 c4 0b")

def make_app():
    return tornado.web.Application([
        (r"/iot", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()

    