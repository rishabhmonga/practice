"""
public class Solution {
    Map<Integer,Integer> amountDict = new HashMap<Integer,Integer>();
    public int coinChange(int[] coins, int amount) {
        if(amount==0)
            return 0;
        if(amountDict.containsKey(amount))
            return amountDict.get(amount);
        int n = amount+1;
        for(int coin : coins) {
            int curr = 0;
            if (amount >= coin) {
                int next = coinChange(coins, amount-coin);
                if(next >= 0)
                    curr = 1+next;
            }
            if(curr > 0)
                n = Math.min(n,curr);
        }
        int finalCount = (n==amount+1) ? -1 : n;
        amountDict.put(amount,finalCount);
        return finalCount;
    }
}
"""
amountDict = {}
def coin_change(coins, amount):
    if amount is 0:

         return 0
    if amount in amountDict:
        return amountDict[amount]
    n = amount + 1
    for coin in coins:
        curr = 0
        if amount >= coin:
            next_coin = coin_change(coins, amount-coin)
            if next_coin >= 0:
                curr = 1 + next_coin
        if curr > 0:
            n = min(n, curr)
    final_count = -1 if n == amount + 1 else n
    amountDict[amount] = final_count
    return final_count

# memo = {}
#
# def coin_change(coins, amount):
#     if amount == 0:
#         return 0
#     if amount in memo:
#         return memo[amount]
#     min_value = float('inf')
#     for coin in coins:
#         if coin > amount:
#             continue
#         val = coin_change(coins, amount - coin)
#         min_value = min(min_value, val)
#     min_value += 1
#     memo[amount] = min_value
#     return min_value


if __name__ == '__main__':
    print coin_change([2], 1)
