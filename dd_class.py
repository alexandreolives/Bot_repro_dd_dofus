import random
from collections import defaultdict 
import numpy as np

"""
import gym
from gym import spaces

class Environnement(gym.Env):
    def __init__(self):
        super(Environnement, self).__init__()
        self.action_space = spaces.Discrete(2)  # Exemple: 2 actions possibles (accouplement A ou B)
        self.observation_space = spaces.Box(low=0, high=1, shape=(10,), dtype=np.float32)  # Exemple: état de 10 dimensions
        self.state = self.reset()
        self.generation = 0
        self.max_generations = 10

    def get_generation(self) :
        return self.generation

    def set_generation(self, actual_generation) :
        self.generation = actual_generation
    
    def step(self, action):
        assert self.action_space.contains(action)
        reward = 0
        done = False

        # Simulez le croisement ici, mettez à jour self.state et reward
        if action > self.generation:
            reward = 1000
            self.generation += 1

        elif action == self.generation:
            reward = 1

        elif action < self.generation-2 :
            reward = -1000

        if self.generation == self.max_generations:
            done = True

        return np.array(self.state), reward, done, {}

    def reset(self):
        self.state = np.random.rand(10)
        self.generation = 0
        return np.array(self.state)

    def render(self, mode='human'):
        print(f"Generation: {self.generation}, State: {self.state}")
"""
class Dragodinde:
    def __init__(self, id : int, sex: str, couleur: str, generation: int, arbre_genealogique=None, nombre_reproductions=0):
        self.id = id
        self.sex = sex
        self.couleur = couleur
        self.generation = generation
        self.arbre_genealogique = arbre_genealogique if arbre_genealogique is not None else Genealogie()
        self.nombre_reproductions = nombre_reproductions

    def get_id(self):
        return self.id

    def get_sex(self):
        return self.sex

    def get_couleur(self):
        return self.couleur

    def get_generation(self):
        return self.generation
    
    def set_arbre_genealogique(self, arbre_genealogique):
        self.arbre_genealogique = arbre_genealogique

    def get_arbre_genealogique(self):
        return self.arbre_genealogique.get_parents_and_grandparents()

    def get_nombre_reproductions(self) :
        return self.nombre_reproductions
    
    def add_reproduction(self):
        self.nombre_reproductions += 1
    
    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Sexe: {self.sex}\n"
                f"Couleur: {self.couleur}\n"
                f"Arbre Généalogique: {self.arbre_genealogique}\n"
                f"Génération: {self.generation}\n"
                f"Nombre de reproductions: {self.nombre_reproductions}\n")

class Generation:
    def __init__(self, number_generation: int, monocolor: bool, colors: list):
        self.number_generation = number_generation
        self.monocolor = monocolor
        self.colors = colors

    def get_number_generation(self):
        return self.number_generation

    def get_monocolor(self):
        return self.monocolor

    def get_colors(self):
        return self.colors
    
class Generations:
    def __init__(self):
        self.generations = self.initialize_generations()

    def get_generations(self):
        return [str(gen) for gen in self.generations]
    
    def get_generation_by_color(self, color: str) -> int:
        for generation in self.generations:
            if color in generation.get_colors():
                return generation.get_number_generation()
        return None
    
    def initialize_generations(self):
        # Data for each generation
        generations_data = [
            (1, True, ["Rousse", "Amande", "Dorée"]),
            (2, False, ["Rousse et Amande", "Rousse et Dorée", "Amande et Dorée"]),
            (3, True, ["Indigo", "Ebène"]),
            (4, False, ["Rousse et Indigo", "Rousse et Ebène", "Amande et Indigo", "Amande et Ebène", 
                        "Dorée et Indigo", "Dorée et Ebène", "Indigo et Ebène"]),
            (5, True, ["Pourpre", "Orchidée"]),
            (6, False, ["Pourpre et Rousse", "Orchidée et Rousse", "Amande et Pourpre", "Amande et Orchidée", 
                        "Dorée et Pourpre", "Dorée et Orchidée", "Indigo et Pourpre", "Indigo et Orchidée", 
                        "Ebène et Pourpre", "Ebène et Orchidée", "Pourpre et Orchidée"]),
            (7, True, ["Ivoire", "Turquoise"]),
            (8, False, ["Ivoire et Rousse", "Turquoise et Rousse", "Amande et Ivoire", "Amande et Turquoise", 
                        "Dorée et Ivoire", "Dorée et Turquoise", "Indigo et Ivoire", "Indigo et Turquoise", 
                        "Ebène et Ivoire", "Ebène et Turquoise", "Pourpre et Ivoire", "Turquoise et Pourpre", 
                        "Ivoire et Orchidée", "Turquoise et Orchidée", "Ivoire et Turquoise"]),
            (9, True, ["Emeraude", "Prune"]),
            (10, False, ["Rousse et Emeraude", "Rousse et Prune", "Amande et Emeraude", "Amande et Prune", 
                         "Dorée et Emeraude", "Dorée et Prune", "Indigo et Emeraude", "Indigo et Prune", 
                         "Ebène et Emeraude", "Ebène et Prune", "Pourpre et Emeraude", "Pourpre et Prune", 
                         "Orchidée et Emeraude", "Orchidée et Prune", "Ivoire et Emeraude", "Ivoire et Prune", 
                         "Turquoise et Emeraude", "Turquoise et Prune"])
        ]

        generations = []
        # Add each generation to the Generations object
        for number, monocolor, colors in generations_data:
            generation = Generation(number, monocolor, colors)
            generations.append(generation)

        return generations

