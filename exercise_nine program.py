# Hello! this program checks if the given number is an example of a palindrome number.

# pseudocode

def palindrome(number):
    print("Given number", number)
    original_num = number
    
    # Reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # Check numbers
    if original_num == reverse_num:
        print("This Given number is an example of a palindrome number")
    else:
        print("This Given number is not an example of a palindrome number")

# Given numbers
palindrome(121)
palindrome(125)
