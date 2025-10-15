def winning_strategy(cards):
    """
    Returns:
      diff: int, score difference (playerA - playerB) when both play optimally
      moves: list of tuples (player, choice, value, i, j) representing an optimal play sequence
             player: 'A' or 'B'
             choice: 'L' (left) or 'R' (right)
             value: card value taken
             i, j: indices at time of taking
    """
    n = len(cards)
    if n == 0:
        return 0, []

    # dp[i][j] = max score difference current player can achieve on cards[i..j]
    dp = [[0]*n for _ in range(n)]
    # choice[i][j] = 'L' or 'R' — which move gives the dp value (for reconstruction)
    choice = [['']*n for _ in range(n)]

    for i in range(n):
        dp[i][i] = cards[i]
        choice[i][i] = 'L'  # only choice

    # length from 2 to n
    for length in range(2, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            # take left
            left = cards[i] - dp[i+1][j]
            # take right
            right = cards[j] - dp[i][j-1]
            if left >= right:
                dp[i][j] = left
                choice[i][j] = 'L'
            else:
                dp[i][j] = right
                choice[i][j] = 'R'

    # reconstruct moves
    moves = []
    i, j = 0, n-1
    player = 'A'
    while i <= j:
        ch = choice[i][j]
        if ch == 'L':
            val = cards[i]
            moves.append((player, 'L', val, i, j))
            i += 1
        else:
            val = cards[j]
            moves.append((player, 'R', val, i, j))
            j -= 1
        player = 'B' if player == 'A' else 'A'

    return dp[0][n-1], moves


# Example usage:
if _name_ == "_main_":
    examples = [
        [3, 9, 1, 2],
        [5, 3, 7, 10],
        [8, 15, 3, 7],
        [20, 30, 2, 2, 2, 10]
    ]

    for cards in examples:
        diff, moves = winning_strategy(cards)
        n = len(cards)
        print("Cards:", cards)
        print("Score difference (A - B):", diff)
        if diff > 0:
            print("Starting player (A) wins by", diff)
        elif diff < 0:
            print("Starting player (A) loses (B wins by)", -diff)
        else:
            print("Tie")

        # pretty-print moves with running totals
        a_score = b_score = 0
        cur = 'A'
        for step, (player, ch, val, i, j) in enumerate(moves, 1):
            if player == 'A':
                a_score += val
            else:
                b_score += val
            print(f" {step}. Player {player} takes {ch}={val} (remaining indices [{i},{j}]) -> totals A:{a_score} B:{b_score}")
        print("-"*40)
