import math

minimax_leaf_count = 0
alphabeta_leaf_count = 0

def minimax(cur_depth, node_index, max_turn, scores, target_depth):
    global minimax_leaf_count
    
    if cur_depth == target_depth:
        minimax_leaf_count += 1
        return scores[node_index]
    
    if max_turn:
        return max(
            minimax(cur_depth + 1, node_index * 2, False, scores, target_depth),
            minimax(cur_depth + 1, node_index * 2 + 1, False, scores, target_depth)
        )
    else:
        return min(
            minimax(cur_depth + 1, node_index * 2, True, scores, target_depth),
            minimax(cur_depth + 1, node_index * 2 + 1, True, scores, target_depth)
        )

def alphabeta(cur_depth, node_index, max_turn, scores, target_depth, alpha, beta):
    global alphabeta_leaf_count
    
    if cur_depth == target_depth:
        alphabeta_leaf_count += 1
        return scores[node_index]
    
    if max_turn:
        value = float('-inf')
        for i in range(2):
            child_val = alphabeta(cur_depth + 1, node_index * 2 + i, False, scores, target_depth, alpha, beta)
            value = max(value, child_val)
            alpha = max(alpha, value)
            if alpha >= beta:
                break  
        return value
    else:
        value = float('inf')
        for i in range(2):
            child_val = alphabeta(cur_depth + 1, node_index * 2 + i, True, scores, target_depth, alpha, beta)
            value = min(value, child_val)
            beta = min(beta, value)
            if alpha >= beta:
                break  
        return value

def run_experiment(scores_list, exp_title):
    global minimax_leaf_count, alphabeta_leaf_count
    
    minimax_leaf_count = 0
    alphabeta_leaf_count = 0
    
    tree_depth = math.ceil(math.log2(len(scores_list)))
    padded_scores = scores_list + [0] * ((2 ** tree_depth) - len(scores_list))
    
    mm_val = minimax(0, 0, True, padded_scores, tree_depth)
    
    ab_val = alphabeta(0, 0, True, padded_scores, tree_depth, float('-inf'), float('inf'))
    
    print(f"=== {exp_title} ===")
    print(f"Scores Array: {scores_list}")
    print(f"Minimax Root Value: {mm_val} | Leaves Evaluated: {minimax_leaf_count}")
    print(f"Alpha-Beta Root Value: {ab_val} | Leaves Evaluated: {alphabeta_leaf_count}")
    print(f"Pruned Leaves Saved: {minimax_leaf_count - alphabeta_leaf_count}\n")

if __name__ == "__main__":

    original_scores = [3, 5, 2, 9, 0, 7, 1, 8]
    run_experiment(original_scores, "Task 1 & 2: Standard Game Tree")

    reordered_scores = [9, 8, 5, 3, 7, 2, 1, 0]
    run_experiment(reordered_scores, "Task 3: Reordered Game Tree (Optimal Branch Ordering)")