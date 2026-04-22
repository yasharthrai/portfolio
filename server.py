#!/usr/bin/env python3
"""
Yasharth Rai - Portfolio
Simple HTTP server with image upload & embedding
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from pathlib import Path
import json
import os
import base64
import cgi

PORT = 8000
HOST = "localhost"

IMAGES_FILE = Path(__file__).parent / "data" / "images.json"
IMAGES_FILE.parent.mkdir(exist_ok=True)

def load_images():
    """Load stored images from JSON"""
    if IMAGES_FILE.exists():
        with open(IMAGES_FILE, "r") as f:
            return json.load(f)
    return {}

def save_images(images):
    """Save images to JSON"""
    with open(IMAGES_FILE, "w") as f:
        json.dump(images, f, indent=2)

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
        
        elif self.path == "/api/images":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            images = load_images()
            self.wfile.write(json.dumps(images).encode("utf-8"))
        
        elif self.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"status": "ok", "service": "Yasharth Rai - Portfolio"}
            self.wfile.write(json.dumps(response).encode("utf-8"))
        
        else:
            # Try to serve static files
            super().do_GET()
    
    def do_POST(self):
        """Handle POST requests for image uploads"""
        if self.path == "/api/upload":
            content_length = int(self.headers.get('Content-Length', 0))
            
            if content_length > 50 * 1024 * 1024:  # 50MB limit
                self.send_response(413)
                self.end_headers()
                self.wfile.write(b"File too large")
                return
            
            # Parse multipart form data
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={
                    'REQUEST_METHOD': 'POST',
                    'CONTENT_TYPE': self.headers['Content-Type'],
                }
            )
            
            if 'file' not in form or 'title' not in form:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Missing file or title")
                return
            
            fileitem = form['file']
            title = form['title'].value
            
            if fileitem.filename:
                # Read file and convert to base64
                file_data = fileitem.file.read()
                base64_data = base64.b64encode(file_data).decode('utf-8')
                
                # Determine MIME type
                filename = fileitem.filename.lower()
                if filename.endswith('.png'):
                    mime_type = 'image/png'
                elif filename.endswith('.gif'):
                    mime_type = 'image/gif'
                elif filename.endswith('.webp'):
                    mime_type = 'image/webp'
                else:
                    mime_type = 'image/jpeg'
                
                data_url = f"data:{mime_type};base64,{base64_data}"
                
                # Save to images.json
                images = load_images()
                images[title] = {
                    "url": data_url,
                    "filename": fileitem.filename,
                    "title": title
                }
                save_images(images)
                
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                response = {"status": "success", "title": title, "message": "Image uploaded and embedded!"}
                self.wfile.write(json.dumps(response).encode("utf-8"))
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"No file selected")
    
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
