from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080 #You can choose any available port; by default, it is 8000


class MyServer(BaseHTTPRequestHandler):  
    def do_GET(self): 
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>gif</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Ini contoh gambar.</p>", "utf-8"))
        self.wfile.write(bytes("<h2>ini jihyo wkwakawk</h2>", "utf-8"))
        self.wfile.write(bytes("<img src='https://c.tenor.com/4hTZIm6CTNMAAAAd/tenor.gif'>", "utf-8"))
        self.wfile.write(bytes("<h2>dani melolong o-o</h2>", "utf-8"))
        self.wfile.write(bytes("<img src='https://media1.tenor.com/m/0T0CxRrWangAAAAd/danielle-new-jeans.gif'>", "utf-8"))
        self.wfile.write(bytes("<h2>hanni cihuy</h2>", "utf-8"))
        self.wfile.write(bytes("<img src='https://media1.tenor.com/m/okGqfXca_eAAAAAd/hanni-newjeans.gif'>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))  #Server starts
try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass
webServer.server_close()  #Executes when you hit a keyboard interrupt, closing the server