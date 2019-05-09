from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop
from app import main



class VideoHandler(RequestHandler):
    def get(self):
        main()
        self.write("Done")

if __name__ == "__main__":
    handler_mapping = [(r'/process_video', VideoHandler)]
    application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()
