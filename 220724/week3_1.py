inp = input("Input Math Com Material: ")
math, com, material = inp.split(" ")
math_grade_val = material_grade_val = com_grade_val = 0.0
math_grade = com_grade = material_grade = "N/A"

math = int(math)
com = int(com)
material = int(material)

if math >= 86:
    math_grade = "A"
    math_grade_val = 4.00
elif math >= 80:
    math_grade = "A-"
    math_grade_val = 3.75
elif math >= 76:
    math_grade = "B+"
    math_grade_val = 3.50
elif math >= 73:
    math_grade = "B"
    math_grade_val = 3.25
elif math >= 70:
    math_grade = "B-"
    math_grade_val = 3.00
elif math >= 66:
    math_grade = "C+"
    math_grade_val = 2.50
elif math >= 63:
    math_grade = "C"
    math_grade_val = 2.25
elif math >= 60:
    math_grade = "C-"
    math_grade_val = 2.00
elif math >= 56:
    math_grade = "D+"
    math_grade_val = 1.50
elif math >= 53:
    math_grade = "D"
    math_grade_val = 1.25
elif math >= 50:
    math_grade = "D-"
    math_grade_val = 1.00
else:
    math_grade = "F"
    math_grade_val = 0.00

if com >= 86:
    com_grade = "A"
    com_grade_val = 4.00
elif com >= 80:
    com_grade = "A-"
    com_grade_val = 3.75
elif com >= 76:
    com_grade = "B+"
    com_grade_val = 3.50
elif com >= 73:
    com_grade = "B"
    com_grade_val = 3.25
elif com >= 70:
    com_grade = "B-"
    com_grade_val = 3.00
elif com >= 66:
    com_grade = "C+"
    com_grade_val = 2.50
elif com >= 63:
    com_grade = "C"
    com_grade_val = 2.25
elif com >= 60:
    com_grade = "C-"
    com_grade_val = 2.00
elif com >= 56:
    com_grade = "D+"
    com_grade_val = 1.50
elif com >= 53:
    com_grade = "D"
    com_grade_val = 1.25
elif com >= 50:
    com_grade = "D-"
    com_grade_val = 1.00
else:
    com_grade = "F"
    com_grade_val = 0.00

if material >= 86:
    material_grade = "A"
    material_grade_val = 4.00
elif material >= 80:
    material_grade = "A-"
    material_grade_val = 3.75
elif material >= 76:
    material_grade = "B+"
    material_grade_val = 3.50
elif material >= 73:
    material_grade = "B"
    material_grade_val = 3.25
elif material >= 70:
    material_grade = "B-"
    material_grade_val = 3.00
elif material >= 66:
    material_grade = "C+"
    material_grade_val = 2.50
elif material >= 63:
    material_grade = "C"
    material_grade_val = 2.25
elif material >= 60:
    material_grade = "C-"
    material_grade_val = 2.00
elif material >= 56:
    material_grade = "D+"
    material_grade_val = 1.50
elif material >= 53:
    material_grade = "D"
    material_grade_val = 1.25
elif material >= 50:
    material_grade = "D-"
    material_grade_val = 1.00
else:
    material_grade = "F"
    material_grade_val = 0.00

sum = math_grade_val + com_grade_val + material_grade_val
grade = sum / 3

print(f"Math: {math_grade}")
print(f"Com: {com_grade}")
print(f"Material: {material_grade}")

if math_grade == "D-" or com_grade == "D-" or material_grade == "D-" or math_grade == "F" or com_grade == "F" or material_grade == "F" or grade < 2:
    print(f"พี่ก้านหยกรีบถอน")
else:
    print(f"เกรดเฉลี่ย {grade:.2f}")           
        