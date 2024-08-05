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
        expected_weights = [10, 6, 3, 1, 1, 3, 1, 1, 6, 3, 1, 1, 3, 1, 1]
        self.assertEqual(initiated_nodes, expected_weights)

class TestCrosing(unittest.TestCase):

    def setUp(self) :

        #                    id  sex   color  generation   root
        # dd_class.Dragodinde(1, "M", "Rousse", 1, self.genealogie_s1)

        # simple mono Rousse
        self.dd_s1 = dd_class.Dragodinde(100, "M", "Rousse", 1)
        #print("self.dd_s1 : ", self.dd_s1)

        # simple bi Pourpre et Ivoire
        self.dd_s2 = dd_class.Dragodinde(101, "F", "Pourpre et Ivoire", 8)

        # # Mono Amande
        # self.gp1 = dd_class.Node("Ebène")
        # self.gp2 = dd_class.Node("Amande")
        # self.p1 = dd_class.Node("Amande", 0.5, self.gp1, self.gp2)
        # self.genealogie_1 = dd_class.Genealogie(self.p1)
        # self.genealogie_1.update_weights_and_colors()
        # self.dd_1 = dd_class.Dragodinde(1, "M", "Amande", 1, self.genealogie_1)

        # # Mono Rousse
        # self.gp3 = dd_class.Node("Indigo")
        # self.gp4 = dd_class.Node("Rousse")
        # self.p2 = dd_class.Node("Rousse", 0.5, self.gp3, self.gp4)
        # self.genealogie_2 = dd_class.Genealogie(self.p2)
        # self.genealogie_2.update_weights_and_colors()
        # self.dd_2 = dd_class.Dragodinde(2, "F", "Rousse", 1, self.genealogie_2)

        # # Bi Rousse et Amande
        # self.ggp1 = dd_class.Node("Dorée et Orchidée")
        # self.ggp2 = dd_class.Node("Orchidée et Rousse")
        # self.ggp3 = dd_class.Node("Rousse et Ebène")
        # self.ggp4 = dd_class.Node("Turquoise et Rousse")

        # self.gp5 = dd_class.Node("Rousse et Prune", None, self.ggp1, self.ggp2)
        # self.gp6 = dd_class.Node("Ebène et Ivoire", None, self.ggp3, self.ggp4)
        # self.p3 = dd_class.Node("Rousse et Pourpre", None, self.gp5, self.gp6)

        # self.gp7 = dd_class.Node("Indigo et Orchidée")
        # self.gp8 = dd_class.Node("Amande et Turquoise")
        # self.p4 = dd_class.Node("Amande et Indigo", None, self.gp7, self.gp8)

        # self.ind_1 = dd_class.Node("Rousse et Amande", None, self.p3, self.p4)
        # self.genealogie_3 = dd_class.Genealogie(self.ind_1)
        # self.genealogie_3.update_weights_and_colors()

        # self.dd_3 = dd_class.Dragodinde(3, "M", "Rousse et Amande", 2, self.genealogie_3)

        # # Bi Pourpre et Orchidée  
        # self.ggp5 = dd_class.Node("Rousse et Ebène")
        # self.ggp6 = dd_class.Node("Turquoise et Rousse")
        # self.ggp7 = dd_class.Node("Rousse et Prune")
        # self.ggp8 = dd_class.Node("Dorée et Indigo")

        # self.gp9 = dd_class.Node("Dorée et Emeraude", None, self.ggp5, self.ggp6)
        # self.gp10 = dd_class.Node("Orchidée et Emeraude", None, self.ggp7, self.ggp8)
        # self.p5 = dd_class.Node("Indigo et Ebène", None, self.gp9, self.gp10)

        # self.gp11 = dd_class.Node("Amande et Ivoire")
        # self.gp12 = dd_class.Node("Indigo et Ivoire")        
        # self.p6 = dd_class.Node("Ivoire et Prune", None, self.gp11, self.gp12)

        # self.ind_2 = dd_class.Node("Pourpre et Orchidée", None, self.p5, self.p6)
        # self.genealogie_4 = dd_class.Genealogie(self.ind_2)
        # self.genealogie_4.update_weights_and_colors()

        # self.dd_4 = dd_class.Dragodinde(4, "F", "Pourpre et Orchidée", 6, self.genealogie_4)

        #self.elevage = dd_class.Elevage([self.dd_1, self.dd_2, self.dd_3, self.dd_4, self.dd_s1, self.dd_s2])
        self.elevage = dd_class.Elevage([self.dd_s1, self.dd_s2])

    # def uni_test_bad_crosing(self):
    #     with self.assertRaises(ValueError) as context:
    #         self.elevage.accouplement_naissance(self.elevage.get_dd_by_id(1), self.elevage.get_dd_by_id(3))

    #     self.assertEqual(str(context.exception), "Cannot breed dragodindes of the same sex.")

    # def test_crosing_mono_mono(self):
    #     _, dic_probability = self.elevage.accouplement_naissance(self.elevage.get_dd_by_id(1), self.elevage.get_dd_by_id(2))
    #     expected_probability = {
    #             "Rousse": 33.75,
    #             "Amande": 33.75,
    #             "Indigo": 11.25,
    #             "Ebène": 11.25,
    #             "Rousse et Amande": 5.62,
    #             "Amande et Indigo": 1.87,
    #             "Rousse et Ebène": 1.87,
    #             "Indigo et Ebène": 0.63
    #         }

    #     dic_probability = {k: v * 100 for k, v in dic_probability.items()}

    #     print("dic_probability mono-mono: ", dic_probability, '\n')
    #     self.assertEqual(dic_probability, expected_probability)
    
    # def test_crosing_mono_bi(self):
    #     _, dic_probability = self.elevage.accouplement_naissance(self.elevage.get_dd_by_id(1), self.elevage.get_dd_by_id(4))
    #     expected_probability = {
    #             "test" : 1
    #         }

    #     print("dic_probability mono-bi : ", dic_probability, '\n')

    #     dic_probability = {k: v * 100 for k, v in dic_probability.items()}
    #     self.assertEqual(dic_probability, expected_probability)
    
    # def test_crosing_bi_bi(self):
    #     _, dic_probability = self.elevage.accouplement_naissance(self.elevage.get_dd_by_id(3), self.elevage.get_dd_by_id(4))
    #     expected_probability = {
    #             "test" : 1
    #         }
        
    #     print("dic_probability bi-bi : ", dic_probability, '\n')

    #     dic_probability = {k: v * 100 for k, v in dic_probability.items()}
    #     self.assertEqual(dic_probability, expected_probability)

    def test_crosing_simple_mono_bi(self):
        _, dic_probability = self.elevage.accouplement_naissance(self.elevage.get_dd_by_id(100), self.elevage.get_dd_by_id(101))
        expected_probability = {
                "Rousse" : 83.334,
                "Pourpre et Ivoire" : 16.667
            }
        
        print("dic_probability simple mono-bi : ", dic_probability, '\n')

        dic_probability = {k: v * 100 for k, v in dic_probability.items()}
        self.assertEqual(dic_probability, expected_probability)

if __name__ == "__main__":
    unittest.main()
