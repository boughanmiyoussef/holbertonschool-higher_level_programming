#!/usr/bin/python3
"""
HTTP Server with Python
"""

import http.server
import json


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    Simple HTTP request handler
    """

    def do_GET(self):
        """
        Handles GET requests.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')

        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not Found')


def run(server_class=http.server.HTTPServer,
        handler_class=SimpleHTTPRequestHandler):
    """
    Main function to run the server.
    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Starting server...')
    httpd.serve_forever()


if __name__ == "__main__":
    run()
