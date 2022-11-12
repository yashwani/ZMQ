import zmq
import time
import sys
import json


if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.ROUTER)
socket.bind("tcp://*:%s" % port)

while True:
    #  Wait for next request from client
    socket.recv()
    msg = socket.recv()
    json_msg = json.loads(msg)
    print("Received request: ", json_msg)
    time.sleep(1)
