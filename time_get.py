import time
import socket

def check(host,port,timeout=2):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #presumably 
    sock.settimeout(timeout)
    try:
       sock.connect((host,port))
    except:
       return False
    else:
       sock.close()
       return True



# print(check('google.com',1234,timeout=1))
# print(check('google.com',443,timeout=1))
# print("\n\n\n")
# print(check('85.114.138.223',8888,timeout=1))
# print("\n\n\n")
# print(check('50.7.46.44',443,timeout=1))




def timed_check(host,port,timeout=2):
    t0 = time.time()
    connect1 =  check(host,port,timeout)
    # connect1 = True
    if connect1:
    #    return time.time()-t0 # a bit inexact but close enough
        return {
            "connect": 1,
            "time_get": time.time()-t0,
            "time": time.time()
        }
    return {
        "connect": 0,
        "time_get": -1,
        "time": time.time()
    }
