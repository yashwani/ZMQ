import zmq
import sys

if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 = sys.argv[2]
    int(port1)

context = zmq.Context()
print("Connecting to server...")
socket = context.socket(zmq.DEALER)
socket.connect("tcp://localhost:%s" % port)
if len(sys.argv) > 2:
    socket.connect("tcp://localhost:%s" % port1)

for request in range (1,10):
    print("Sending request ", request, "...")
    socket.send_string("Hello")
