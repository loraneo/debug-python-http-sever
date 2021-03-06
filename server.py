#!/usr/bin/env python
# Reflects the requests from HTTP methods GET, POST, PUT, and DELETE
# Written by Nathan Hamiel (2010)

import sys
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        request_path = self.path

        print("\n----- Request Start ----->\n")
        print(request_path)
        print(self.headers)
        print("<----- Request End -----\n")

        self.send_response(200)
        self.send_header("Set-Cookie", "foo=bar")
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>Title goes here.</title></head>")
        self.wfile.write("<body><p>Hi Michael!</p>")
        self.wfile.write("<p>You accessed path: %s</p>" % self.path)
        self.wfile.write("<pre>")
        self.wfile.write("%s" % self.headers)
        self.wfile.write("</pre>")
        
        self.wfile.write("</body></html>")

    def do_POST(self):

        request_path = self.path

        print("\n----- Request Start ----->\n")
        print(request_path)

        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0

        print(request_headers)
        print(self.rfile.read(length))
        print("<----- Request End -----\n")

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>Title goes here.</title></head>")
        self.wfile.write("<body><p>Hi Michael!</p>")
        self.wfile.write("<p>You accessed path: %s</p>" % self.path)
        self.wfile.write("<pre>")
        self.wfile.write("%s" % self.headers)
        self.wfile.write("</pre>")

    do_PUT = do_POST
    do_DELETE = do_GET
    do_HEAD = do_GET

def main():
    port = 8080
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = ("Creates an http-server that will echo out any GET or POST parameters\n"
                    "Run:\n\n"
                    "   reflect")
    (options, args) = parser.parse_args()

    main()
