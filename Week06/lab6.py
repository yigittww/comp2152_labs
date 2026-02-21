# ============================================================
# WEEK 05 LAB: RECURSION & FUNCTIONS
# COMP2152 - Python Programming
# ============================================================

# ============================================================
# Question 1: Fibonacci Number (LeetCode #509)
# ============================================================

def fib(n):
    """
    Calculates the nth Fibonacci number using recursion.
    F(n) = F(n-1) + F(n-2)
    """
    # Base cases to stop recursion
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive case: move toward base case
    return fib(n - 1) + fib(n - 2)

# Testing Fibonacci
print("Fibonacci Sequence (0 to 10):")
print("-" * 30)
for i in range(11):
    print(f"F({i}) = {fib(i)}")


# ============================================================
# Question 2: FizzBuzz (LeetCode #412)
# ============================================================

def fizz_buzz(n):
    """
    Generates a list of strings from 1 to n with FizzBuzz logic.
    """
    result = []
    
    for i in range(1, n + 1):
        # Most restrictive condition first
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
            
    return result

# Verification for FizzBuzz
print("\nFizzBuzz (n=15):")
print(fizz_buzz(15))


# ============================================================
# Question 3: Binary Search (LeetCode #704)
# ============================================================

# Part A: Iterative Solution
def binary_search_iterative(nums, target):
    """
    Searches for target in a sorted list using a while loop.
    Time Complexity: O(log n)
    """
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid  # Target found
        elif target < nums[mid]:
            right = mid - 1  # Discard right half
        else:
            left = mid + 1   # Discard left half
            
    return -1  # Target not in list

# Part B: Recursive Solution
def binary_search_recursive(nums, target, left, right):
    """
    Searches for target in a sorted list using recursion.
    """
    # Base case: search space exhausted
    if left > right:
        return -1
        
    mid = (left + right) // 2
    
    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        # Recursive call on left half
        return binary_search_recursive(nums, target, left, mid - 1)
    else:
        # Recursive call on right half
        return binary_search_recursive(nums, target, mid + 1, right)

# Wrapper function for recursion
def search_recursive(nums, target):
    """Wrapper to initialize bounds for the recursive search."""
    return binary_search_recursive(nums, target, 0, len(nums) - 1)


# ============================================================
# Verification: Results Matching
# ============================================================
nums_test = [-1, 0, 3, 5, 9, 12]
target_val = 9

print("\nBinary Search Verification (Target = 9):")
print(f"Iterative Result: {binary_search_iterative(nums_test, target_val)}")
print(f"Recursive Result: {search_recursive(nums_test, target_val)}")