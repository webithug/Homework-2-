# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution

tokenB: 5->tokenA: 5.65532
tokenA: 5.65532->tokenD: 2.45878
tokenD: 2.45878->tokenC:5.08892
tokenC: 5.08892->tokenB: 20.12988

path: tokenB->tokenA->tokenD->tokenC->tokenB, tokenB balance=20.129888944077447

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution

Slippage in Automated Market Makers (AMMs) like Uniswap V2 refers to the difference between the expected price of a trade and the actual price at which the trade is executed. This discrepancy can occur due to changes in a pool's liquidity between the time a transaction is submitted and when it is executed. In Uniswap V2, slippage is managed by allowing users to specify limits on the amounts they are willing to accept for their trades. For example, swapExactTokensForTokens checks if the actual amount of output tokens available at the last step of the swap is at least as much as the amountOutMin specified. If the available amount is less than amountOutMin, the transaction is reverted, protecting the user from excessive slippage.


## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution

