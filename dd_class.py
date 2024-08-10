from collections import defaultdict 
import random 
#from dataclasses import dataclass, field
#from typing import Optional

# @dataclass
class Dragodinde:
    def __init__(self, id : int, sex: str, couleur: str, generation: int, arbre_genealogique=None, nombre_reproductions=0):
        self.id = id
        self.sex = sex
        self.couleur = couleur
        self.generation = generation
        self.arbre_genealogique = arbre_genealogique
        self.nombre_reproductions = nombre_reproductions

        # Initialize arbre_genealogique
        if arbre_genealogique is not None:
            self.arbre_genealogique = arbre_genealogique.update_weights()
        else:
            self.arbre_genealogique = Genealogie(Node(self.couleur, 10/42))

        if self.sex not in ("M", "F"):
            raise ValueError("sex must be 'M' or 'F'")
        
        if self.generation < 0:
            raise ValueError("generation must be a positive integer")

    def get_id(self):
        return self.id

    def get_sex(self):
        return self.sex

    def get_couleur(self):
        return self.couleur

    def get_generation(self):
        return self.generation
    
    def get_arbre_genealogique(self):
        return self.arbre_genealogique
    
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
    def __init__(self, number_generation: int, apprendissage:float, monocolor: bool, colors: list):
        self.number_generation = number_generation
        self.apprendissage = apprendissage
        self.monocolor = monocolor
        self.colors = colors

    def get_number_generation(self):
        return self.number_generation
    
    def get_apprendissage(self):
        return self.apprendissage

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
        raise ValueError("Color not find in the generations object")
    
    def get_apprentissage_by_color(self, color:str) -> float :
        for generation in self.generations:
            if color in generation.get_colors():
                return generation.get_apprendissage()[generation.get_colors().index(color)]
        raise ValueError("Color not find in the generations object")
    
    def get_list_bicolor(self) -> list :
        list_bicolor = []
        for generation in self.generations :
            if not generation.get_monocolor() :
                list_bicolor.extend(generation.get_colors())
        return list_bicolor
    
    def initialize_generations(self):
 
        generations_data = [
            # (generation, monocolor, dict(color: weight))
            (1, True, {"Rousse": 1.0, "Amande": 1.0, "Dorée": 0.2}),
            (2, False, {"Rousse et Amande": 0.8, "Rousse et Dorée": 0.8, "Amande et Dorée": 0.8}),
            (3, True, {"Indigo": 0.8, "Ebène": 0.8}),
            (4, False, {
                "Rousse et Indigo": 0.8, "Rousse et Ebène": 0.8, "Amande et Indigo": 0.8, "Amande et Ebène": 0.8,
                "Dorée et Indigo": 0.8, "Dorée et Ebène": 0.8, "Indigo et Ebène": 0.8
            }),
            (5, True, {"Pourpre": 0.6, "Orchidée": 0.6}),
            (6, False, {
                "Pourpre et Rousse": 0.6, "Orchidée et Rousse": 0.6, "Amande et Pourpre": 0.6, "Amande et Orchidée": 0.6,
                "Dorée et Pourpre": 0.6, "Dorée et Orchidée": 0.6, "Indigo et Pourpre": 0.6, "Indigo et Orchidée": 0.6,
                "Ebène et Pourpre": 0.6, "Ebène et Orchidée": 0.6, "Pourpre et Orchidée": 0.6
            }),
            (7, True, {"Ivoire": 0.6, "Turquoise": 0.6}),
            (8, False, {
                "Ivoire et Rousse": 0.4, "Turquoise et Rousse": 0.4, "Amande et Ivoire": 0.4, "Amande et Turquoise": 0.4,
                "Dorée et Ivoire": 0.4, "Dorée et Turquoise": 0.4, "Indigo et Ivoire": 0.4, "Indigo et Turquoise": 0.4,
                "Ebène et Ivoire": 0.4, "Ebène et Turquoise": 0.4, "Pourpre et Ivoire": 0.4, "Turquoise et Pourpre": 0.4,
                "Ivoire et Orchidée": 0.4, "Turquoise et Orchidée": 0.4, "Ivoire et Turquoise": 0.4
            }),
            (9, True, {"Emeraude": 0.4, "Prune": 0.4}),
            (10, False, {
                "Rousse et Emeraude": 0.2, "Rousse et Prune": 0.2, "Amande et Emeraude": 0.2, "Amande et Prune": 0.2,
                "Dorée et Emeraude": 0.2, "Dorée et Prune": 0.2, "Indigo et Emeraude": 0.2, "Indigo et Prune": 0.2,
                "Ebène et Emeraude": 0.2, "Ebène et Prune": 0.2, "Pourpre et Emeraude": 0.2, "Pourpre et Prune": 0.2,
                "Orchidée et Emeraude": 0.2, "Orchidée et Prune": 0.2, "Ivoire et Emeraude": 0.2, "Ivoire et Prune": 0.2,
                "Turquoise et Emeraude": 0.2, "Turquoise et Prune": 0.2
            })
        ]

        generations = []
        for number, monocolor, color_weights in generations_data:
            colors = list(color_weights.keys())          # Extract the colors (keys) from the dictionary
            apprentissage = list(color_weights.values()) # Extract the weights (values) from the dictionary
            generation = Generation(number, apprentissage, monocolor, colors)
            generations.append(generation)

        return generations

