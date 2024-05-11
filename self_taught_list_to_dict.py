# Use the function 'zip', then dict to conversation from list to dict

def united_list_to_dict(first_list, second_list):
    return dict(zip(first_list, second_list))


first_resault = united_list_to_dict(
    ['apple', 'pineapple', 'waterlemon'],
    ['like', 'yammy', 'great']
)
print(first_resault)

second_resault = united_list_to_dict(
    ['table', 'sofa', 'armchair'],
    [10, 20, 30]
)
print(second_resault)
