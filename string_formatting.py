def print_formatted(number):
    wide = len(bin(number)) - 2

    for i in range(1, number + 1):
        print(str(i).rjust(wide), end=' ')
        print(oct(i).lstrip('0o').rjust(wide), end=' ')
        print((hex(i).lstrip('0x').rjust(wide)).upper(), end=' ')
        print(bin(i).lstrip('0b').rjust(wide))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)