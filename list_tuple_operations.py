def list_operations():
    """Perform various list operations"""
    # Create list of favorite movies
    movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction", "Forrest Gump"]
    print("Original list:", movies)
    
    # Print third movie
    print("\nThird movie:", movies[2])
    
    # Add new movie
    movies.append("Inception")
    print("\nAfter adding new movie:", movies)
    
    # Remove second movie
    removed_movie = movies.pop(1)
    print(f"\nRemoved movie: {removed_movie}")
    print("After removing second movie:", movies)
    
    # Sort list
    movies.sort()
    print("\nSorted list:", movies)
    
    # Create new list with first and last movie
    first_last = [movies[0], movies[-1]]
    print("\nFirst and last movies:", first_last)

def tuple_operations():
    """Perform various tuple operations"""
    # Create tuple of favorite foods
    foods = ("Pizza", "Pasta", "Burger", "Sushi", "Ice Cream")
    print("Original tuple:", foods)
    
    # Print second food
    print("\nSecond food:", foods[1])
    
    # Try to change second food (will raise error)
    try:
        foods[1] = "Salad"
    except TypeError as e:
        print("\nCannot modify tuple:", e)
    
    # Create new tuple with first and last food
    first_last = (foods[0], foods[-1])
    print("\nFirst and last foods:", first_last)
    
    # Print number of foods
    print("\nNumber of foods:", len(foods))
    
    # Convert tuple to list
    foods_list = list(foods)
    print("\nConverted to list:", foods_list)

def print_integers_up_to_n():
    """Print integers from 0 to n"""
    n = int(input("Enter a number: "))
    for i in range(n + 1):
        print(i)

def print_string_characters():
    """Print each character in string on new line"""
    text = input("Enter a string: ")
    for char in text:
        print(char)

def print_pattern():
    """Print a pattern"""
    n = 5
    for i in range(1, n + 1):
        print('*' * i)
    for i in range(n - 1, 0, -1):
        print('*' * i)

if __name__ == "__main__":
    print("List Operations:")
    list_operations()
    
    print("\nTuple Operations:")
    tuple_operations()
    
    print("\nPrint integers up to n:")
    print_integers_up_to_n()
    
    print("\nPrint string characters:")
    print_string_characters()
    
    print("\nPrint pattern:")
    print_pattern() 