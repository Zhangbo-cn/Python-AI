
def water_flower():
    for num in range(10, 1000):
        hundred = num // 100
        ten = num // 10 % 10
        units = num % 10

        if hundred ** 3 + ten ** 3 + units ** 3 == num:
            print(num)


if __name__ == '__main__':
    water_flower()