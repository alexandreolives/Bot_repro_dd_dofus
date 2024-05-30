import dd_class
#import Bot_repro_dd_dofus.DQNAgent

def creat_elevage() :
    elevage = dd_class.Elevage()
    dd_rousse1 = dd_class.Dragodinde(1, "M", "Rousse", 1)
    dd_rousse2 = dd_class.Dragodinde(2, "F", "Rousse", 1)

    dd_amande1 = dd_class.Dragodinde(3, "M", "Amande", 1)
    dd_amande2 = dd_class.Dragodinde(4, "F", "Amande", 1)

    dd_dorée1 = dd_class.Dragodinde(5, "M", "Dorée", 1)
    dd_dorée2 = dd_class.Dragodinde(6, "F", "Dorée", 1)

    dd_am_roM = dd_class.Dragodinde(7, "M", "Amande et Dorée", 2)
    dd_am_roF = dd_class.Dragodinde(8, "F", "Rousse et Dorée", 2)

    elevage.add_DD(dd_rousse1)
    elevage.add_DD(dd_rousse2)
    elevage.add_DD(dd_amande1)
    elevage.add_DD(dd_amande2)
    elevage.add_DD(dd_dorée1)
    elevage.add_DD(dd_dorée2)
    elevage.add_DD(dd_am_roM)
    elevage.add_DD(dd_am_roF)

    return elevage

def creat_generations() :
    # Création des générations
    generation_1 = dd_class.Generation(1, True, ["Rousse", "Amande", "Dorée"])
    generation_2 = dd_class.Generation(2, False, ["Rousse et Amande", "Rousse et Dorée", "Amande et Dorée"])
    generation_3 = dd_class.Generation(3, True, ["Indigo", "Ebène"])
    generation_4 = dd_class.Generation(4, False, ["Rousse et Indigo", "Rousse et Ebène", "Amande et Indigo", "Amande et Ebène", 
                                        "Dorée et Indigo", "Dorée et Ebène", "Indigo et Ebène"])
    generation_5 = dd_class.Generation(5, True, ["Pourpre", "Orchidée"])
    generation_6 = dd_class.Generation(6, False, ["Pourpre et Rousse", "Orchidée et Rousse", "Amande et Pourpre", "Amande et Orchidée", 
                                        "Dorée et Pourpre", "Dorée et Orchidée", "Indigo et Pourpre", "Indigo et Orchidée", 
                                        "Ebène et Pourpre", "Ebène et Orchidée", "Pourpre et Orchidée"])
    generation_7 = dd_class.Generation(7, True, ["Ivoire", "Turquoise"])
    generation_8 = dd_class.Generation(8, False, ["Ivoire et Rousse", "Turquoise et Rousse", "Amande et Ivoire", "Amande et Turquoise", 
                                        "Dorée et Ivoire", "Dorée et Turquoise", "Indigo et Ivoire", "Indigo et Turquoise", 
                                        "Ebène et Ivoire", "Ebène et Turquoise", "Pourpre et Ivoire", "Turquoise et Pourpre", 
                                        "Ivoire et Orchidée", "Turquoise et Orchidée", "Ivoire et Turquoise"])
    generation_9 = dd_class.Generation(9, True, ["Emeraude", "Prune"])
    generation_10 = dd_class.Generation(10, False, ["Rousse et Emeraude", "Rousse et Prune", "Amande et Emeraude", "Amande et Prune", 
                                        "Dorée et Emeraude", "Dorée et Prune", "Indigo et Emeraude", "Indigo et Prune", 
                                        "Ebène et Emeraude", "Ebène et Prune", "Pourpre et Emeraude", "Pourpre et Prune", 
                                        "Orchidée et Emeraude", "Orchidée et Prune", "Ivoire et Emeraude", "Ivoire et Prune", 
                                        "Turquoise et Emeraude", "Turquoise et Prune"])

    # Création de l'objet Generations
    generations = dd_class.Generations()

    # Ajout des générations
    generations.add_generation(generation_1)
    generations.add_generation(generation_2)
    generations.add_generation(generation_3)
    generations.add_generation(generation_4)
    generations.add_generation(generation_5)
    generations.add_generation(generation_6)
    generations.add_generation(generation_7)
    generations.add_generation(generation_8)
    generations.add_generation(generation_9)
    generations.add_generation(generation_10)
    return generations

if __name__ == "__main__" :
    elevage = creat_elevage()
    generations = creat_generations()
    new_dd = elevage.accouplement_naissance(elevage.get_dd_by_id(8), elevage.get_dd_by_id(7))
    print(str(new_dd))
    #print(str(elevage))