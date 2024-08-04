import unittest
import dd_class

class TestGenealogie(unittest.TestCase):

    def setUp(self):
        # Level 3 (Great Grandparents)
        self.ggp1 = dd_class.Node("ggp1", 0)
        self.ggp2 = dd_class.Node("ggp2", 0)
        self.ggp3 = None
        self.ggp4 = None

        self.ggp5 = None
        self.ggp6 = None
        self.ggp7 = None
        self.ggp8 = None

        # Level 2 (Grandparents)
        self.gp1 = dd_class.Node("gp1", 0, ancestor_m=self.ggp1, ancestor_f=self.ggp2)
        self.gp2 = dd_class.Node("gp2", 0, ancestor_m=self.ggp3, ancestor_f=self.ggp4)
        self.gp3 = None
        self.gp4 = None

        # Level 1 (Parents)
        self.p1 = dd_class.Node("p1", 0, ancestor_m=self.gp1, ancestor_f=self.gp2)
        self.p2 = None

        # Root
        self.root = dd_class.Node("root", 0, ancestor_m=self.p1, ancestor_f=self.p2)
        self.genealogy = dd_class.Genealogie(self.root)

    def test_init_weight(self):
        self.genealogy.update_weights_and_colors()

        print(self.genealogy.__str__())
        all_nodes = self.genealogy.get_all_nodes()
        initiated_nodes = [node.get_weight() for node in all_nodes]
        expected_weights = [0.5, 0.125, 0.0375, 0.0125, 0.0125, 0.0375, 0.0125, 0.0125, 0.125, 0.0375, 0.0125, 0.0125, 0.0375, 0.0125, 0.0125]
        self.assertEqual(initiated_nodes, expected_weights)

if __name__ == "__main__":
    unittest.main()

# def creat_elevage() :

#     arbre_1 = dd_class.Genealogie(["Ebène", "Amande"])
#     arbre_2 = dd_class.Genealogie(["Indigo", "Rousse"])

#     dd_1 = dd_class.Dragodinde(1, "M", "Amande", 1, arbre_1)
#     dd_2 = dd_class.Dragodinde(2, "F", "Rousse", 1, arbre_2)

#     elevage = dd_class.Elevage([dd_1, dd_2])
#     return elevage

# if __name__ == "__main__" :
#     elevage = creat_elevage()
#     new_dd, dic_probability = elevage.accouplement_naissance(elevage.get_dd_by_id(1), elevage.get_dd_by_id(2))
#     print(str(new_dd))
#     print("dic_probability : ", dic_probability)

#     expected_probability = {
#         "Rousse": 37,
#         "Amande": 37,
#         "Indigo": 8,
#         "Ebène": 8,
#         "Amande et Rousse": 6,
#         "Amande et Indigo": 1,
#         "Ebène et Rousse": 1,
#         "Indigo et Ebène": 0
#     }

#     Convert probabilities to percentages if needed
#     dic_probability = {k: v * 100 for k, v in dic_probability.items()}

#     Ensure the keys are properly formatted to match expected keys
#     formatted_dic_probability = {k.split(' ')[-1]: v for k, v in dic_probability.items()}

#     assert formatted_dic_probability == expected_probability, f"Probabilities do not match. Expected: {expected_probability}, but got: {formatted_dic_probability}"
#     print("Probabilities match expected values.")
