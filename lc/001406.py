# 1406. Stone Game III
#
# Alice and Bob continue their games with piles of stones. There are
# several stones arranged in a row, and each stone has an associated
# value which is an integer given in the array `stoneValue`.
#
# Alice and Bob take turns, with Alice starting first. On each player's
# turn, that player can take 1, 2, or 3 stones from the first remaining
# stones in the row.
#
# The score of each player is the sum of the values of the stones
# taken. The score of each player is 0 initially.
#
# The objective of the game is to end with the highest score, and the
# winner is the player with the highest score and there could be a
# tie. The game continues until all the stones have been taken.
#
# Assume Alice and Bob play optimally.
#
# Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if
# they will end the game with the same score.

# I'm assuming all stones are visible to both Alice and Bob at the
# start, i.e., this is a game of perfect information.


# Example: stones = [1, 2, 3, 7]
#
# Build solution from end.
# Possibilities: A[7], B[7], A[3,7], B[3,7], A[2,3,7], B[2,3,7]
#
# [2,3,7] <- A[1] means B[2,3,7] <- A[1]: {A: 1, B: 12}; so A[2,3,7] is not possible.
#
# [3,7] <--- [2] <- A[1]: {A: 11, B: 2}
#         `- A[1,2]: {A: 3, B: 10}
#
# [7] <--- [3] <--- [2] <--- A[1]: {A: 4, B: 9}
#       |        `- A[1,2]: {A: 10, B: 3}
#       `- [2,3] <--- A[1]: {A: 8, B: 5}
#       `- A[1,2,3]: {A: 6, B: 7}
#
# Game tree:
# A[1,2,3] ---> B[7]: {A: 6, B: 7}  <-- Best game for Alice
# A[1,2] ---> B[3] ---> A[7]: {A: 10, B: 3}
#        `--> B[3,7]: {A: 3, B: 10}
# A[1] ---> B[2] ---> A[3] ---> B[7]: {A: 4, B: 9}
#      |         `--> A[3,7]: {A: 11, B: 2}
#      `--> B[2,3] ---> A[7]: {A: 8, B: 5}
#      `--> B[2,3,7]: {A: 1, B: 12}
#
# Ok, so we have a tree structure over partitions of the stone sequence
# into subsequences of lengths 1-3.  But I'm not sure how to build the
# optimal solution from the bottom up, in part because it could be
# either player.  (Is tracking the player required?  Or can it be
# inferred?)  Since I know I need to do minimax search, it seems like
# maybe aggregating both a minimum and a maximum at each ply of the game
# tree would allow deducing the optimal play without tracking the player
# along the way.
#
# Try tracking both a min & max (but alternating)
# end: min: [7],     max: [2,3,7]
#  -1: max: [2,3,7], min: [1]
#  -2: no more moves, Alice picks max from step -1
#
# Try same strategy with another example: stones = [1, 2, 3, -9]
# end: min: [-9],    max: [2,3,-9]
#  -1: max: [1,2,3], min: [1]
#  -2: no more moves, Alice picks max from step -1
#
# Try same strategy with example where end max is 2 stones:
# stones = [3, 8, 0, -3, -10, 6, -8]  # [random.randint(-10, 10) for _ in range(7)]
# end: min: [-10,6,-8], max: [6,-8]
#  -1: max: [8,0,-3],   min: [-3,-10], [0,-3,-10]
#  -2: min: [3],        max: [3,8,0], [3,8]
#  -3: no more moves, Alice picks max from step -2: {A: 9, B: -13}
# This doesn't work as, for example, A[3,8,0], B[-3,-10,6], A[-8]: {A: 3, B: -7}.
#
# >>> brute_force_game_tree_search([3, 8, 0, -3, -10, 6, -8])
# [([3, 8], 4, -8), ([0], -8, -7), ([-3, -10, 6], -7, -8), ([-8], -8, 0)]
#
# Example where end min is 2 stones:
# stones = [-5, 5, 4, 0, 4, -8, -6]
#
# >>> brute_force_game_tree_search([-5, 5, 4, 0, 4, -8, -6])
# [([-5, 5, 4], -4, -2), ([0, 4], -2, -8), ([-8], -8, -6), ([-6], -6, 0)]
#
# Example where the best strategy is 2 & 2: stones = [1, 2, -1, 3]
#
# >>> brute_force_game_tree_search([1, 2, -1, 3])
# [([1, 2], 3, 2), ([-1, 3], 2, 0)]

