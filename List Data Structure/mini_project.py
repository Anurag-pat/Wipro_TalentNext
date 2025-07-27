"""
Given the participant's score sheet for your University Sports Day, you are required to find the runner-up score. You have scores. Store them in a list and find the score of the runner-up.

Sample input: [2, 3, 6, 6, 5]

Sample output: 5

Explanation: Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
"""
def find_runner_up(scores):
    
    unique_scores = set(scores)
    
    
    unique_scores.remove(max(unique_scores))
    
    
    runner_up = max(unique_scores)
    
    return runner_up


scores = [2, 3, 6, 6, 5]

print("Runner-up score:", find_runner_up(scores))

"""
You have a record of n students. Each record contains the student's name, and their percent marks in Math, Physics and Chemistry. The marks can be floating values. You are required to save the record in a dictionary data type.

Student's name is the key. Marks stored in a list is the value. The user enters a student's name. Output the average percentage marks obtained by that student.

Formula: (sum of marks) / (no of subjects)

Sample Input: {

"Krishna":

[67, 68, 69],

"Arjun"

: (70, 98, 63],

"Malika": [52, 56, 60]}

Sample output:

Enter a name: Malika

Average percentage mark: 56

Explanation:

Marks for Malika are [52, 56, 60] whose average is (52+56+60)/3 =>56
"""
student_records = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}


name = input("Enter a name: ")


if name in student_records:
    marks = student_records[name]
    average = sum(marks) / len(marks)
    print("Average percentage mark:", round(average))
else:
    print("Student not found.")
