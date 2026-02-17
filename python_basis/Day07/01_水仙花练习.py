import a_fn

if __name__ == '__main__':
    water_l = a_fn.water_flower()
    print(water_l)


coordinates = (30, 40)
x, y = coordinates
print(f"x = {x}, y = {y}")

a, b, c = 1, 2, 3
a, b, c = b, c, a
print(a, b, c)

data = [(1, 2), (3, 4)]
(a, b), (c, d) = data
print(a + b + c + d)

# def multiply(a, b):
#     return a * b

multiply = lambda a, b: a * b

print(multiply(1, 2))

# 按照年龄对学生列表进行降序排序，补全代码



students = [
    {"name": "德华", "age": 19, "score": 100},
    {"name": "成龙", "age": 15, "score": 90},
    {"name": "李连杰", "age": 18, "score": 95}
]

def get_student_age(student_dict):
    return student_dict['age']

students.sort(key=get_student_age, reverse=True)
print(students)