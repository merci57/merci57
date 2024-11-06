def remove_vowels():
    # Define a set of vowels, both uppercase and lowercase
    vowels = "aeiouAEIOU"
    
    # Prompt the user to enter a string of text
    text = input("Enter some text: ")
    
    # Use a list comprehension to filter out vowels
    result = ''.join([char for char in text if char not in vowels])
    
    # Output the result
    print("Text without vowels:", result)

# Run the function
remove_vowels()