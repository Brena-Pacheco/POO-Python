from http.server import SimpleHTTPRequestHandler, HTTPServer
import webbrowser

PORT = 8000

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        super().do_GET()

# Iniciar o servidor
httpd = HTTPServer(("", PORT), MyHandler)
print(f"Servindo na porta {PORT}")

# Abrir o navegador automaticamente
webbrowser.open(f'http://localhost:{PORT}/formulario.html')

httpd.serve_forever()
