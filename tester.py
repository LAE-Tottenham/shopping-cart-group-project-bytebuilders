#formatting tutorial :)

print(' ')

example_list = ['this', 'is', 'a', 'test']

#this is how it looks when u print raw:

print(example_list)

#how to do it in the nice format:
print('--------------------')

for item in example_list:
    print(f'{item}\n')

#if you wanted to make a numbered list:
print('--------------------')

list_count = 1

for item in example_list:
    print(f'{list_count}. {item}\n')
    list_count += 1

#for a dictionary:
print('-------------------------')

dict = {'1':'hello',
        '2': 'hi',
        '3': 'wassup'}

for item in dict:
    print(f'{item}. {dict[item]}\n')

#hope this helps :)