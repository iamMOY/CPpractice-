def product_except_self(nums):
    n = len(nums)
    # Initialize two arrays to store products to the left and right of each element
    left_products = [1] * n
    right_products = [1] * n
    
    # Calculate products to the left of each element
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]
    
    # Calculate products to the right of each element
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]
    
    # Multiply left and right products to get the result
    result = [left_products[i] * right_products[i] for i in range(n)]
    
    return result

# Example usage:
nums = [1, 2, 3, 4]
print(product_except_self(nums))  # Output: [24, 12, 8, 6]
