import zmq


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:1337")

    while True:
        #  Wait for next request from client
        message = socket.recv().decode()

        try:
            value = float(message) * 1.609344
            value = str(value).encode()
            socket.send(value)

        except ValueError:
            socket.send(b"Attempted to send a non-float/integer input.")


if __name__ == "__main__":
    main()
