import math
def minimax(depth, node_index, is_max, scores, height):
    if depth == height:
        return scores[node_index]  
    if is_max:
        return max(minimax(depth + 1, node_index * 2, False, scores, height),
                   minimax(depth + 1, node_index * 2 + 1, False, scores, height))
    else:
        return min(minimax(depth + 1, node_index * 2, True, scores, height),
                   minimax(depth + 1, node_index * 2 + 1, True, scores, height))
scores = [3, 5, 2, 9, 12, 5, 23, 23]
tree_height = int(math.log2(len(scores)))
optimal_value = minimax(0, 0, True, scores, tree_height)
print("Minimax Optimal Value:", optimal_value)