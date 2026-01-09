def calculate_average(numbers):
    if len(numbers) == 0:
        return 0 
    return sum(numbers) / len(numbers)

scores = [85, 90, 78, 92, 88]

average_score = calculate_average(scores)
print("Average score:", average_score)
