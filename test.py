import dd_class

def creat_elevage() :

    arbre_1 = dd_class.Genealogie(["Ebène", "Amande"])
    arbre_2 = dd_class.Genealogie(["Indigo", "Rousse"])

    dd_1 = dd_class.Dragodinde(1, "M", "Amande", 1, arbre_1)
    dd_2 = dd_class.Dragodinde(2, "F", "Rousse", 1, arbre_2)

    elevage = dd_class.Elevage([dd_1, dd_2])
    return elevage

if __name__ == "__main__" :
    elevage = creat_elevage()
    new_dd, dic_probability = elevage.accouplement_naissance(elevage.get_dd_by_id(1), elevage.get_dd_by_id(2))
    print(str(new_dd))
    print("dic_probability : ", dic_probability)

    expected_probability = {
        "Rousse": 37,
        "Amande": 37,
        "Indigo": 8,
        "Ebène": 8,
        "Amande et Rousse": 6,
        "Amande et Indigo": 1,
        "Ebène et Rousse": 1,
        "Indigo et Ebène": 0
    }

    # Convert probabilities to percentages if needed
    dic_probability = {k: v * 100 for k, v in dic_probability.items()}

    # Ensure the keys are properly formatted to match expected keys
    formatted_dic_probability = {k.split(' ')[-1]: v for k, v in dic_probability.items()}

    assert formatted_dic_probability == expected_probability, f"Probabilities do not match. Expected: {expected_probability}, but got: {formatted_dic_probability}"
    print("Probabilities match expected values.")