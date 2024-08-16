def reverse_elements(nested_list):
    nested_list.reverse()
    for i in range(len(nested_list)):
        if isinstance(nested_list[i], list):
            reverse_elements(nested_list[i])
    return nested_list
liste_input=[[1, 2], [3, 4], [5, 6, 7]]
reverse_liste=reverse_elements(liste_input)
print(reverse_liste)