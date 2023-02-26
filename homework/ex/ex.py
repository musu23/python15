my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
my_list.sort(reverse=False)
my_list.sort(reverse= True)

print(sorted(my_list))
numbers = my_list

even_numbers = numbers[::2]
odd_numbers = numbers[1::2]

sorted_even_numbers = sorted(even_numbers)
sorted_odd_numbers = sorted(odd_numbers)

sorted_numbers_odd = sorted_odd_numbers
sorted_numbers_even = sorted_even_numbers

print(sorted_numbers_odd, sorted_numbers_even)

result = my_list[::3]
print(result)





























