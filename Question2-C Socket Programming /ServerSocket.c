#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>

#define PORT 8443

int main() {
    // Create a socket
    int server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket < 0) {
        perror("Socket creation error");
        exit(EXIT_FAILURE);
    }

    // Bind the socket to an IP address and port
    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);

    if (bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Binding error");
        close(server_socket);
        exit(EXIT_FAILURE);
    }

    // Listen for incoming connections
    if (listen(server_socket, 5) < 0) {
        perror("Listening error");
        close(server_socket);
        exit(EXIT_FAILURE);
    }

    printf("Server is listening on port %d...\n", PORT);

    while (1) {
        // Accept a client connection
        struct sockaddr_in client_addr;
        int client_socket;
        socklen_t client_addr_len = sizeof(client_addr);
        client_socket = accept(server_socket, (struct sockaddr *)&client_addr, &client_addr_len);
        if (client_socket < 0) {
            perror("Accepting error");
            close(server_socket);
            exit(EXIT_FAILURE);
        }

        // Generate a random number ranging from 100 to 999
        int random_number = rand() % 900 + 100;
        printf("Generated random number: %d\n", random_number);

        // Send the random number to the client
        send(client_socket, &random_number, sizeof(random_number), 0);

        // Close the connection
        close(client_socket);
    }

    return 0;
}
