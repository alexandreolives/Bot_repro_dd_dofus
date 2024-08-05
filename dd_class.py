from collections import defaultdict 
import random 

class Dragodinde:
    def __init__(self, id : int, sex: str, couleur: str, generation: int, arbre_genealogique=None, nombre_reproductions=0):
        self.id = id
        self.sex = sex
        self.couleur = couleur
        self.generation = generation
        self.arbre_genealogique = arbre_genealogique if arbre_genealogique is not None else Genealogie(Node(couleur, 10)).update_weights_and_colors()
        self.nombre_reproductions = nombre_reproductions

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
                return generation.get_apprendissage()
        raise ValueError("Color not find in the generations object")
    
    def initialize_generations(self):

        generations_data = [
            (1, True, ["Rousse", "Amande", "Dorée"], 0.2),
            (2, False, ["Rousse et Amande", "Rousse et Dorée", "Amande et Dorée"], 0.25),
            (3, True, ["Indigo", "Ebène"], 0.25),
            (4, False, ["Rousse et Indigo", "Rousse et Ebène", "Amande et Indigo", "Amande et Ebène", 
                        "Dorée et Indigo", "Dorée et Ebène", "Indigo et Ebène"], 0.25),
            (5, True, ["Pourpre", "Orchidée"], 0.33),
            (6, False, ["Pourpre et Rousse", "Orchidée et Rousse", "Amande et Pourpre", "Amande et Orchidée", 
                        "Dorée et Pourpre", "Dorée et Orchidée", "Indigo et Pourpre", "Indigo et Orchidée", 
                        "Ebène et Pourpre", "Ebène et Orchidée", "Pourpre et Orchidée"], 0.33),
            (7, True, ["Ivoire", "Turquoise"], 0.33),
            (8, False, ["Ivoire et Rousse", "Turquoise et Rousse", "Amande et Ivoire", "Amande et Turquoise", 
                        "Dorée et Ivoire", "Dorée et Turquoise", "Indigo et Ivoire", "Indigo et Turquoise", 
                        "Ebène et Ivoire", "Ebène et Turquoise", "Pourpre et Ivoire", "Turquoise et Pourpre", 
                        "Ivoire et Orchidée", "Turquoise et Orchidée", "Ivoire et Turquoise"], 0.5),
            (9, True, ["Emeraude", "Prune"], 0.5),
            (10, False, ["Rousse et Emeraude", "Rousse et Prune", "Amande et Emeraude", "Amande et Prune", 
                         "Dorée et Emeraude", "Dorée et Prune", "Indigo et Emeraude", "Indigo et Prune", 
                         "Ebène et Emeraude", "Ebène et Prune", "Pourpre et Emeraude", "Pourpre et Prune", 
                         "Orchidée et Emeraude", "Orchidée et Prune", "Ivoire et Emeraude", "Ivoire et Prune", 
                         "Turquoise et Emeraude", "Turquoise et Prune"], 1.0)
        ]
        generations = []

        for number, monocolor, colors, apprentissage in generations_data:
            generation = Generation(number, apprentissage, monocolor, colors)
            generations.append(generation)

        return generations
    
