student_marks = open("Fafali.txt") #All the scores in this File is for one student 

scores = list(student_marks)

student_marks.close()

scores = list(map(lambda x : int(x.strip()),scores))

if len(scores) == 0:
    print("No Scores found")
else:
    average = sum(scores) / len(scores)

    if average >= 70: #This is to check whether the average of that particular student is a pass or a fail 
      print("You have passed ")
    else:
     print("You have failed")     

    print("Your Average is :",round(average,2)) #Shows you the average of  that paticular student
    
    
    





