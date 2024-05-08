def calculate_parity(value):
    count = 0
    for bit in value:
        if bit == '1':
            count += 1
    # For each bit stream, calculate parity
    return count % 2

def get_valid_bitstream(prompt):
    while True:
        bitstream = input(prompt)
        if len(bitstream) <= 7:
            return bitstream
        else:
            print("Invalid input. Bitstream can have a maximum of 7 bits. Please enter again.")

# Input bitstreams (up to 7 bits) from sender for 2D parity
input_sender_2d = []
num_rows = int(input('Sender: Enter the number of rows: '))
num_cols = int(input('Sender: Enter the number of columns: '))
for row in range(num_rows):
    row_data = get_valid_bitstream(f'Sender: Enter row {row + 1} ({num_cols} bits): ')
    input_sender_2d.append(row_data)

# Calculate row and column parity bits for 2D parity
row_parity_2d = [calculate_parity(row) for row in input_sender_2d]
column_parity_2d = [calculate_parity(''.join([input_sender_2d[row][col] for row in range(num_rows)])) for col in range(num_cols)]

# Generate parity for the newly created row of parity
new_row_parity = calculate_parity(''.join([str(row_parity_2d[row]) for row in range(num_rows)]))

# Displaying the input matrix for 2D parity
print("\nInput Matrix for 2D Parity:")
for row in range(num_rows):
    print(f"Row {row + 1}: {input_sender_2d[row]}")

# Displaying the output matrix with row and column parity bits for 2D parity
output_matrix_2d = [input_sender_2d[row] + str(row_parity_2d[row]) for row in range(num_rows)]
output_matrix_2d.append(''.join([str(column_parity_2d[col]) for col in range(num_cols)] + [str(new_row_parity)]))

print("\nOutput Matrix for 2D Parity:")
for row in range(num_rows + 1):
    print(f"Row {row + 1}: {output_matrix_2d[row]}")

# Input bitstreams (up to 7 bits) from receiver for 2D parity
input_receiver_2d = []
for row in range(num_rows):
    row_data = get_valid_bitstream(f'Receiver: Enter received row : ')
    input_receiver_2d.append(row_data)

# Check if there is an error or not
if input_receiver_2d == output_matrix_2d[:-1]:
    print("\nThere is no error in your received data.")
else:
    print("\nThere is an error in your received data.")
