from dd_class import Elevage
from dd_class import Dragodinde
#import Bot_repro_dd_dofus.DQNAgent

def create_elevage():

    dragodindes_data = [
        (1, "M", "Rousse", 1),
        (2, "F", "Rousse", 1),
        (3, "M", "Amande", 1),
        (4, "F", "Amande", 1),
        (5, "M", "Dorée", 1),
        (6, "F", "Dorée", 1)
    ]

    list_dd = []
    for id, gender, color, generation in dragodindes_data:
        dragodinde = Dragodinde(id, gender, color, generation)
        list_dd.append(dragodinde)

    return Elevage(list_dd)

if __name__ == "__main__" :
    elevage = create_elevage()
    new_dd, dic_prob = elevage.accouplement_naissance(elevage.get_dd_by_id(8), elevage.get_dd_by_id(1))
    print(str(new_dd), dic_prob)
    print(" ")
    if new_dd.get_sex() == "F" : 
        new_dd2, _ = elevage.accouplement_naissance(elevage.get_dd_by_id(9), elevage.get_dd_by_id(3))
    else :
        new_dd2, _ = elevage.accouplement_naissance(elevage.get_dd_by_id(9), elevage.get_dd_by_id(4))
    print(str(new_dd2), dic_prob)
