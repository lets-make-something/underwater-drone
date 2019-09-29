#!/usr/bin/python3
import struct
import time
from socket import socket, AF_INET, SOCK_DGRAM

host = '127.0.0.1'
port = 5000

EVENT_FORMAT = "LhBB";
EVENT_SIZE = struct.calcsize(EVENT_FORMAT)

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((host, port))
print("recv start") 

while True:
  try:
    msg, address = sock.recvfrom(EVENT_SIZE)
    (ds3_time, ds3_val, ds3_type, ds3_num) = struct.unpack(EVENT_FORMAT, msg)
    print(f"{ds3_time} , {ds3_val} , {ds3_type} , {ds3_num}")
    if (ds3_type == 2 and (ds3_num >= 0 and ds3_num <= 3)):
      print( "{0}, {1}, {2}, {3}".format( ds3_time, ds3_val, ds3_type, ds3_num ) )
  except:
    import traceback
    traceback.print_exc() 
    time.sleep(5)

sock.close() 

