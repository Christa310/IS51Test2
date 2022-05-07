"""

To start we will gather the grades from the Final.txt file and 
catputure users input for each grade. Each time we capture the users input,
we append the number to the list. once we have three highest number in the list, 
we sum them up and divide by 3 and output a message to the user.
We will display the number of grades, the average grade, 
and a calculate_percent_above_average to calculate the percentage 
of grades that are above the average grade.

"""

def calculate_percent_above_average(grades, avg):
count = 0
for grade in grades:
if grade > avg:
count += 1
return (count * 100) / len(grades)


def main():
f = open('Final.txt')
grades = []
for line in f:
grades.append(int(line.strip()))
print("Number of grades:", len(grades))
avg = 0
for grade in grades:
avg += grade
avg /= len(grades)
print("Average grade:", avg)
print("Percentage of grades above average: {:.2f}%".format(calculate_percent_above_average(grades, avg)))
f.close()


main()