def dictionary_operations():
    """Perform various dictionary operations"""
    # Create dictionary of favorite books
    books = {
        "To Kill a Mockingbird": "Harper Lee",
        "1984": "George Orwell",
        "The Great Gatsby": "F. Scott Fitzgerald",
        "Pride and Prejudice": "Jane Austen"
    }
    print("Original dictionary:", books)

    # Add new book
    books["The Catcher in the Rye"] = "J.D. Salinger"
    print("\nAfter adding new book:", books)

    # Remove a book
    del books["1984"]
    print("\nAfter removing a book:", books)

    # Print book titles
    print("\nBook titles:", list(books.keys()))

    # Print authors
    print("\nAuthors:", list(books.values()))

def set_operations():
    """Perform various set operations"""
    # Create set of favorite colors
    colors = {"Blue", "Red", "Green", "Yellow", "Black"}
    print("Original set:", colors)

    # Add new color
    colors.add("Purple")
    print("\nAfter adding new color:", colors)

    # Remove a color
    colors.remove("Yellow")
    print("\nAfter removing a color:", colors)

    # Create set of colors starting with 'B'
    b_colors = {color for color in colors if color.startswith('B')}
    print("\nColors starting with 'B':", b_colors)

    # Print number of colors
    print("\nNumber of colors:", len(colors))

if __name__ == "__main__":
    dictionary_operations()
    set_operations() 