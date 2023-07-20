Client

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>

#define PORT 8443

int main() {
    // Create a socket
    int client_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (client_socket < 0) {
        perror("Socket creation error");
        exit(EXIT_FAILURE);
    }

    // Server information
    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    inet_pton(AF_INET, "192.168.188.130", &server_addr.sin_addr);

    // Connect to the server
    if (connect(client_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Connection error");
        close(client_socket);
        exit(EXIT_FAILURE);
    }

    // Receive the random number from the server
    int random_number;
    recv(client_socket, &random_number, sizeof(random_number), 0);

    // Display the random number
    printf("Received random number from server: %d\n", random_number);

    // Close the connection
    close(client_socket);

    return 0;
}
