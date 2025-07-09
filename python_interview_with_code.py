
# Python Interview Coding Questions with Code

# 1. Reverse a String
s = "hello"
print("1. Reverse:", s[::-1])

# 2. Check for Palindrome
s = "madam"
print("2. Palindrome:", s == s[::-1])

# 3. Find Factorial using Recursion
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
print("3. Factorial:", factorial(5))

# 4. Generate Fibonacci Series (Iterative)
a, b = 0, 1
print("4. Fibonacci:", end=" ")
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b
print()

# 5. Check if a Number is Prime
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
print("5. Prime:", is_prime(11))

# 6. Find GCD of Two Numbers
import math
print("6. GCD:", math.gcd(12, 18))

# 7. Count Vowels in a String
s = "Hello World"
print("7. Vowels:", sum(1 for c in s.lower() if c in 'aeiou'))

# 8. Find Duplicate Elements in a List
lst = [1, 2, 2, 3, 4, 4]
duplicates = set([x for x in lst if lst.count(x) > 1])
print("8. Duplicates:", duplicates)

# 9. Check if Two Strings are Anagrams
from collections import Counter
print("9. Anagram:", Counter("listen") == Counter("silent"))

# 10. Merge Two Sorted Lists
a, b = [1, 3, 5], [2, 4, 6]
print("10. Merged:", sorted(a + b))

# 11. Find Missing Number in Range 1 to n
lst = [1, 2, 4, 5]
n = 5
print("11. Missing Number:", sum(range(1, n+1)) - sum(lst))

# 12. Check if a Number is an Armstrong Number
n = 153
print("12. Armstrong:", n == sum(int(d)**3 for d in str(n)))

# 13. Check if a String is a Pangram
import string
s = "The quick brown fox jumps over the lazy dog"
print("13. Pangram:", set(string.ascii_lowercase).issubset(s.lower()))

# 14. Remove Duplicates from a List
lst = [1, 2, 2, 3]
print("14. Unique List:", list(set(lst)))

# 15. Find the Second Largest Number in a List
lst = [1, 2, 3, 4]
print("15. Second Largest:", sorted(set(lst))[-2])

# 16. Count Occurrences of Elements in a List
from collections import Counter
lst = [1, 2, 2, 3]
print("16. Occurrences:", Counter(lst))

# 17. Transpose a Matrix
matrix = [[1, 2], [3, 4]]
print("17. Transposed:", list(map(list, zip(*matrix))))

# 18. Implement Linear Search
def linear_search(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return -1
print("18. Linear Search:", linear_search([1, 2, 3], 2))

# 19. Implement Binary Search
def binary_search(arr, x):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == x: return mid
        elif arr[mid] < x: low = mid + 1
        else: high = mid - 1
    return -1
print("19. Binary Search:", binary_search([1, 2, 3, 4, 5], 4))

# 20. Find Intersection of Two Lists
a, b = [1, 2, 3], [2, 3, 4]
print("20. Intersection:", list(set(a) & set(b)))

# 21. Flatten a Nested List
from itertools import chain
nested = [[1, 2], [3, 4]]
print("21. Flattened:", list(chain.from_iterable(nested)))

# 22. Find All Armstrong Numbers in a Range
print("22. Armstrong Numbers:", [i for i in range(1000) if i == sum(int(d)**len(str(i)) for d in str(i))])

# 23. Count Number of Words in a String
s = "Hello world from Python"
print("23. Word Count:", len(s.split()))

# 24. Implement String Compression (e.g. a3b2c2)
def compress(s):
    result = ""
    i = 0
    while i < len(s):
        count = 1
        while i+1 < len(s) and s[i] == s[i+1]:
            count += 1
            i += 1
        result += s[i] + str(count)
        i += 1
    return result
print("24. Compressed:", compress("aaabbcc"))

# 25. Print Pascal’s Triangle up to n Rows
def pascal(n):
    for i in range(n):
        val = 1
        for j in range(i+1):
            print(val, end=' ')
            val = val * (i - j) // (j + 1)
        print()
print("25. Pascal's Triangle:")
pascal(5)

# 26. Find the Majority Element in a List
lst = [1, 2, 3, 2, 2]
count = Counter(lst)
print("26. Majority:", max(count, key=count.get))

# 27. Move All Zeros to End of List
lst = [0, 1, 0, 3, 12]
res = [x for x in lst if x != 0] + [0] * lst.count(0)
print("27. Move Zeros:", res)

# 28. Implement a Stack using List
stack = []
stack.append(1)
stack.append(2)
print("28. Stack Pop:", stack.pop())
print("28. Stack:", stack)

# 29. Rotate a List by k Elements
lst = [1, 2, 3, 4, 5]
k = 2
print("29. Rotated List:", lst[k:] + lst[:k])

# 30. Check if a List is Sorted
lst = [1, 2, 3, 4]
print("30. Is Sorted:", lst == sorted(lst))
