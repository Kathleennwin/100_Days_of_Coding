student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))

# total_exam_score = sum(student_scores)
#
# sum = 0
# for score in student_scores:
#     sum+= score
#     print(sum)
# print(sum)

# print(max(student_scores))

# PAUSE 1 - Max
high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
        print(high_score)
print(high_score)