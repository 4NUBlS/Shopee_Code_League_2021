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