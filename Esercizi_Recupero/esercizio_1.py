def covertion(my_list:list[tuple]) -> dict:
    dict1: dict = {}
    # for element in my_list:
    #     key, value = element[0], element[1]
    for key, value in my_list:
        if key in dict1:
            dict1 += value
        else:
            dict1[key] = value
    return dict1




