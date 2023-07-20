import socket
import threading
import random

# List of quotes
quotes = [
    "If you has problem with me, Text me. If you don’t have my number, you don’t know me well to has a problem with me. -TomHolland " ,
    "The purpose of our lives is to be happy. - Dalai",
    "They follow you in the sun but leave you in the dark. - Kal",
    ]

def handle_client(client_socket):
    # Send a random quote to the client
    quote = random.choice(quotes).encode('utf-8')
    client_socket.send(quote)
    client_socket.close()

def main():
    # Server settings(Put You Own Server IP Address)
    host = '192.168.188.130' 
    port = 8888

    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    print("Server listening on {}:{}".format(host, port))

    while True:
        server_socket.listen(5)
        client_socket, client_addr = server_socket.accept()

        print("Accepted connection from: {}:{}".format(client_addr[0], client_addr[1]))

        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
