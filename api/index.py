from http.server import BaseHTTPRequestHandler
import json


# Create a custom HTTP request handler
class handler(BaseHTTPRequestHandler):
    # Define how to handle GET requests
    def do_GET(self):
        print("Here => ", self.path)
        if self.path == "/api":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(
                "Python API Example - Welcome to the homepage!".encode("utf-8")
            )
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_data = {"message": "Not Found", "status": "error"}
            json_error_data = json.dumps(error_data)
            self.wfile.write(json_error_data.encode("utf-8"))
