import random

def get_random(ingredient_list, element_no=1):
	ingredient_list = list(ingredient_list)
	list_of_randoms = []
	for i in range(max(element_no, len(ingredient_list))):
		list_of_randoms.append(ingredient_list.pop(random.randint(0,len(ingredient_list)-1)))
	return list_of_randoms	