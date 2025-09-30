from http.server import BaseHTTPRequestHandler, HTTPServer
import sys

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read content length from headers
        content_length = int(self.headers.get('Content-Length', 0))
        # Read request body
        body = self.rfile.read(content_length).decode('utf-8')
        
        # Print request body
        print(body)

        # Send basic response
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    server = HTTPServer(('', port), WebhookHandler)
    print(f"Starting server on port {port}...")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.server_close()
