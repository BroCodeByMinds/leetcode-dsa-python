class Solution:
    """
    Approach:
    - We want to maximize profit with one transaction (buy once, sell once).
    - Idea: For each day, check the profit if we sell on that day.
    - Maintain:
        - min_price: The lowest price encountered so far (best day to buy).
        - max_profit: The best profit achievable so far.
    - For each price:
        - Calculate profit = price - min_price
        - Update max_profit if profit is higher
        - Update min_price if current price is lower

    Time Complexity: O(N)
        - We scan the array once.
    Space Complexity: O(1)
        - Only two variables (min_price, max_profit) are used.
    """

    # @param A : list of integers
    # @return an integer
    def maxProfit(self, A):
        if not A or len(A) < 2:
            return 0

        min_price = A[0]
        max_profit = 0

        for price in A[1:]:
            profit = price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)

        return max_profit


# Example usage
print(Solution().maxProfit([1, 2]))        # Output: 1
print(Solution().maxProfit([1, 4, 5, 2, 4]))  # Output: 4