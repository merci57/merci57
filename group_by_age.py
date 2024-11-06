def group_by_age(name_age_list):
    age_dict = {}
    
    # Iterate through the list of tuples
    for name, age in name_age_list:
        # If the age already exists as a key, append the name to the list
        if age in age_dict:
            age_dict[age].append(name)
        else:
            # If the age is not in the dictionary, create a new list with the name
            age_dict[age] = [name]
    
    return age_dict

# Example usage:
name_age_list = [("Alice", 30), ("Bob", 25), ("Charlie", 30), ("David", 25), ("Eve", 35)]
result = group_by_age(name_age_list)
print(result)