class Node:
    def __init__(self, color=None, weight=None, ancestor_m=None, ancestor_f=None):
        self.color = color
        self.weight = weight
        self.ancestor_m = ancestor_m
        self.ancestor_f = ancestor_f

    def get_color(self):
        return self.color

    def get_ancestor_m(self):
        return self.ancestor_m

    def get_ancestor_f(self):
        return self.ancestor_f

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def __str__(self):
        return (f"color: {self.color}\n"
                f"weight: {self.weight}\n"
                f"ancestor_m: {self.ancestor_m}\n"
                f"ancestor_f: {self.ancestor_f}\n")

# heritage Node ?
class Genealogie:
    def __init__(self, root_node:Node):
        self.root_node = root_node

    def get_node(self) :
        return self.root_node

    def init_weight(self, node, current_level, dic_weight_level):
        if current_level > 3 or node is None:
            return

        node.set_weight(dic_weight_level[current_level])
        parents = [node.get_ancestor_m(), node.get_ancestor_f()]

        for i, parent in enumerate(parents):
            if current_level < 3 :
                if i == 0:
                    node.ancestor_m = parent
                else :
                    node.ancestor_f = parent
            
            self.init_weight(parent, current_level + 1, dic_weight_level)

    def update_weights(self) :
        dic_weight_level = {0: 10/42, 1: 6/42, 2: 3/42, 3: 1/42} # weight
        dump = Node(None, None, self.root_node)
        self.init_weight(self.root_node, 0, dic_weight_level)
        return Genealogie(dump.get_ancestor_m())

    def get_ancestors_at_level(self, node, current_level, level):
        if node is None:
            return []
        if current_level == level:
            return [node.get_color()]
        else:
            ancestors = []
            ancestors += self.get_ancestors_at_level(node.get_ancestor_m(), current_level + 1, level)
            ancestors += self.get_ancestors_at_level(node.get_ancestor_f(), current_level + 1, level)
            return ancestors

    def get_genealogie(self, level):
        return self.get_ancestors_at_level(self.root_node, 0, level)

    def traverse_genealogy(self, node, nodes_list):
        if node is None:
            return
        nodes_list.append(node)
        self.traverse_genealogy(node.get_ancestor_m(), nodes_list)
        self.traverse_genealogy(node.get_ancestor_f(), nodes_list)

    def get_all_nodes(self):
        nodes_list = []
        self.traverse_genealogy(self.root_node, nodes_list)
        return nodes_list
    
    def __str__(self):
        return (f"individu: {self.get_genealogie(0)}\n"
                f"parents: {self.get_genealogie(1)}\n"
                f"grand parents: {self.get_genealogie(2)}\n"
                f"great-grand parents: {self.get_genealogie(3)}")
    
