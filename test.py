#__author:"HYK"
#DATE:2018/4/22

import socketserver

obj = socketserver.ThreadingTCPServer()

obj.serve_forever()