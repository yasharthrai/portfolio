#!/usr/bin/env python3
"""
Yasharth Rai - Portfolio
Simple HTTP server using built-in modules (no external dependencies)
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import json
import os

PORT = 8000
HOST = "localhost"

class PortfolioHandler(SimpleHTTPRequestHandler):
    """Serve static files and handle routing"""
    
    def do_GET(self):
        """Handle GET requests"""
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            
            # Read and serve the HTML template
            html_file = Path(__file__).parent / "templates" / "index.html"
            if html_file.exists():
                with open(html_file, "r", encoding="utf-8") as f:
                    self.wfile.write(f.read().encode("utf-8"))
            else:
                self.wfile.write(b"<h1>Portfolio page not found</h1>")
        
        elif self.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"status": "ok", "service": "Yasharth Rai - Portfolio"}
            self.wfile.write(json.dumps(response).encode("utf-8"))
        
        else:
            # Try to serve static files
            super().do_GET()
    
    def log_message(self, format, *args):
        """Custom logging"""
        print(f"[{self.log_date_time_string()}] {format % args}")

def start_server():
    """Start the HTTP server"""
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, PortfolioHandler)
    
    print("=" * 70)
    print("🚀 Yasharth Rai - Portfolio Server")
    print("=" * 70)
    print(f"✅ Server running at: http://{HOST}:{PORT}/")
    print(f"📱 Open your browser and visit: http://localhost:{PORT}")
    print("\n💡 Press CTRL+C to stop the server")
    print("=" * 70 + "\n")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n✋ Server stopped.")
        httpd.server_close()

if __name__ == "__main__":
    start_server()
