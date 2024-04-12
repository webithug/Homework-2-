# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> tokenB: 5->tokenA: 5.65532 \\
> tokenA: 5.65532->tokenD: 2.45878 \\
> tokenD: 2.45878->tokenC:5.08892 \\
> tokenC: 5.08892->tokenB: 20.12988 \\
>
> path: tokenB->tokenA->tokenD->tokenC->tokenB, tokenB balance=20.129888944077447

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Slippage in Automated Market Makers (AMMs) like Uniswap V2 refers to the difference between the expected price of a trade and the actual price at  which the trade is executed. This discrepancy can occur due to changes in a pool's liquidity between the time a transaction is submitted and when it is executed. In Uniswap V2, slippage is managed by allowing users to specify limits on the amounts they are willing to accept for their trades. For example, swapExactTokensForTokens checks if the actual amount of output tokens available at the last step of the swap is at least as much as the amountOutMin specified. If the available amount is less than amountOutMin, the transaction is reverted, protecting the user from excessive slippage.


## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> 1. This mechanism prevents anyone from owning a significant percentage of the pool with a very small initial investment. It ensures that the first liquidity provider does not end up with an excessively large share of the total liquidity tokens, which would be disproportionate to their actual contribution relative to future liquidity providers.
>
> 2. This subtracted minimum liquidity is permanently locked in the pool and is not redeemable. By locking a small amount of liquidity permanently, the pool ensures that there is always some minimal liquidity in the pool, which can be crucial for maintaining the pool's operation and preventing it from being entirely drained.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> When liquidity is added to a Uniswap V2 pool after the initial setup, the number of liquidity tokens $\( L \)$ minted for a deposit of tokens $\( \Delta x \)$ and $\( \Delta y \)$ is given by:
> $$
\[ L = \min\left(\frac{\Delta x \times T}{x}, \frac{\Delta y \times T}{y}\right) \]
> $$
where $\( T \)$ is the total supply of liquidity tokens before the deposit, $\( x \)$ and $\( y \)$ are the existing reserves of the two tokens in the pool.

> This formula ensures that the amount of liquidity tokens minted is proportional to the increase in pool size due to the added liquidity, relative to the existing reserves.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> The sandwich attack basically follows the steps as below:
> 1. Detection: The attacker monitors the mempool for large trade orders on a DEX that are likely to impact the market price of a token pair.
>
> 2. Front-Running: Upon detecting a pending transaction that will buy a token and likely increase its price, the attacker places their own buy order for the same token just before the detected transaction in the order of transactions. To ensure their transaction is processed first, the attacker pays a higher gas fee.
>
> 3. Back-Running: After the victim's transaction is executed and the price of the token has increased, the attacker immediately sells the tokens they bought in the front-running step, benefiting from the price increase caused by the victim's transaction.
>
> 4. Result: The victim's transaction buys the token at a higher price than they would have without the intervention of the attacker, and the attacker profits from the price difference.

