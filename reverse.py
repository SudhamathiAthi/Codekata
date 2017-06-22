def reverse(text):

    lst = []
    count = 1
    hello=input("Enter the string to be reversed:")
    for i in range(0,len(text)):

        lst.append(text[len(text)-count])
        count += 1

    lst = ''.join(lst)
    return lst

print reverse('hello')

if __name__ == '__reverse__':
    reverse()
