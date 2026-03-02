def sum_letters(s):
    # Create a string variable with all letters
    str_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # init sum_letter variable in 0
    sum_letters = 0
    # iterate over each character in string s
    for char in s:
        # try (if) character in str_letters (this is because index function raices a error if the character is not found)
        try:
            index = str_letters.index(char.upper()) + 1
            sum_letters += index
        # except (else) character is not in str_letter
        except:
            continue

    return sum_letters

if __name__ == '__main__':
    print(sum_letters("Hello"))
    print('-----')
    print(sum_letters("freeCodeCamp"))
    print('-----')
    print(sum_letters("The quick brown fox jumps over the lazy dog."))
    print('-----')
    print(sum_letters("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ex nisl, pretium eu varius blandit, facilisis quis eros. Vestibulum ante ipsum primis in faucibus orci."))
    print('-----')
    print(sum_letters("</404>"))