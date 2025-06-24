import socketserver, os

TFTP_ROOT = "./tftp_config"
os.makedirs(TFTP_ROOT, exist_ok=True)

class TFTPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data, sock = self.request
        if data[1] == 1:  # RRQ not supported
            print("Read request not supported.")
        elif data[1] == 2:  # WRQ (Write Request)
            filename = data[2:].split(b'\x00')[0].decode()
            print(f"Receiving file: {filename}")

            # Send ACK for WRQ (ACK with block number 0)
            ack = b'\x00\x04\x00\x00'
            sock.sendto(ack, self.client_address)

            with open(os.path.join(TFTP_ROOT, filename), 'wb') as f:
                while True:
                    block = sock.recv(516)
                    f.write(block[4:])  # Write only the data part
                    ack = b'\x00\x04' + block[2:4]  # ACK with received block number
                    sock.sendto(ack, self.client_address)

                    if len(block) < 516:  # Last block is less than 512 bytes of data
                        break

            print(f"File {filename} saved.")

if __name__ == "__main__":
    print("Starting TFTP server on port 69...")
    with socketserver.UDPServer(('', 69), TFTPHandler) as server:
        server.serve_forever()
