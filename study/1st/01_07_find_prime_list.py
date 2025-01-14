input = 2000

def find_prime_list_under_number(number):
    arr = []
    for n in range(2, number + 1):
        for i in arr:
            if n % i == 0 and i * i <= n:
                break
        else:
            arr.append(n)
    return arr





result = find_prime_list_under_number(input)
print(result)