def max_score(cards, i, j, memo):
    if i > j:
        return 0
    if (i, j) in memo:
        return memo[(i, j)]

    # Choose the first card
    pick_first = cards[i] + min(
        max_score(cards, i+2, j, memo),   # Opponent picks i+1
        max_score(cards, i+1, j-1, memo)  # Opponent picks j
    )
    # Choose the last card
    pick_last = cards[j] + min(
        max_score(cards, i+1, j-1, memo),  # Opponent picks i
        max_score(cards, i, j-2, memo)     # Opponent picks j-1
    )

    memo[(i, j)] = max(pick_first, pick_last)
    return memo[(i, j)]

# Example usage
cards = [3, 9, 1, 2]
memo = {}
max_points = max_score(cards, 0, len(cards)-1, memo)

print("Card sequence:", cards)
print("Maximum points player 1 can achieve:", max_points)
