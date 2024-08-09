from dd_class import Elevage
from dd_class import Dragodinde
import random
import time 

class Random_crossing :
    def __init__(self) :
        self.elevage = self.create_elevage()

    def __str__(self) :
        return (f"{self.elevage}")
    
    def get_length_elevage(self) :
        return len(self.elevage.get_dragodindes())
    
    def get_better_generation(self) :
        better_generation = 1
        for dragodinde in self.elevage.get_dragodindes() :
            generation = dragodinde.get_generation()
            if generation > better_generation :
                better_generation = generation
        
        return better_generation

    def get_dd_better_generation(self, dragodindes) :
        better_generation = 1
        index_best_dd = 0
        for idx, dragodinde in enumerate(dragodindes) :
            generation  = dragodinde.get_generation()
            if generation > better_generation :
                better_generation = generation
                index_best_dd = idx
        return dragodindes[index_best_dd]

    def create_elevage(self):

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
    
    def random_crosing_better_gen(self):
        males = [dd for dd in self.elevage.get_dragodindes() if dd.get_sex() == "M"]
        females = [dd for dd in self.elevage.get_dragodindes() if dd.get_sex() == "F"]

        if not males or not females:
            raise ValueError("No suitable pairs for crossing.")

        # Take the best generation
        male = self.get_dd_better_generation(males)
        female = self.get_dd_better_generation(females)

        if male.get_generation() != female.get_generation():
            male = random.choice(males)
            female = random.choice(females)
        
        while male.get_couleur() == female.get_couleur() :
            male = random.choice(males)
            female = random.choice(females)

        # Assuming accouplement_naissance is a method that performs crossing and returns probabilities
        nouvelle_dd, _ = self.elevage.accouplement_naissance(male, female)

        return nouvelle_dd.get_generation()

    def random_crosing(self):
        males = [dd for dd in self.elevage.get_dragodindes() if dd.get_sex() == "M"]
        females = [dd for dd in self.elevage.get_dragodindes() if dd.get_sex() == "F"]

        if not males or not females:
            raise ValueError("No suitable pairs for crossing.")

        male = random.choice(males)
        female = random.choice(females)

        # Assuming accouplement_naissance is a method that performs crossing and returns probabilities
        nouvelle_dd, _ = self.elevage.accouplement_naissance(male, female)

        return nouvelle_dd.get_generation()
    
if __name__ == "__main__" :

    start_time = time.time()
    elevage = Random_crossing()
    better_generation = 1
    crosing_number = 10000
    for i in range(crosing_number) :
        higher_generation = elevage.random_crosing_better_gen()
        if higher_generation > better_generation :
            better_generation = higher_generation
    
    end_time = time.time()
    print(f"Length of the evelage : {elevage.get_length_elevage()}")
    print(f"Better generation so far : {better_generation}")
    print(f"Time taken to compute {crosing_number} crossing : {end_time - start_time:.6f} seconds")
