import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the requested URL
        parsed_path = urllib.parse.urlparse(self.path)
        query_components = urllib.parse.parse_qs(parsed_path.query)
        requested_path = parsed_path.path

        # Print the HTTP request to the terminal
        print(f"Request: {self.requestline} from {self.client_address}")

        # Handle redirects
        if requested_path == "/so":
            self.send_response(307)
            self.send_header('Location', 'https://stackoverflow.com')
            self.end_headers()
        elif requested_path == "/itc":
            self.send_response(307)
            self.send_header('Location', 'https://itc.birzeit.edu')
            self.end_headers()
        # Handle image serving
        elif requested_path == "/get_image" and 'image' in query_components:
            image_name = query_components['image'][0]
            image_path = os.path.join('images', image_name)  # Path to the image folder
            
            if os.path.exists(image_path):
                # Serve the image
                self.send_response(200)
                if image_name.endswith(".jpg") or image_name.endswith(".jpeg"):
                    self.send_header('Content-Type', 'image/jpeg')
                elif image_name.endswith(".png"):
                    self.send_header('Content-Type', 'image/png')
                self.end_headers()

                with open(image_path, 'rb') as file:
                    self.wfile.write(file.read())
            else:
                # Return 404 if image not found
                self.send_response(404)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                error_page = f"""
                <html>
                <head><title>Error 404</title></head>
                <body>
                    <h1 style="color: blue;">The file is not found</h1>
                    <p><b>Amro Deek</b><br><b>1221642</b></p>
                    <p>Client IP: {self.client_address[0]}<br>Port: {self.client_address[1]}</p>
                </body>
                </html>
                """
                self.wfile.write(error_page.encode())
        # Handle the root request to serve the HTML form
        elif requested_path == "/" or requested_path == "/mySiteSTDID.html":
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            with open('mySiteSTDID.html', 'rb') as file:
                self.wfile.write(file.read())
        # Handle 404 error for any other request
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            error_page = f"""
            <html>
            <head><title>Error 404</title></head>
            <body>
                <h1 style="color: blue;">The file is not found</h1>
                <p><b>Amro Deek</b><br><b>1221642</b></p>
                <p>Client IP: {self.client_address[0]}<br>Port: {self.client_address[1]}</p>
            </body>
            </html>
            """
            self.wfile.write(error_page.encode())

def run(server_class=HTTPServer, handler_class=MyServer, port=1473):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run(port=1473)
