import socket

# Create a socket to send fatigue feedback to workers and supervisors
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 5000))

# Send fatigue level updates to workers and supervisors
while True:
    fatigue_level = get_fatigue_level()
    sock.send(fatigue_level.encode())
