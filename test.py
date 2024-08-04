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
        all_nodes = self.genealogy.get_all_nodes()
        initiated_nodes = [node.get_weight() for node in all_nodes]
        expected_weights = [0.5, 0.125, 0.0375, 0.0125, 0.0125, 0.0375, 0.0125, 0.0125, 0.125, 0.0375, 0.0125, 0.0125, 0.0375, 0.0125, 0.0125]
        self.assertEqual(initiated_nodes, expected_weights)

class TestCrosing(unittest.TestCase):

    def setUp(self) :

        # Mono Amande
        self.gp1 = dd_class.Node("Ebène")
        self.gp2 = dd_class.Node("Amande")
        self.p1 = dd_class.Node("Amande", 0.5, self.gp1, self.gp2)
        self.genealogie_1 = dd_class.Genealogie(self.p1)
        self.genealogie_1.update_weights_and_colors()
        self.dd_1 = dd_class.Dragodinde(1, "M", "Amande", 1, self.genealogie_1)

        # Mono Rousse
        self.gp3 = dd_class.Node("Indigo", 0.)
        self.gp4 = dd_class.Node("Rousse")
        self.p2 = dd_class.Node("Rousse", 0.5, self.gp3, self.gp4)
        self.genealogie_2 = dd_class.Genealogie(self.p2)
        self.genealogie_2.update_weights_and_colors()
        self.dd_2 = dd_class.Dragodinde(2, "F", "Rousse", 1, self.genealogie_2)

        # Bi Rousse et Amande
        self.gp3 = dd_class.Node("Indigo", 0.)
        self.gp4 = dd_class.Node("Rousse")
        self.p2 = dd_class.Node("Rousse", 0.5, self.gp3, self.gp4)
        self.genealogie_2 = dd_class.Genealogie(self.p2)
        self.genealogie_2.update_weights_and_colors()
        self.dd_2 = dd_class.Dragodinde(2, "F", "Rousse", 1, self.genealogie_2)

        # Bi Pourpre et Orchidée  
        self.gp3 = dd_class.Node("Indigo", 0.)
        self.gp4 = dd_class.Node("Rousse")
        self.p2 = dd_class.Node("Rousse", 0.5, self.gp3, self.gp4)
        self.genealogie_2 = dd_class.Genealogie(self.p2)
        self.genealogie_2.update_weights_and_colors()
        self.dd_2 = dd_class.Dragodinde(2, "F", "Rousse", 1, self.genealogie_2)

        self.elevage = dd_class.Elevage([self.dd_1, self.dd_2])

    def test_crosing_mono(self):
        _, dic_probability = self.elevage.accouplement_naissance(self.elevage.get_dd_by_id(1), self.elevage.get_dd_by_id(2))
        expected_probability = {
                "Rousse": 33.75,
                "Amande": 33.75,
                "Indigo": 11.25,
                "Ebène": 11.25,
                "Rousse et Amande": 5.62,
                "Amande et Indigo": 1.87,
                "Rousse et Ebène": 1.87,
                "Indigo et Ebène": 0.63
            }

        print("dic_probability : ", dic_probability)

        # Convert probabilities to percentages if needed
        dic_probability = {k: v * 100 for k, v in dic_probability.items()}

        print("formatted_dic_probability : ", dic_probability)
        self.assertEqual(dic_probability, expected_probability)

if __name__ == "__main__":
    unittest.main()
