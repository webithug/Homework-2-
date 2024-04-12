liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

def get_output_amount(input_amount, input_reserves, output_reserves, fee=0.003):
    # Calculate the amount of tokens received after the swap
    # Deducting the fee from the input amount
    input_amount_after_fee = input_amount * (1 - fee)
    # Using the constant product formula to find the output amount
    output_amount = (input_amount_after_fee * output_reserves) / (input_reserves + input_amount_after_fee)
    return output_amount

def dfs(current_token, current_amount, path, visited, liquidity, goal_amount=20):
    # If we have looped back to tokenB and have sufficient amount, print the result
    if current_token == "tokenB" and len(path) > 1:
        if current_amount >= goal_amount:
            return path, current_amount
        else:
            return None
    
    # Explore neighbors
    for (token1, token2), (res1, res2) in liquidity.items():
        if token1 == current_token and (token2 not in visited or token2 == "tokenB"):
            output_amount = get_output_amount(current_amount, res1, res2)
            result = dfs(token2, output_amount, path + [token2], visited + [token2], liquidity)
            if result:
                return result
        elif token2 == current_token and (token1 not in visited or token1 == "tokenB"):
            output_amount = get_output_amount(current_amount, res2, res1)
            result = dfs(token1, output_amount, path + [token1], visited + [token1], liquidity)
            if result:
                return result
    return None


# Start DFS from tokenB with an initial amount of 5 units
result = dfs("tokenB", 5, ["tokenB"], ["tokenB"], liquidity)
if result:
    path, final_amount = result
    print(f"path: {'->'.join(path)}, tokenB balance={final_amount}")
else:
    print("No profitable path found")
