import math

nodes_visited_minimax = 0
nodes_visited_alphabeta = 0

def minimax_count(depth, node_index, is_max, scores, height):
    global nodes_visited_minimax
    nodes_visited_minimax += 1
    
    if depth == height:
        return scores[node_index]
    
    if is_max:
        return max(minimax_count(depth + 1, node_index * 2, False, scores, height),
                   minimax_count(depth + 1, node_index * 2 + 1, False, scores, height))
    else:
        return min(minimax_count(depth + 1, node_index * 2, True, scores, height),
                   minimax_count(depth + 1, node_index * 2 + 1, True, scores, height))

def alphabeta_count(depth, node_index, is_max, scores, alpha, beta, height):
    global nodes_visited_alphabeta
    nodes_visited_alphabeta += 1
    
    if depth == height:
        return scores[node_index]
    
    if is_max:
        best = -math.inf
        for i in range(2):
            val = alphabeta_count(depth + 1, node_index * 2 + i, False, scores, alpha, beta, height)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alphabeta_count(depth + 1, node_index * 2 + i, True, scores, alpha, beta, height)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

scores = [3, 5, 2, 9, 12, 5, 23, 23]
tree_height = int(math.log2(len(scores)))

res_m = minimax_count(0, 0, True, scores, tree_height)
res_ab = alphabeta_count(0, 0, True, scores, -math.inf, math.inf, tree_height)

print("Minimax Result:", res_m, "| Visited Nodes:", nodes_visited_minimax)
print("Alpha-Beta Result:", res_ab, "| Visited Nodes:", nodes_visited_alphabeta)