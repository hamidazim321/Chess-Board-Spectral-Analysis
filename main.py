import numpy as np
import matplotlib.pyplot as plt

# Adjacency matrix of the graph
A = np.zeros((64, 64))

# the 8 possible "L" moves for a knight in chess
knight_moves = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

# Fill the adjacency matrix based on knight moves
for current_row in range(8):
    for current_col in range(8):
        for row_move, col_move in knight_moves:
            new_row, new_col = current_row + row_move, current_col + col_move
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                A[current_row * 8 + current_col][new_row * 8 + new_col] = 1

eigenvalues, eigenvectors = np.linalg.eigh(A)
principal_vector = eigenvectors[:, -1]
heatmap = principal_vector.reshape((8, 8))

# Plot the results
plt.figure(figsize=(8, 6))
plt.imshow(np.abs(heatmap), cmap='hot', interpolation='nearest', origin='lower')
plt.colorbar(label='Influence Score')
plt.title("The Knight's Power Map (Principal Eigenvector)")
plt.show()