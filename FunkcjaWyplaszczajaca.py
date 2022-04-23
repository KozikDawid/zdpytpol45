def mested_list_flattener_gen(nested_list):
    for lst in nested_list:
        if isinstance(lst, list):
            yield from nested_list_fattener(lst)
        else:
            yield lst

def nested_list_flattener(nested_list):
    return list(mested_list_flattener_gen(nested_list))
