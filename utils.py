def find_max(numbers):
    maxium = numbers[0]
    for sing_number in numbers:
        if maxium < sing_number:
            maxium = sing_number
    return maxium