# I don't know.  Just write the brute force game tree search.
def pick_optimal_stones__bfgts(stones: list[int],
) -> list[tuple[list[int], int, int]]:
    """
    Find the optimal way of picking stones for both players.  Return
    a list containing the optimal move and its scores at each step.

    Brute force game tree search (BFGTS) solution.
    """
    # This case should only be needed for empty games
    if len(stones) == 0:
        return [([], 0, 0)]
    moves = []
    for n_stones in (3, 2, 1):
        # Base case, last move, take all remaining stones
        if len(stones) == n_stones:
            moves.append((stones, sum(stones), 0, []))
        elif len(stones) > n_stones:
            best_of_rest = pick_optimal_stones__bfgts(stones[n_stones:])
            # Reverse scores
            (_, p2_score, p1_score) = best_of_rest[0]
            stones_taken = stones[:n_stones]
            p1_score += sum(stones_taken)
            moves.append((stones_taken, p1_score, p2_score, best_of_rest))
        # Otherwise, skip  as there aren't enough stones for that move
    # Pick the best out of the moves that have been explored
    best = max(moves, key=lambda t: (
                     # Max over:
        t[1] - t[2], # Score difference (higher is presumably better)
        t[1],        # Absolute score (if tied, go for impressiveness)
        -len(t[3]),  # Shortest game (if tied, prefer shorter games)
    ))
    (move, score1, score2, states) = best
    return [(move, score1, score2)] + states

# [Hours later.]  Earlier I had trouble thinking clearly, but, when
# walking home from the co-op, I think I figured it out.
#
# * The game is symmetric.  That's why we don't need to keep track of
#   the player.  Any player can start from any position and the optimal
#   will be the same.
# * The optimal move is wrt a given position.  Then, when considering
#   moves, one has to look across later positions.  That's what I was
#   missing.
# * The aggregation is just a max, as illustrated in the brute force
#   version above.  It's not alternating minimum and maximum nor
#   anything else.  The symmetry and switching players accomplishes the
#   minimax search automatically.
# * While I haven't convinced myself yet, I believe the bottom-up
#   dynamic programming approach finds the optimum due to an inductive
#   argument from the end to the beginning.
#
# Work out my new approach on the example above:
# stones = [3, 8, 0, -3, -10, 6, -8]
#
# index: dict[move, tuple[score, opponent score]], best move #stones: score diff
# -1: {[-8]: (-8, 0)}, 1: -8
# -2: {[6]: (6, -8), [6, -8]: (-2, 0)}, 1: 14
# -3: {[-10]: (-18, 6), [-10, 6]: (-4, -8), [-10, 6, -8]: (-12, 0)}, 2: 4
# -4: {[-3]: (-11, -4), [-3, -10]: (-21, 6), [-3, -10, 6]: (-7, -8)}, 3: 1
# -5: {[0]: (-8, -7), [0, -3]: (-11, -4), [0, -3, -10]: (-21, 6)}, 1: 1
# -6: {[8]: (1, -8), [8, 0]: (0, -7), [8, 0, -3]: (-3, -4)}, 1: 9
# -7: {[3]: (5, 1), [3, 8]: (4, -8), [3, 8, 0]: (3, -7)}, 2: 12
# ---> A[3, 8], B[0], A[-3, -10, 6], B[-8]: {A: 4, B: -8}
#
# Alright.  That checks out.  Let's write it!

def pick_optimal_stones__dp(stones: list[int], max_n_stones=3,
) -> list[tuple[list[int], int, int]]:
    """
    Find the optimal way of picking stones for both players.  Return
    a list containing the optimal move and its scores at each step.

    Dynamic programming (DP) solution.
    """
    # Empty game
    if len(stones) == 0:
        return [([], 0, 0)]
    # Allocate solution
    best_moves_scores = [None] * len(stones)
    # Build solution from end to beginning
    for move_idx in range(len(stones) - 1, -1, -1):
        moves = []
        for n_stones in range(1, max_n_stones + 1):
            end_idx = move_idx + n_stones
            # Skip moves that are too large (this and all following)
            if end_idx > len(stones):
                break
            # Get the scores of the optimal tail
            if end_idx < len(stones):
                (_, score1, score2) = best_moves_scores[end_idx]
            else:
                assert end_idx == len(stones)
                score1 = 0
                score2 = 0
            # Record this move.  Switch players to get the correct score.
            take_stones = stones[move_idx:end_idx]
            move = (take_stones, sum(take_stones) + score2, score1)
            moves.append(move)
        # Find the best move and its scores
        best = max(moves, key=lambda t: (
                         # Max over:
            t[1] - t[2], # Score difference (accomplishes minimax search)
            t[1],        # Absolute score (if tied, go for impressiveness)
        ))
        best_moves_scores[move_idx] = best
    return best_moves_scores


# Interface to LeetCode
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        best_moves = pick_optimal_stones__dp(stoneValue)
        (_, score1, score2) = best_moves[0]
        if score1 > score2:
            return 'Alice'
        elif score1 < score2:
            return 'Bob'
        else:
            return 'Tie'
