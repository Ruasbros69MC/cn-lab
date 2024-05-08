import sys

def generate_routing_tables(adjacency_matrix):
    num_nodes = len(adjacency_matrix)

    # Initialize routing tables
    routing_tables = []
    for node in range(num_nodes):
        routing_table = []
        for destination in range(num_nodes):
            cost, outgoing_line = sys.maxsize, -1

            if node == destination:
                cost = 0
            elif adjacency_matrix[node][destination] != 0:
                cost = adjacency_matrix[node][destination]
                outgoing_line = destination

            routing_table.append((cost, outgoing_line))

        routing_tables.append(routing_table)

    return routing_tables

def print_routing_tables(routing_tables):
    num_nodes = len(routing_tables)

    for node in range(num_nodes):
        print(f"\nRouting Table for Node {node + 1}:\n{'Destination':<15}{'Cost':<10}{'Outgoing Line':<15}")

        for destination in range(num_nodes):
            cost, outgoing_line = routing_tables[node][destination]
            print(f"{destination + 1:<15}{cost:<10}{outgoing_line + 1:<15}")

if __name__ == "__main__":
    # Get user input for the number of nodes in the network
    num_nodes = int(input("Enter the number of nodes in the network: "))

    # Initialize an empty adjacency matrix
    adjacency_matrix = []

    # Get user input for the adjacency matrix
    print("Enter the adjacency matrix:")
    for i in range(num_nodes):
        row = list(map(int, input().split()))
        adjacency_matrix.append(row)

    # Generate and print routing tables
    routing_tables = generate_routing_tables(adjacency_matrix)
    print_routing_tables(routing_tables)
