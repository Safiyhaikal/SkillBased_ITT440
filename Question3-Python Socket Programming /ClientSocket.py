import socket

def main():
    host = '192.168.188.130'  
    port = 4040      

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        pressure_bar = float(input("Enter pressure value in bar: "))
        client_socket.send(str(pressure_bar).encode('utf-8'))
        atmosphere_standard = client_socket.recv(1024).decode('utf-8')
        print("Pressure in atmosphere-standard: {} atm".format(atmosphere_standard))
    except ValueError:
        print("Invalid input. Please provide a valid pressure value in bar.")
    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
