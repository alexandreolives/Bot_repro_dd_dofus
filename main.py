from dd_class import Generation
from dd_class import Generations
from bot_dd import *

def creat_generations() :
    # Création des générations
    generation_1 = Generation(1, True, ["Rousse", "Amande", "Dorée"])
    generation_2 = Generation(2, False, ["Rousse et Amande", "Rousse et Dorée", "Amande et Dorée"])
    generation_3 = Generation(3, True, ["Indigo", "Ebène"])
    generation_4 = Generation(4, False, ["Rousse et Indigo", "Rousse et Ebène", "Amande et Indigo", "Amande et Ebène", 
                                        "Dorée et Indigo", "Dorée et Ebène", "Indigo et Ebène"])
    generation_5 = Generation(5, True, ["Pourpre", "Orchidée"])
    generation_6 = Generation(6, False, ["Pourpre et Rousse", "Orchidée et Rousse", "Amande et Pourpre", "Amande et Orchidée", 
                                        "Dorée et Pourpre", "Dorée et Orchidée", "Indigo et Pourpre", "Indigo et Orchidée", 
                                        "Ebène et Pourpre", "Ebène et Orchidée", "Pourpre et Orchidée"])
    generation_7 = Generation(7, True, ["Ivoire", "Turquoise"])
    generation_8 = Generation(8, False, ["Ivoire et Rousse", "Turquoise et Rousse", "Amande et Ivoire", "Amande et Turquoise", 
                                        "Dorée et Ivoire", "Dorée et Turquoise", "Indigo et Ivoire", "Indigo et Turquoise", 
                                        "Ebène et Ivoire", "Ebène et Turquoise", "Pourpre et Ivoire", "Turquoise et Pourpre", 
                                        "Ivoire et Orchidée", "Turquoise et Orchidée", "Ivoire et Turquoise"])
    generation_9 = Generation(9, True, ["Emeraude", "Prune"])
    generation_10 = Generation(10, False, ["Rousse et Emeraude", "Rousse et Prune", "Amande et Emeraude", "Amande et Prune", 
                                        "Dorée et Emeraude", "Dorée et Prune", "Indigo et Emeraude", "Indigo et Prune", 
                                        "Ebène et Emeraude", "Ebène et Prune", "Pourpre et Emeraude", "Pourpre et Prune", 
                                        "Orchidée et Emeraude", "Orchidée et Prune", "Ivoire et Emeraude", "Ivoire et Prune", 
                                        "Turquoise et Emeraude", "Turquoise et Prune"])

    # Création de l'objet Generations
    generations = Generations()

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

if __name__ == "__main__" :
    creat_generations()