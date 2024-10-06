data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

summ = 0
def calculate_structure_sum(data_structure):
    global summ

    for current_element in data_structure:
        if isinstance(current_element, dict) == True:
            dict_to_list = list()
            for key, val in current_element.items():
                dict_to_list.append(key)
                dict_to_list.append(val)
            calculate_structure_sum(dict_to_list)
        elif isinstance(current_element,int):
            summ = summ + current_element
        elif isinstance(current_element,str):
            summ = summ + len(current_element)
        else:
            calculate_structure_sum(current_element)
    return(summ)

result = calculate_structure_sum(data_structure)
print(result)