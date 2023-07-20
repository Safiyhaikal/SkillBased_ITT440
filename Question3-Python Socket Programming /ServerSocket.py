import socket

def bar_to_atmosphere(pressure_bar):
    return pressure_bar * 0.986923

def handle_client(client_socket):
    data = client_socket.recv(1024).decode('utf-8')
    try:
        pressure_bar = float(data)
        atmosphere_standard = bar_to_atmosphere(pressure_bar)
        client_socket.send(str(atmosphere_standard).encode('utf-8'))
    except ValueError:
        client_socket.send("Invalid input. Please provide a valid pressure value in bar.".encode('utf-8'))
    client_socket.close()

def main():
    host = '0.0.0.0'  
    port = 4040  

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server is listening on {}:{}".format(host, port))

    while True:
        client_socket, addr = server_socket.accept()
        print("Connection from:", addr)
        handle_client(client_socket)

if __name__ == "__main__":
    main()
