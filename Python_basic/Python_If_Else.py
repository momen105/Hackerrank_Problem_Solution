def check_number(n):

    if n % 2 != 0 or n in range(6, 21):
        result = "Weird"
    elif n in range(2, 6) or n > 20:
        result = "Not Weird"

    return result


number = check_number(int(input("Enter Number:")))
print(number)