class Elevage:  

    def __init__(self, dragodindes : list) :
        self.dragodindes = dragodindes
        self.generations = Generations()
        self.special_cases = {
            "Rousse et Dorée": ["Ebène", "Orchidée"],
            "Amande et Dorée": ["Indigo", "Ebène"],
            "Rousse et Amande": ["Indigo", "Pourpre"],
            "Indigo et Ebène": ["Orchidée", "Pourpre"],
            "Pourpre et Orchidée": ["Ivoire", "Turquoise"],
            "Indigo et Pourpre": ["Ivoire"],
            "Ebène et Orchidée": ["Turquoise"],
            "Turquoise et Orchidée": ["Prune"],
            "Ivoire et Turquoise": ["Prune", "Emeraude"],
            "Pourpre et Ivoire": ["Emeraude"]
        }

        self.list_bicolor_dd = self.generations.get_list_bicolor()

    def __str__(self):
        return "\n".join(str(dragodinde.get_couleur()) for dragodinde in self.dragodindes)

    def get_dragodindes(self) :
        return self.dragodindes
    
    def get_dd_by_id(self, id: int) :
        for dragodinde in self.dragodindes:
            if dragodinde.get_id() == id :
                return dragodinde
        raise ValueError(f"ID = {id}, not find in the elevage")
    
    def check_mort(self, dragodinde:Dragodinde) :
        if dragodinde.get_nombre_reproductions() >= 20:
            self.dragodindes = [dd for dd in self.dragodindes if dd.id != dragodinde.get_id()]

    def naissance(self, dragodinde:Dragodinde) :
        self.dragodindes.append(dragodinde)

    def has_common_element(self, list1, list2):
        return any(element in list2 for element in list1)
    
    def check_compatibility(self, color_A:str, color_B:str) -> bool :

        # True case : mono-mono / bi-bi with special case
        # bi-bi with special case
        if " et " in color_A and " et " in color_B and (color_A in self.special_cases.keys() and color_B in self.special_cases.keys()):
            if self.has_common_element(self.special_cases[color_A], self.special_cases[color_B]) :
                return True
            
        # mono-mono (but not the same color)
        elif " et " not in color_A and " et " not in color_B :
            if color_A != color_B :
                return True
        
        # False case : mono-bi / bi-mono / bi-bi with no specila case / mono == mono
        return False

    def identify_new_color(self, color_A:str, color_B:str) -> str :
        # Case bi-bi
        if " et " in color_A and " et " in color_B :
            return list(set(self.special_cases[color_A]) & set(self.special_cases[color_B]))[0]
            
        # Case mono-mono
        elif " et " not in color_A and " et " not in color_B :
            
            # Construct the bicolor key
            bicolor_key_1 = f"{color_A} et {color_B}"
            bicolor_key_2 = f"{color_B} et {color_A}"

            # Check if the bicolor combination is in the list
            if bicolor_key_1 in self.list_bicolor_dd:
                return bicolor_key_1
            elif bicolor_key_2 in self.list_bicolor_dd:
                return bicolor_key_2
            else :
                raise ValueError(f"The combinaison of {color_A} and {color_B} didn't match any kind of bicolored dd")
 
        else :
            raise ValueError(f"{color_A} and {color_B} are not suppose to combine here")

    def calcul_PGC(self, apprentissage_value:float, generation:int) -> float :
        return (100*apprentissage_value)/(2-(generation%2))
    
    def calcul_prob_color_imcomp(self, PGC_c1, PGC_c2) -> float :
        return PGC_c1 / (PGC_c1 + PGC_c2)

    def calcul_prob_color_comp(self, PGC_c1, PGC_c2, PGC_c3) -> float :
        return PGC_c1 / (PGC_c1 + PGC_c2 + 0.5 * PGC_c3)

    def calcul_prob_color_new(self, PGC_c1, PGC_c2, PGC_c3) -> float :
        return (0.5 * PGC_c3) / (PGC_c1 + PGC_c2 + 0.5 * PGC_c3)
     
    def crossing_incompatible(self, couleur_A: str, weight_A : float, couleur_B: str, weight_B : float, color_prob : defaultdict):
        """
        Crossing where 2 dd can't create a third one
        """
        if couleur_A != couleur_B :

            pgc_a = self.calcul_PGC(self.generations.get_apprentissage_by_color(couleur_A), self.generations.get_generation_by_color(couleur_A))
            pgc_b = self.calcul_PGC(self.generations.get_apprentissage_by_color(couleur_B), self.generations.get_generation_by_color(couleur_B))
            Proba_a = self.calcul_prob_color_imcomp(pgc_a, pgc_b)
            Proba_b = self.calcul_prob_color_imcomp(pgc_b, pgc_a)
            color_prob[couleur_A] = color_prob.get(couleur_A, 0) + Proba_a * weight_A * weight_B
            color_prob[couleur_B] = color_prob.get(couleur_B, 0) + Proba_b * weight_A * weight_B
    
        else:
            color_prob[couleur_A] = color_prob.get(couleur_A, 0) + 1.0 * weight_A * weight_B

        return color_prob

    def crossing_compatible(self, couleur_A: str, weight_A : float, couleur_B: str, weight_B : float, color_prob : defaultdict):
        """
        Crossing where 2 dd can create a third one
        """
        couleur_C = self.identify_new_color(couleur_A, couleur_B)

        pgc_a = self.calcul_PGC(self.generations.get_apprentissage_by_color(couleur_A), self.generations.get_generation_by_color(couleur_A))
        pgc_b = self.calcul_PGC(self.generations.get_apprentissage_by_color(couleur_B), self.generations.get_generation_by_color(couleur_B))
        pgc_c = self.calcul_PGC(self.generations.get_apprentissage_by_color(couleur_C), self.generations.get_generation_by_color(couleur_C))

        Proba_a = self.calcul_prob_color_comp(pgc_a, pgc_b, pgc_c)
        Proba_b = self.calcul_prob_color_comp(pgc_b, pgc_a, pgc_c)
        Proba_c = self.calcul_prob_color_new(pgc_a, pgc_b, pgc_c)

        color_prob[couleur_A] = color_prob.get(couleur_A, 0) + Proba_a * weight_A * weight_B
        color_prob[couleur_B] = color_prob.get(couleur_B, 0) + Proba_b * weight_A * weight_B
        color_prob[couleur_C] = color_prob.get(couleur_C, 0) + Proba_c * weight_A * weight_B

        return color_prob

    def crossing(self, dinde_m: Dragodinde, dinde_f: Dragodinde) -> dict :

        node_list_dinde_m = dinde_m.get_arbre_genealogique().get_all_nodes()
        node_list_dinde_f = dinde_f.get_arbre_genealogique().get_all_nodes()
        dic_dinde_m = dict()
        dic_dinde_f = dict()
        color_prob = defaultdict(float)

        # Create 2 color dict from both genealogic tree 
        for node_m in node_list_dinde_m :
            color_m, weight_m = node_m.get_color(), node_m.get_weight()
            dic_dinde_m[color_m] = dic_dinde_m.get(color_m, 0) + weight_m 
        
        for node_f in node_list_dinde_f :
            color_f, weight_f = node_f.get_color(), node_f.get_weight()
            dic_dinde_f[color_f] = dic_dinde_f.get(color_f, 0) + weight_f
        
        # Crossing both dic 
        for color_m, weight_m in dic_dinde_m.items() :
            for color_f, weight_f in dic_dinde_f.items() :
                if self.check_compatibility(color_m, color_f):
                    color_prob = self.crossing_compatible(color_m, weight_m, color_f, weight_f, color_prob)
                else:
                    color_prob = self.crossing_incompatible(color_m, weight_m, color_f, weight_f, color_prob)
        
        if not color_prob:
            raise ValueError("Probability color dictionary is empty")
        
        return color_prob

    def choice_color(self, probabilities : float) :
        list_color = list(probabilities.keys())
        list_proba = list(probabilities.values())
        selected_color = random.choices(list_color, weights=list_proba, k=1)[0]
        return selected_color
    
    def get_generation(self, color: str) -> int:
        return self.generations.get_generation_by_color(color)

    def round_dict_values(self, input_dict : dict):
        return {key: round(value*100, 3) for key, value in input_dict.items()}

    def normalise_proba(self, proba_dict : dict) -> dict :
        return {key: value / sum(proba_dict.values()) for key, value in proba_dict.items()}
           
    def accouplement_naissance(self, male: Dragodinde, female: Dragodinde):
        if male is None or female is None:
            raise ValueError("One or both of the Dragodindes do not exist.")

        if male.get_sex() == female.get_sex():
            raise ValueError("Cannot breed dragodindes of the same sex.")

        # Calcul the color probablity dictionnary
        male.add_reproduction()
        female.add_reproduction()
        nouvel_id = len(self.dragodindes) + 1
        sexe = random.choice(['M', 'F'])
        dic_probability = self.crossing(male, female)
        dic_probability = self.round_dict_values(self.normalise_proba(dic_probability))
        couleur = self.choice_color(dic_probability)
        
        # Create an new dd
        generation = self.get_generation(couleur)
        node_parent_m = male.get_arbre_genealogique().get_node()
        node_parent_f = female.get_arbre_genealogique().get_node()
        new_ind = Node(couleur, 0.5, node_parent_m, node_parent_f)
        nouvel_arbre_genealogique = Genealogie(new_ind)
        nouvelle_dd = Dragodinde(nouvel_id, sexe, couleur, generation, nouvel_arbre_genealogique)
        self.naissance(nouvelle_dd)

        self.check_mort(male)
        self.check_mort(female)

        return nouvelle_dd, dic_probability
