import http.server
import socketserver
import webbrowser
import threading

PORT = 8000

# Funktion, um den Browser zu öffnen
def open_browser():
    webbrowser.open(f'http://localhost:{PORT}')

# Browser in einem separaten Thread starten
threading.Timer(1.0, open_browser).start()

# HTTP Server starten
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server läuft auf http://localhost:{PORT}")
    httpd.serve_forever()
