def grades(x):
    grades_list = ['A', 'B', 'C', 'D', 'F']
    assert x in grades_list
    return f"You have got {x}"
