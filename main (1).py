def is_palindromic_integer(my_list):
    #Checking if all the integers are positive or not and initializing the variable
    is_all_positive = all(item >= 0 for item in my_list)
    #Initializing the variable
    is_palindrome = False

    if is_all_positive == True:
        for item in my_list:
            #Converting the integer into a string and reversing it 
            item_str = str(item)[::-1]
            #Checking weather the string is a palindrome or not
            if str(item) == item_str:
                is_palindrome = True       
    #Printing the result 
    if is_all_positive == True and is_palindrome == True:
        print('True')
    else:
        print('False')


if __name__ == '__main__':
    #Defining an empty list
    my_list = []
    #taking input for the number of integers
    number_of_integers = input()
    #taking input for the list
    my_list = list(map(int, input().split()))
    #Calling the function
    is_palindromic_integer(my_list)
