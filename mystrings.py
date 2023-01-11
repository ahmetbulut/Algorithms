def scan_and_print(sequence):
    index = 0

    while index < len(sequence):
        print(sequence[index])
        index = index + 1

def scan_and_print_forloop(sequence):

    for item in sequence:
        print(item)


#scan_and_print('CSE 101')
#scan_and_print_forloop('CSE 101')


def count_as(word):
    counter = 0

    for item in word:
        if item == 'a':
            counter = counter + 1 # increment counter by 1

    return counter

test = 'ZZZZZZ'
#print('The number of letter a in', test, 'is', count_as(test))

print(test.lower(), test)

test.