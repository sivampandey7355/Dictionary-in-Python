#DICTIONARY & SET

student = {
"name" : "Shivam pandey",
"age"  : 21,
"collage" : "Ramdev pg collage",
"city" : "varanshi",
"name" : "mohit pandey"
}   
print(student)
#duplicate value print
print(student["name"])
#update my age 
student["city"] = "Bhadohi"
print(student)
#adding and updating value
student["favsubject"] = "chemsitry"
print(student)
#Removing items
student.pop("age")
print(student)

#DICTIONARY METHOD

print(student.keys())
print(student.values())
print(student.items())
print(student.update())