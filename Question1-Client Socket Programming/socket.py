import socket

def connect_to_server():
    # Server information
    server_host = "izani.synology.me"
    server_port = 8443

    # Put your UiTM Student ID 
    student_id = "2021887274"

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((server_host, server_port))
        print("Connected to the server!")

        # Send the Student ID to the server
        client_socket.send(student_id.encode())

        # Receive the server response
        response = client_socket.recv(1024).decode()
        print("Server response:", response)

        # Close the connection
        client_socket.close()

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    connect_to_server()
