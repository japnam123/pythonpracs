def gcd(a, b):
    """Find GCD of two positive numbers"""
    while b:
        a, b = b, a % b
    return a

def sum_of_digits(number):
    """Find sum of digits in a number"""
    return sum(int(digit) for digit in str(number))

def print_multiples_of_three():
    """Print first 10 multiples of 3"""
    for i in range(1, 11):
        print(f"3 x {i} = {3 * i}")

def find_largest_element(arr):
    """Find largest element in an array"""
    return max(arr)

def add_matrices(matrix1, matrix2):
    """Add two matrices"""
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have same dimensions"
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def sum_odd_even_numbers(n):
    """Find sum of all odd and even numbers up to n"""
    odd_sum = sum(i for i in range(1, n + 1) if i % 2 != 0)
    even_sum = sum(i for i in range(1, n + 1) if i % 2 == 0)
    return odd_sum, even_sum

def fibonacci_sequence(n):
    """Display Fibonacci sequence up to n terms"""
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def is_palindrome(text):
    """Check if string is palindrome using slicing"""
    return text == text[::-1]

def count_vowels_consonants_blanks(text):
    """Count vowels, consonants and blanks in a string"""
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char in consonants)
    blank_count = text.count(' ')
    
    return vowel_count, consonant_count, blank_count

def find_repeated_chars(text):
    """Find characters that are repeated in string"""
    repeated = set()
    for char in text:
        if text.count(char) > 1:
            repeated.add(char)
    return repeated

def calculate_grade(marks):
    """Calculate average marks, percentage and grade"""
    total_marks = sum(marks)
    average = total_marks / len(marks)
    percentage = (total_marks / (len(marks) * 100)) * 100
    
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    return average, percentage, grade

if __name__ == "__main__":
    # Example usage
    print("GCD of 48 and 18:", gcd(48, 18))
    print("Sum of digits in 12345:", sum_of_digits(12345))
    print("\nFirst 10 multiples of 3:")
    print_multiples_of_three()
    
    arr = [1, 5, 3, 9, 2, 6]
    print("\nLargest element in array:", find_largest_element(arr))
    
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    print("\nMatrix addition:", add_matrices(matrix1, matrix2))
    
    odd_sum, even_sum = sum_odd_even_numbers(10)
    print(f"\nSum of odd numbers up to 10: {odd_sum}")
    print(f"Sum of even numbers up to 10: {even_sum}")
    
    print("\nFibonacci sequence up to 10 terms:", fibonacci_sequence(10))
    print("\nIs 'radar' a palindrome?", is_palindrome("radar"))
    
    text = "Hello World"
    vowels, consonants, blanks = count_vowels_consonants_blanks(text)
    print(f"\nIn '{text}':")
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"Blanks: {blanks}")
    
    print("\nRepeated characters in 'hello':", find_repeated_chars("hello"))
    
    marks = [85, 90, 75, 95, 80]
    avg, percentage, grade = calculate_grade(marks)
    print(f"\nFor marks {marks}:")
    print(f"Average: {avg}")
    print(f"Percentage: {percentage}%")
    print(f"Grade: {grade}") 