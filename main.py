#1
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

#2
x, y, a = (1, 2, 5)
print(x)
print(y)
print(a)
#3
name, age, company = ("Илья", 18, "НГТУ")
print(name)
print(age)
print(company)
#4
people = ["Андрей", "Екатерина", "Сергей"]
first, second, third = people
print(first)
print(second)
print(third)
#5
dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
r, b, g = dictionary
print(r)
print(b)
print(g)
print(dictionary[g])
#6
people = [
("Андрей", 17, "НГТУ"),
("Екатерина", 17, "НГУ"),
("Сергей", 19, "НГУЭУ")
]

for name, age, company in people:
    print(f"Name: {name}, Age: {age}, Company: {company}")
#7
people = ["Андрей", "Екатерина", "Сергей"]
for index, name in enumerate(people):
    print(f"{index}.{name}")
#8
person =("Илья", 18, "НГТУ")
name, _, company = person
print(name)
print(company)
name, _, company = person
print(_)
#9
num1=1
num2=2
num3=3
*numbers,=num1,num2,num3
print(numbers)
#10
head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)
#11
*head, tail = [1, 2, 3, 4, 5]
print(head)
print(tail)
#12
head, *middle, tail = [1, 2, 3, 4, 5]
print(head)
print(middle)
print(tail)
#13
first, second, *other = [1, 2, 3, 4, 5]
print(first)
print(second)
print(other)
#14
first, _, third, *_, last = [1, 2, 3, 4, 5, 6, 7, 8]
print(first)
print(third)
print(last)
#15
red, *other, green = {"red":"красный", "blue":"синий", "yellow":"желтый", "green":"зеленый"}
print(red)
print(green)
print(other)
#16
nums1 = [1, 2, 3]
nums2 = (4, 5, 6)
nums3 = [*nums1, *nums2]
print(nums3)
#17
dictionary1 = {"red":"красный", "blue":"синий"}
dictionary2 = {"green":"зеленый", "yellow":"желтый"}
dictionary3 = {**dictionary1, **dictionary2}
print(dictionary3)



