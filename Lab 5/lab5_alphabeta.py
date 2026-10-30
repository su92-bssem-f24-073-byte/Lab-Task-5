import math

def alphabeta(depth, node_index, is_max, scores, alpha, beta, height):
    if depth == height:
        return scores[node_index]
    
    if is_max:
        best = -math.inf
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, False, scores, alpha, beta, height)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, True, scores, alpha, beta, height)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

scores = [3, 5, 2, 9, 12, 5, 23, 23]
tree_height = int(math.log2(len(scores)))

optimal_value = alphabeta(0, 0, True, scores, -math.inf, math.inf, tree_height)
print("Alpha-Beta Pruning Optimal Value:", optimal_value)