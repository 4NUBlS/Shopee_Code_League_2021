# Q&A_1
a = ["บ้าน", "วันนี้", "คน", "อยู่", "เดียว", "ผม"]
print(a[1] + a[5] + a[3] + a[0] + a[2] + a[4])
print("="*30)

# Q&A_2
def calculategrade(myscore):
    if myscore >= 80:
        grade = "A"
    elif myscore >= 70:
        grade = "B"
    elif myscore >= 60:
        grade = "C"
    elif myscore >= 50:
        grade = "D"
    elif myscore < 50:
        grade = "F"
    return grade
print(calculategrade(80))
print("="*30)

# Q&A_3
n = [53, 1, 2, 67, 543, 3, 8, -9, 43, 12]
sums = 0
for i in n:
    sums += i
print(sums)
print("="*30)

# Q&A_4
def sum_list(inputlist):
    sum_n = 0
    for i in inputlist:
        if (i % 2) == 0:
            sum_n += i
    return sum_n
inputlist = [1, 10, 12, 41, 23, 11, 20, 41, 29, 33, 22, 56]
print(sum_list(inputlist))
print("="*30)