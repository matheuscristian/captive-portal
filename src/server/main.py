from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define the HTML file to be served
HTML_FILE = "src/global/pages/index.html"

# Define the HTTP request handler class
class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    # Handle GET requests
    def do_GET(self):
        # Check if the requested path is the root path "/"
        if self.path == '/':
            # Set response status code
            self.send_response(200)
            # Set headers
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # Read the content from the HTML file
            with open(HTML_FILE, 'rb') as file:
                content = file.read()
            # Write the response content
            self.wfile.write(content)
        else:
            # If the requested path is not the root path, serve files as usual
            super().do_GET()

# Define the main function
def main():
    # Set the server address
    server_address = ('', 8000)
    # Create an instance of HTTP server
    httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
    # Print a message indicating the server has started
    print('Server started on port 8000...')
    # Start the HTTP server
    httpd.serve_forever()

# Check if the script is being run directly
if __name__ == '__main__':
    # Call the main function
    main()
