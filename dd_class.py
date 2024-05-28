import random
from collections import defaultdict 

class Dragodinde:
    def __init__(self, id : int, sex: bool, couleur: str, generation: int, arbre_genealogique=None, nombre_reproductions=0):
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
        return self.arbre_genealogique

    def get_nombre_reproductions(self):
        return self.nombre_reproductions

    def __repr__(self):
        return (f"DD{id}: (Sex: {self.sex}, Couleur: {self.couleur}, "
                f"Reproductions: {self.nombre_reproductions}, Généalogie: {self.arbre_genealogique})")

class Elevage:
    def __init__(self):
        self.dragodindes = []

    def add_DD(self, dragodinde:object) :
        self.dragodindes.append(dragodinde)

    def check_mort(self, dragodinde:object):
        if dragodinde.get_nombre_reproductions() >= 20:
            self.dragodindes = [dd for dd in self.dragodindes if dd.id != dragodinde.get_id()]

    def naissance(self, dragodinde:object):
        self.dragodindes.append(dragodinde)

    def check_couleur(couleur_A:str, couleur_B:str) -> bool :
        return True if " et " not in couleur_A and  " et " not in couleur_B else False
    
    def croisement_mono_mono(couleur_A: str, couleur_B: str):
        """
        Croisement : mono couleur (A) X mono couleur (B) :
        (45% couleur (A))(45% couleur (B))(10% bicolor (A/B))
        """
        proba = defaultdict(float)
        proba[couleur_A] += 0.45
        proba[couleur_B] += 0.45
        proba[f"{couleur_A} et {couleur_B}"] += 0.10
        return proba

    def croisement_mono_bi(couleur_A: str, couleur_B: str):
        """
        Croisement : mono couleur (A) X bi couleur (B):
        (50% mono)(50% bicolor)
        """
        proba = defaultdict(float)
        proba[couleur_A] += 0.50
        proba[couleur_B] += 0.50
        return proba

    def croisement_bi_bi(couleur_A: str, couleur_B: str):
        """
        Croisement : bi couleur (A) X bi couleur (B):
        (50% bicolor (A))(50% bi (B))
        """
        proba = defaultdict(float)
        if couleur_A in special_cases and couleur_B in special_cases :
            if special_cases[couleur_A] == special_cases[couleur_B] :
                couleur_speciale = special_cases[couleur_A]
                proba[couleur_speciale] += 0.10
                proba[couleur_A] += 0.45
                proba[couleur_B] += 0.45
        else:
            proba[couleur_A] += 0.50
            proba[couleur_B] += 0.50
        return proba

    def combiner_probabilites(proba1, proba2, poids1, poids2):
        """
        Combine les probabilités de deux dictionnaires en utilisant des poids donnés.
        """
        result = defaultdict(float)
        for couleur, p in proba1.items():
            result[couleur] += p * poids1
        for couleur, p in proba2.items():
            result[couleur] += p * poids2
        return result   
        
    def croisement(self, dinde1:object, dinde2:object) -> dict :
        """
        Appel les autres fonctions en fonction 
        du type de couleur de croisement et de l'ordre de la gealogie :
        génération                   : parents > grand parents > arrière grand parents
        multiplicateur de génération :   50%   >      30%      >       20%   
        Dans le cas ou il manque un parents on a une redistribution des
        probabilité au couches d'en dessous de facon équivalent, ex :
        Pas de arrière grand parents : parent (60%), grand parents (40%)
        """
        couleur_dinde1 = dinde1.get_couleur()
        couleur_dinde2 = dinde2.get_couleur()
        
        # Croisement direct
        if self.check_couleur(couleur_dinde1, couleur_dinde2):
            proba_directe = self.croisement_mono_mono(couleur_dinde1, couleur_dinde2)
        else:
            proba_directe = self.croisement_mono_bi(couleur_dinde1, couleur_dinde2)
        
        # Croisement des parents
        proba_parents = defaultdict(float)
        if dinde1.get_arbre_genealogique() and dinde2.get_arbre_genealogique():
            list_Gcouleur_dinde1 = dinde1.get_parents_and_grandparents()[:2] # Parents only
            list_Gcouleur_dinde2 = dinde2.get_parents_and_grandparents()[:2] # Parents only
            
            for parent1 in list_Gcouleur_dinde1:
                for parent2 in list_Gcouleur_dinde2:
                    if parent1 and parent2:
                        couleur_parent1 = parent1.get_couleur()
                        couleur_parent2 = parent2.get_couleur()
                        if self.check_couleur(couleur_parent1, couleur_parent2):
                            proba_parents = self.combiner_probabilites(proba_parents, self.croisement_mono_mono(couleur_parent1, couleur_parent2), 1.0, 0.5)
                        else:
                            proba_parents = self.combiner_probabilites(proba_parents, self.croisement_mono_bi(couleur_parent1, couleur_parent2), 1.0, 0.5)
        
        # Croisement des grands-parents
        proba_grandparents = defaultdict(float)
        if dinde1.get_arbre_genealogique() and dinde2.get_arbre_genealogique():
            list_Gcouleur_dinde1 = dinde1.get_parents_and_grandparents()[2:6] # Grandparents only
            list_Gcouleur_dinde2 = dinde2.get_parents_and_grandparents()[2:6] # Grandparents only
            
            for gparent1 in list_Gcouleur_dinde1:
                for gparent2 in list_Gcouleur_dinde2:
                    if gparent1 and gparent2:
                        couleur_gparent1 = gparent1.get_couleur()
                        couleur_gparent2 = gparent2.get_couleur()
                        if self.check_couleur(couleur_gparent1, couleur_gparent2):
                            proba_grandparents = self.combiner_probabilites(proba_grandparents, self.croisement_mono_mono(couleur_gparent1, couleur_gparent2), 1.0, 0.3)
                        else:
                            proba_grandparents = self.combiner_probabilites(proba_grandparents, self.croisement_mono_bi(couleur_gparent1, couleur_gparent2), 1.0, 0.3)
        
        # Croisement des arrière-grands-parents
        proba_great_grandparents = defaultdict(float)
        if dinde1.get_arbre_genealogique() and dinde2.get_arbre_genealogique():
            list_AGcouleur_dinde1 = dinde1.get_parents_and_grandparents()[6:] # Great-grandparents only
            list_AGcouleur_dinde2 = dinde2.get_parents_and_grandparents()[6:] # Great-grandparents only
            
            for ggparent1 in list_AGcouleur_dinde1:
                for ggparent2 in list_AGcouleur_dinde2:
                    if ggparent1 and ggparent2:
                        couleur_ggparent1 = ggparent1.get_couleur()
                        couleur_ggparent2 = ggparent2.get_couleur()
                        if self.check_couleur(couleur_ggparent1, couleur_ggparent2):
                            proba_great_grandparents = self.combiner_probabilites(proba_great_grandparents, self.croisement_mono_mono(couleur_ggparent1, couleur_ggparent2), 1.0, 0.2)
                        else:
                            proba_great_grandparents = self.combiner_probabilites(proba_great_grandparents, self.croisement_mono_bi(couleur_ggparent1, couleur_ggparent2), 1.0, 0.2)
        
        # Combinaison des probabilités
        proba_finale = self.combiner_probabilites(proba_directe, proba_parents, 0.5, 0.5)
        proba_finale = self.combiner_probabilites(proba_finale, proba_grandparents, 1.0, 0.3)
        proba_finale = self.combiner_probabilites(proba_finale, proba_great_grandparents, 1.0, 0.2)
        
        return dict(proba_finale)

    def accoupler_naissance(self, male:object, female:object):
        if male and female:
            male.nombre_reproductions += 1
            female.nombre_reproductions += 1
            nouvel_id = len(self.dragodindes) + 1
            ancetres_male = male.arbre_genealogique[:2] 
            ancetres_female = female.arbre_genealogique[:2]
            nouvel_arbre_genealogique = [(male.couleur, female.couleur)] + ancetres_male + ancetres_female
            sexe = random.choice(['M', 'F'])
            couleur = self.choix_croisement(male, female)
            random.choice([male.couleur, female.couleur])  # Simplification de l'héritage de couleur
            nouvelle_dd = Dragodinde(nouvel_id, sexe, couleur, nouvel_arbre_genealogique)
            self.naissance(nouvelle_dd)
            self.check_mort(male)
            self.check_mort(female)

