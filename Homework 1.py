numbers = [2, -1, 3, 5, 10, 3, -5, -10, 5, 7]
number_M = 4
count_positive = 0
count_M = 0

for i in range(len(numbers)):
    if numbers[i] > 0:
        count_positive += 1
print("положительных чисел", count_positive)

for i in range(len(numbers)):
    if numbers[i] > number_M:
        count_M += 1
print("чисел больше М", count_M)

max_number = max(numbers)
print("максимальное число в списке", max_number)

print("индекс максимального элемента", numbers.index(max(numbers)))

mean = sum(numbers) / (len(numbers))
print("среднее арифметическое списка", mean)