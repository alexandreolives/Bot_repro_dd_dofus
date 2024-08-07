from dd_class import Elevage
from dd_class import Dragodinde
import DQNAgent

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
    