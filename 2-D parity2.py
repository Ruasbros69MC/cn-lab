# Input: Number of rows and columns
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Input: Binary matrix
matrix = []
print("Enter the binary matrix (0s and 1s):")
for _ in range(rows):
    row_data = list(map(int, input().split()[:cols]))  # Ensure only 'cols' elements are considered
    matrix.append(row_data)

# Ensure each row has the correct number of columns
for row in matrix:
    if len(row) != cols:
        print("Error: Please enter exactly {} elements for each row.".format(cols))
        exit()

# Calculate row parity
row_parity = [sum(matrix[i]) % 2 for i in range(rows)]
for i in range(rows):
    matrix[i].append(row_parity[i])

# Calculate column parity
col_parity = [sum(matrix[i][j] for i in range(rows)) % 2 for j in range(cols)]  # Corrected indexing
matrix.append(col_parity)

# Calculate parity bit for both row and column parity
matrix[-1].append(sum(col_parity) % 2)

# Print the matrix with parity bits
print("Matrix with Row and Column Parities:")
for row in matrix:
    print(' '.join(map(str, row)))

# Verify parity with user input
verify_matrix = []
print("Enter a new binary matrix for verification:")
for _ in range(rows):
    row_data = list(map(int, input().split()[:cols]))
    verify_matrix.append(row_data)

# Ensure each row has the correct number of columns
for row in verify_matrix:
    if len(row) != cols:
        print("Error: Please enter exactly {} elements for each row.".format(cols))
        exit()

# Verify row parity
verify_row_parity = [sum(verify_matrix[i]) % 2 for i in range(rows)]
if verify_row_parity == row_parity:
    print("Row Parities match!")
else:
    print("Row Parities do not match!")

# Verify column parity
verify_col_parity = [sum(verify_matrix[i][j] for i in range(rows)) % 2 for j in range(cols)]
if verify_col_parity == col_parity:
    print("Column Parities match!")
else:
    print("Column Parities do not match!")
