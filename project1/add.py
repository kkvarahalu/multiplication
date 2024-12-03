a=3
print(a)
user_input = int(input("Enter a number: ")) 
even_numbers = [num for num in range(1, user_input + 1) if num % 2 == 0]
print("Even numbers:", even_numbers)
print("total count of even numbers:", len(even_numbers))
user_input=int(input("Enter a name: "))
odd_numbers=[num for num in range(1,user_input+1) if num %2 !=0]
print("odd_numbers:",odd_numbers)
print("Total count of odd numbers:",len(odd_numbers))

X=10
print(id(X))