class Elevage:
    def __init__(self, dragodindes:list) :
        self.dragodindes = dragodindes
        self.generations = Generations()
        self.special_cases = {
            "Rousse et Dorée": ["Indigo", "Orchidée"],
            "Amande et Dorée": ["Indigo", "Ebène"],
            "Rousse et Amande": ["Ebène", "Pourpre"],
            "Indigo et Ebène": ["Orchidée", "Pourpre"],
            "Pourpre et Orchidée": ["Ivoire", "Turquoise"],
            "Indigo et Pourpre": ["Ivoire"],
            "Ebène et Orchidée": ["Turquoise"],
            "Turquoise et Orchidée": ["Prune"],
            "Ivoire et Turquoise": ["Prune", "Emeraude"],
            "Pourpre et Ivoire": ["Emeraude"]
        }

    def __str__(self):
        return "\n".join(str(dragodinde) for dragodinde in self.dragodindes)

    def get_dd_by_id(self, id: int) :
        for dragodinde in self.dragodindes:
            if dragodinde.get_id() == id :
                return dragodinde
        return None 
    
    def add_DD(self, dragodinde:Dragodinde) :
        self.dragodindes.append(dragodinde)

    def check_mort(self, dragodinde:Dragodinde) :
        if dragodinde.get_nombre_reproductions() >= 20:
            self.dragodindes = [dd for dd in self.dragodindes if dd.id != dragodinde.get_id()]

    def naissance(self, dragodinde:Dragodinde) :
        self.dragodindes.append(dragodinde)

    def check_couleur(self, couleur_A:str, couleur_B:str) -> bool :
        return True if " et " not in couleur_A and " et " not in couleur_B else False
    
    def croisement_mono_mono(self, couleur_A: str, couleur_B: str):
        """
        Croisement : mono couleur (A) X mono couleur (B) :
        (45% couleur (A))(45% couleur (B))(10% bicolor (A/B))
        """
        proba = defaultdict(float)
        if couleur_A != couleur_B :
            proba[couleur_A] = 0.45
            proba[couleur_B] = 0.45
            proba[f"{couleur_A} et {couleur_B}"] = 0.10

        else :
            proba[couleur_A] = 1.0
        return proba

    def croisement_monobi_bibi(self, couleur_A: str, couleur_B: str):
        """
        Croisement : bi/mono couleur (A) X bi couleur (B):
        (50% bi/monocolor (A))(50% bi (B))
        """
        proba = defaultdict(float)
        if couleur_A in self.special_cases and couleur_B in self.special_cases :
            #Special case where both bicolor dd can try the get a mono color baby
            set1 = set(self.special_cases[couleur_A])
            set2 = set(self.special_cases[couleur_B])
            intersection = set1 & set2
            if intersection :
                proba[intersection.pop()] += 0.10
                proba[couleur_A] += 0.45
                proba[couleur_B] += 0.45
        else:
            #Case momo/bi or bi/bi not special case
            proba[couleur_A] += 0.50
            proba[couleur_B] += 0.50

        return proba

    def combiner_probabilites(self, proba1:float, proba2:float, poids1:float, poids2:float):
        """
        Combine les probabilités de deux dictionnaires en utilisant des poids donnés.
        """
        result = defaultdict(float)
        for couleur, p in proba1.items():
            result[couleur] += p * poids1
        for couleur, p in proba2.items():
            result[couleur] += p * poids2
        return result   
        
    def croisement_parents(self, dinde1: Dragodinde, dinde2: Dragodinde, niveau: int, poids: float):
        """
        Fonction auxiliaire pour gérer le croisement à un certain niveau généalogique.
        """
        proba = defaultdict(float)
        if dinde1.get_arbre_genealogique() and dinde2.get_arbre_genealogique():
            list_couleur_dinde1 = dinde1.get_arbre_genealogique()[niveau]
            list_couleur_dinde2 = dinde2.get_arbre_genealogique()[niveau]
            
            for couleur1, couleur2 in zip(list_couleur_dinde1, list_couleur_dinde2):
                if couleur1 and couleur2:
                    if self.check_couleur(couleur1, couleur2):
                        proba = self.combiner_probabilites(proba, self.croisement_mono_mono(couleur1, couleur2), 1.0, poids)
                    else:
                        proba = self.combiner_probabilites(proba, self.croisement_monobi_bibi(couleur1, couleur2), 1.0, poids)
        return proba
    
    def croisement(self, dinde1: Dragodinde, dinde2: Dragodinde) -> dict :
        """
        Appel les autres fonctions en fonction du type de couleur de croisement et de l'ordre de la généalogie :
        génération                   : parents > grands-parents > arrière-grands-parents
        multiplicateur de génération :   50%   >      30%       >       20%   
        Dans le cas où il manque un parent, on a une redistribution des
        probabilités aux couches d'en dessous de façon équivalente, ex :
        Pas d'arrière-grands-parents : parent (60%), grands-parents (40%)
        """
        
        couleur_dinde1 = dinde1.get_couleur()
        couleur_dinde2 = dinde2.get_couleur()
        
        if self.check_couleur(couleur_dinde1, couleur_dinde2):
            proba_directe = self.croisement_mono_mono(couleur_dinde1, couleur_dinde2)
        else:
            proba_directe = self.croisement_monobi_bibi(couleur_dinde1, couleur_dinde2)
        
        proba_parents = self.croisement_parents(dinde1, dinde2, 0, 0.5)
        proba_grandparents = self.croisement_parents(dinde1, dinde2, 1, 0.3)
        proba_great_grandparents = self.croisement_parents(dinde1, dinde2, 2, 0.2)

        total_weight = 1.0
        combined_probabilities = proba_directe
        
        if proba_parents:
            combined_probabilities = self.combiner_probabilites(combined_probabilities, proba_parents, total_weight, 0.5)
            total_weight += 0.5
        
        if proba_grandparents:
            # Adjust weight for grandparents if great-grandparents are missing
            adjusted_weight_grandparents = 0.3 if proba_great_grandparents else 0.5
            combined_probabilities = self.combiner_probabilites(combined_probabilities, proba_grandparents, total_weight, adjusted_weight_grandparents)
            total_weight += adjusted_weight_grandparents

        if proba_great_grandparents:
            combined_probabilities = self.combiner_probabilites(combined_probabilities, proba_great_grandparents, total_weight, 0.2)
            total_weight += 0.2
        
        # Normalize the combined probabilities to ensure they sum to 1
        total_prob_sum = sum(combined_probabilities.values())
        normalized_probabilities = {key: value / total_prob_sum for key, value in combined_probabilities.items()}
        
        return dict(normalized_probabilities)
    
    def choice_color(self, probabilities) :
        # Liste des événements et des poids correspondants
        events = list(probabilities.keys())
        weights = list(probabilities.values())
        selected_event = random.choices(events, weights=weights, k=1)[0]
        return selected_event
    
    def get_generation(self, color: str) -> int:
        return self.generations.get_generation_by_color(color)

    def check_proba(self, dict_proba:dict) :
        if sum(dict_proba.values()) != 1.0 :
            raise ValueError("Error : The sum of dict_prob isn't equal to 1")

    def accouplement_naissance(self, male:Dragodinde, female:Dragodinde) -> Dragodinde :
        if male and female :
            if male.get_sex() != female.get_sex() :
                male.add_reproduction()
                female.add_reproduction()
                nouvel_id = len(self.dragodindes) + 1
                ancetres_gparent = male.get_arbre_genealogique()[0] + female.get_arbre_genealogique()[0]
                print("ancetres_gparent : ", ancetres_gparent)

                ancetres_ggparent = male.get_arbre_genealogique()[1] + female.get_arbre_genealogique()[1]
                print("ancetres_ggparent : ", ancetres_ggparent)

                nouvel_arbre_genealogique = Genealogie([male.couleur, female.couleur], ancetres_gparent , ancetres_ggparent)
                print("nouvel_arbre_genealogique : ", nouvel_arbre_genealogique)

                sexe = random.choice(['M', 'F'])
                dic_probability = self.croisement(male, female)
                print("dic probabilité : ", dic_probability)
                self.check_proba(dic_probability)

                couleur = self.choice_color(dic_probability)
                generation = self.get_generation(couleur)

                nouvelle_dd = Dragodinde(nouvel_id, sexe, couleur, generation, nouvel_arbre_genealogique)
                self.naissance(nouvelle_dd)
                self.check_mort(male)
                self.check_mort(female)

                return nouvelle_dd, dic_probability
            
            else :
                raise ValueError("Cannot breed dragodindes of the same sex.")        
        else :
            raise ValueError("Dragodindes not exist")

class Genealogie:
    def __init__(self, parents=[None, None], 
                 grandparents=[None, None, None, None],
                 great_grandparents=[None] * 8) :
        
        self.parents = parents  # [father, mother]
        self.grandparents = grandparents  # [paternal grandfather, paternal grandmother, maternal grandfather, maternal grandmother]
        self.great_grandparents = great_grandparents # [four pairs of great-grandparents]

    def __str__(self) :
        return (f"parents: {self.parents}\n"
                f"grand parents: {self.grandparents}\n"
                f"grand grand parents: {self.great_grandparents}")
    
    def get_parents_and_grandparents(self) :
        return [self.parents, self.grandparents, self.great_grandparents]