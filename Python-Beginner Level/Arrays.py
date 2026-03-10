sample=["First","Name","Selenium", ""]
print(sample)

#by using index we can access the specific value
p=sample[2]
print(p)

#by using len() we can access the length of array
u=len(sample)
print(u)

#using for in loop - to loop all the elements of an array
cars = ["Ford", "Volvo", "BMW"]
for h in cars:
  print(h)

#adding one more element to the array
cars.append("Honda")
print(cars)

#by using pop() we can remove the specific element by using index
sample.pop(3)
print(sample)

#By using remove() we can delete the first occurrence of the specific value
sample.remove("Name")
print(sample)

#count
b=sample.count("Name")
print(b)   #index starting with zero
