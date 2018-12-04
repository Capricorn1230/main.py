import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def get(self,n):
        n = int(n)
        html='''
        <html>
        <body>
        <table>
        '''  
        for i in range(1 ,n+1):
            html += '<TR>'
            for j in range ( 1, n+1):
                 if i <= j:
                   html += '<TD>%d*%d=%2d</td>'%(i , j , i*j)
            html += '</TR>'
        html +='''
        </table>
        </body>
        </html>
        '''
        self.write(html)
application = tornado.web.Application([
    (r"/([0-9]+)", MainHandler),
], debug = True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()