class Genealogie:
    def __init__(self):
        self.parents = [None, None]  # [father, mother]
        self.grandparents = [None, None, None, None]  # [paternal grandfather, paternal grandmother, maternal grandfather, maternal grandmother]
        self.great_grandparents = [None] * 8  # [four pairs of great-grandparents]

    def get_parents_and_grandparents(self) :
        return self.parents, self.grandparents, self.great_grandparents
    
    def set_tree_for_birth(self, father:object, mother:object):
        self.parents = [father.get_couleur(), mother.get_couleur()]

        father_genealogie = father.get_arbre_genealogique()
        if father_genealogie:
            father_parents, father_grandparents = father_genealogie.get_parents_and_grandparents()
            self.grandparents[:2] = father_parents
            if father_grandparents:
                self.great_grandparents[:4] = father_grandparents[:4]

        mother_genealogie = mother.get_arbre_genealogique()
        if mother_genealogie:
            mother_parents, mother_grandparents = mother_genealogie.get_parents_and_grandparents()
            self.grandparents[2:] = mother_parents
            if mother_grandparents:
                self.great_grandparents[4:] = mother_grandparents[4:]

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
        self.generations = []
        self.links = {}

    def add_generation(self, generation):
        self.generations.append(generation)

    def get_generations(self):
        return [str(gen) for gen in self.generations]

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

special_cases = {
    "Rousse et Dorée": "Orchidée",
    "Amande et Dorée": "Ebène",
    "Rousse et Amande": "Pourpre",
    "Indigo et Ebène": "Orchidée",
    "Pourpre et Orchidée": "Turquoise",
    "Indigo et Pourpre": "Ivoire",
    "Ebène et Orchidée": "Turquoise",
    "Ivoire et Turquoise": "Emeraude",
    "Turquoise et Orchidée": "Prune",
    "Pourpre et Ivoire": "Emeraude"
}