class Elevage:  

    def __init__(self, dragodindes : list) :
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

        self.list_bicolor_dd = [
            "Rousse et Amande", "Rousse et Dorée", "Amande et Dorée",
            "Rousse et Indigo", "Rousse et Ebène", "Amande et Indigo", "Amande et Ebène",
            "Dorée et Indigo", "Dorée et Ebène", "Indigo et Ebène",
            "Pourpre et Rousse", "Orchidée et Rousse", "Amande et Pourpre", "Amande et Orchidée",
            "Dorée et Pourpre", "Dorée et Orchidée", "Indigo et Pourpre", "Indigo et Orchidée",
            "Ebène et Pourpre", "Ebène et Orchidée", "Pourpre et Orchidée",
            "Ivoire et Rousse", "Turquoise et Rousse", "Amande et Ivoire", "Amande et Turquoise",
            "Dorée et Ivoire", "Dorée et Turquoise", "Indigo et Ivoire", "Indigo et Turquoise",
            "Ebène et Ivoire", "Ebène et Turquoise", "Pourpre et Ivoire", "Turquoise et Pourpre",
            "Ivoire et Orchidée", "Turquoise et Orchidée", "Ivoire et Turquoise",
            "Rousse et Emeraude", "Rousse et Prune", "Amande et Emeraude", "Amande et Prune",
            "Dorée et Emeraude", "Dorée et Prune", "Indigo et Emeraude", "Indigo et Prune",
            "Ebène et Emeraude", "Ebène et Prune", "Pourpre et Emeraude", "Pourpre et Prune",
            "Orchidée et Emeraude", "Orchidée et Prune", "Ivoire et Emeraude", "Ivoire et Prune",
            "Turquoise et Emeraude", "Turquoise et Prune"
        ]

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
    
    def calcul_PGC(self, apprentissage_value:float, generation:int) -> float :
        return (100*apprentissage_value)/(2-(generation%2))
    
    def calcul_prob_color(self, PGC_c1, PGC_c2) -> float :
        return PGC_c1 / (PGC_c1 + PGC_c2)
    
    def croisement_mono_mono(self, couleur_A: str, weight_A : float, couleur_B: str, weight_B : float, color_prob : defaultdict):
        """
        Croisement : mono couleur (A) X mono couleur (B) :
        (45% couleur (A))(45% couleur (B))(10% bicolor (A/B))
        """
        if couleur_A != couleur_B :

            pgc_a = self.calcul_PGC(self.generations.get_apprentissage_by_color(couleur_A), self.generations.get_generation_by_color(couleur_A))
            pgc_b = self.calcul_PGC(self.generations.get_apprentissage_by_color(couleur_B), self.generations.get_generation_by_color(couleur_B))
            Proba_a = self.calcul_prob_color(pgc_a, pgc_b)
            Proba_b = self.calcul_prob_color(pgc_b, pgc_a)
            color_prob[couleur_A] = color_prob.get(couleur_A, 0) + Proba_a * weight_A * weight_B
            color_prob[couleur_B] = color_prob.get(couleur_B, 0) + Proba_b * weight_A * weight_B
            # color_prob[couleur_A] = color_prob.get(couleur_A, 0) + 0.45 * weight_A * weight_B
            # color_prob[couleur_B] = color_prob.get(couleur_B, 0) + 0.45 * weight_A * weight_B
            
            # Construct the bicolor key
            bicolor_key_1 = f"{couleur_A} et {couleur_B}"
            bicolor_key_2 = f"{couleur_B} et {couleur_A}"

            # Check if the bicolor combination is in the list
            if bicolor_key_1 in self.list_bicolor_dd:
                color_prob[bicolor_key_1] = color_prob.get(bicolor_key_1, 0) + 0.10 * weight_A * weight_B
            elif bicolor_key_2 in self.list_bicolor_dd:
                color_prob[bicolor_key_2] = color_prob.get(bicolor_key_2, 0) + 0.10 * weight_A * weight_B
            else :
                raise ValueError(f"The combinaison of {couleur_A} and {couleur_B} didn't match any kind of bicolored dd")
        else:
            color_prob[couleur_A] = color_prob.get(couleur_A, 0) + 1.0 * weight_A * weight_B

        return color_prob

    def croisement_monobi_bibi(self, couleur_A: str, weight_A : float, couleur_B: str, weight_B : float, color_prob : defaultdict):
        """
        Croisement : bi/mono couleur (A) X bi couleur (B):
        (50% bi/monocolor (A))(50% bi (B))
        """
        # Special case where both bicolor dd can try the get a mono color baby
        if couleur_A in self.special_cases and couleur_B in self.special_cases :

            set1 = set(self.special_cases[couleur_A])
            set2 = set(self.special_cases[couleur_B])
            intersection = set1 & set2

            if intersection :
                color_prob[next(iter(intersection))] = color_prob.get(next(iter(intersection)), 0) + 0.10 * weight_A * weight_B
                color_prob[couleur_A] = color_prob.get(couleur_A, 0) + 0.45 * weight_A * weight_B
                color_prob[couleur_B] = color_prob.get(couleur_B, 0) + 0.45 * weight_A * weight_B
                return color_prob

        color_prob[couleur_A] = color_prob.get(couleur_A, 0) + 0.50 * weight_A * weight_B
        color_prob[couleur_B] = color_prob.get(couleur_B, 0) + 0.50 * weight_A * weight_B

        return color_prob

    def croisement(self, dinde_m: Dragodinde, dinde_f: Dragodinde) -> dict :
        
        node_list_dinde_m = dinde_m.get_arbre_genealogique().get_all_nodes()
        node_list_dinde_f = dinde_f.get_arbre_genealogique().get_all_nodes()
        dic_dinde_m = dict()
        dic_dinde_f = dict()
        color_prob = defaultdict(float)

        for node_m, node_f in zip(node_list_dinde_m, node_list_dinde_f) :
            color_m, weight_m = node_m.get_color(), node_m.get_weight()
            color_f, weight_f = node_f.get_color(), node_f.get_weight()

            dic_dinde_m[color_m] = dic_dinde_m.get(color_m, 0) + (weight_m / 42)
            dic_dinde_f[color_f] = dic_dinde_f.get(color_f, 0) + (weight_f / 42)

        # Do crossing
        for color_m, weight_m in dic_dinde_m.items() :
            for color_f, weight_f in dic_dinde_f.items() :
                if self.check_couleur(color_m, color_f):
                    color_prob = self.croisement_mono_mono(color_m, weight_m, color_f, weight_f, color_prob)
                else:
                    color_prob = self.croisement_monobi_bibi(color_m, weight_m, color_f, weight_f, color_prob)
        
        if not color_prob:
            raise ValueError("Probability color dictionary is empty")
        
        return color_prob

    def choice_color(self, probabilities) :
        list_color = list(probabilities.keys())
        list_proba = list(probabilities.values())
        selected_color = random.choices(list_color, weights=list_proba, k=1)[0]
        
        return selected_color
    
    def get_generation(self, color: str) -> int:
        return self.generations.get_generation_by_color(color)

    def round_dict_values(self, input_dict):
        return {key: round(value, 4) for key, value in input_dict.items()}

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
        dic_probability = self.round_dict_values(self.croisement(male, female))
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

class Node:
    def __init__(self, color=None, weight=None, ancestor_m=None, ancestor_f=None):
        self.color = color
        self.weight = weight
        self.ancestor_m = ancestor_m
        self.ancestor_f = ancestor_f

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_ancestor_m(self):
        return self.ancestor_m

    def get_ancestor_f(self):
        return self.ancestor_f

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight
    
    def __str__(self):
        return (f"color: {self.color}\n"
                f"weight: {self.weight}\n"
                f"ancestor_m: {self.ancestor_m}\n"
                f"ancestor_f: {self.ancestor_f}\n")

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
            if parent is None and current_level < 3:
                parent = Node(node.get_color(), dic_weight_level[current_level+1])
                if i == 0:
                    node.ancestor_m = parent
                else:
                    node.ancestor_f = parent
            self.init_weight(parent, current_level + 1, dic_weight_level)

    def update_weights_and_colors(self):
        dic_weight_level = {0: 10, 1: 6, 2: 3, 3: 1} # weight
        self.init_weight(self.root_node, 0, dic_weight_level)

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
    