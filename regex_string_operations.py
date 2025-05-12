import re

def extract_date_components(text):
    """Extract year, month and date from a string"""
    pattern = r'(\d{4})-(\d{2})-(\d{2})'
    match = re.search(pattern, text)
    if match:
        year, month, date = match.groups()
        return year, month, date
    return None

def extract_three_digit_numbers(text):
    """Extract only 3 digit numbers from string"""
    pattern = r'\b\d{3}\b'
    return re.findall(pattern, text)

def extract_words_and_numbers(text):
    """Extract all words and numbers from string"""
    pattern = r'\b\w+\b'
    return re.findall(pattern, text)

def find_vowel_starting_words(text):
    """Find words starting with vowels"""
    pattern = r'\b[aeiouAEIOU]\w+\b'
    return re.findall(pattern, text)

def find_consonant_starting_words(text):
    """Find words starting with consonants"""
    pattern = r'\b[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]\w+\b'
    return re.findall(pattern, text)

def count_articles(text):
    """Count total numbers of a, an and the"""
    pattern = r'\b(a|an|the)\b'
    matches = re.findall(pattern, text.lower())
    return len(matches)

def find_long_words(text):
    """Find words which are at least 4 characters long"""
    pattern = r'\b\w{4,}\b'
    return re.findall(pattern, text)

def check_number_at_end(text):
    """Check for a number at the end of a string"""
    pattern = r'\d+$'
    return bool(re.search(pattern, text))

def check_four_digit_number(text):
    """Check for a number starting with 2 or 1 and having 4 digits"""
    pattern = r'\b[12]\d{3}\b'
    return bool(re.search(pattern, text))

def check_a_ending_b(text):
    """Check for a string that has an 'a' followed by anything, ending in 'b'"""
    pattern = r'a.*b$'
    return bool(re.search(pattern, text))

if __name__ == "__main__":
    # Test date extraction
    date_text = "The event is on 2024-03-15"
    year, month, date = extract_date_components(date_text)
    print(f"Date components: Year={year}, Month={month}, Date={date}")
    
    # Test three digit numbers
    number_text = "123 4567 789 101"
    print("\nThree digit numbers:", extract_three_digit_numbers(number_text))
    
    # Test words and numbers
    text = "Hello123 World 456"
    print("\nWords and numbers:", extract_words_and_numbers(text))
    
    # Test vowel starting words
    text = "Apple Orange Banana"
    print("\nVowel starting words:", find_vowel_starting_words(text))
    
    # Test consonant starting words
    print("\nConsonant starting words:", find_consonant_starting_words(text))
    
    # Test article counting
    text = "The cat and a dog saw an elephant"
    print("\nNumber of articles:", count_articles(text))
    
    # Test long words
    text = "Python programming is awesome"
    print("\nWords with 4+ characters:", find_long_words(text))
    
    # Test number at end
    text = "Hello123"
    print("\nHas number at end:", check_number_at_end(text))
    
    # Test four digit number
    text = "1234 2345 3456"
    print("\nHas four digit number starting with 1 or 2:", check_four_digit_number(text))
    
    # Test a ending b
    text = "a123b"
    print("\nHas 'a' followed by anything ending in 'b':", check_a_ending_b(text)) 