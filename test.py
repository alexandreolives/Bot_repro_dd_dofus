import unittest
import dd_class

# Website to generated test : https://felis-silvestris.lescigales.org/
class TestGenealogie(unittest.TestCase):

    def setUp(self):
        # Level 3 (Great Grandparents)
        self.ggp1 = dd_class.Node("ggp1", 0)
        self.ggp2 = dd_class.Node("ggp2", 0)

        # Level 2 (Grandparents)
        self.gp1 = dd_class.Node("gp1", 0, ancestor_m=self.ggp1, ancestor_f=self.ggp2)
        self.gp2 = dd_class.Node("gp2", 0)

        # Level 1 (Parents)
        self.p1 = dd_class.Node("p1", 0, ancestor_m=self.gp1, ancestor_f=self.gp2)

        # Root
        self.root = dd_class.Node("root", 0, ancestor_m=self.p1)
        self.genealogy = dd_class.Genealogie(self.root)

    def test_init_weight(self):
        self.genealogy.update_weights()
        all_nodes = self.genealogy.get_all_nodes()
        initiated_nodes = [node.get_weight() for node in all_nodes]
        expected_weights = [10/42, 6/42, 3/42, 1/42, 1/42, 3/42]
        self.assertEqual(initiated_nodes, expected_weights)

class TestCrosing(unittest.TestCase):

    def setUp(self) :
        self.maxDiff = None

        #                    id  sex   color  generation   root
        # dd_class.Dragodinde(1, "M", "Rousse", 1, self.genealogie_s1)

        # simple mono
        self.dd_sm1 = dd_class.Dragodinde(100, "M", "Rousse", 1)
        self.dd_sm2 = dd_class.Dragodinde(101, "F", "Amande", 1)

        # simple bi 
        self.dd_sb1 = dd_class.Dragodinde(200, "M", "Indigo et Orchidée", 6)
        self.dd_sb2 = dd_class.Dragodinde(201, "F", "Pourpre et Ivoire", 8)

        # first bi
        self.p1 = dd_class.Node("Rousse")
        self.p2 = dd_class.Node("Dorée")
        self.ind_1 = dd_class.Node("Rousse et Dorée", None, self.p1, self.p2)
        self.genealogie_1 = dd_class.Genealogie(self.ind_1)
        self.genealogie_1.update_weights()
        self.dd_fb1 = dd_class.Dragodinde(300, "M", "Rousse et Dorée", 2, self.genealogie_1)

        self.p1 = dd_class.Node("Amande")
        self.p2 = dd_class.Node("Dorée")
        self.ind_1 = dd_class.Node("Amande et Dorée", None, self.p1, self.p2)
        self.genealogie_1 = dd_class.Genealogie(self.ind_1)
        self.genealogie_1.update_weights()
        self.dd_fb2 = dd_class.Dragodinde(301, "F", "Amande et Dorée", 2, self.genealogie_1)

        # Mono Amande
        self.gp1 = dd_class.Node("Ebène")
        self.gp2 = dd_class.Node("Amande")
        self.p1 = dd_class.Node("Amande", None, self.gp1, self.gp2)
        self.p2 = dd_class.Node("Amande")
        self.ind_1 = dd_class.Node("Amande", None, self.p1, self.p2)
        self.genealogie_1 = dd_class.Genealogie(self.ind_1)
        self.genealogie_1.update_weights()
        self.dd_1 = dd_class.Dragodinde(1, "M", "Amande", 1, self.genealogie_1)

        # Mono Rousse
        self.gp3 = dd_class.Node("Indigo")
        self.gp4 = dd_class.Node("Rousse")
        self.p2 = dd_class.Node("Rousse", 0.5, self.gp3, self.gp4)
        self.p3 = dd_class.Node("Rousse")
        self.ind_2 = dd_class.Node("Rousse", None, self.p2, self.p3)
        self.genealogie_2 = dd_class.Genealogie(self.ind_2)
        self.genealogie_2.update_weights()
        self.dd_2 = dd_class.Dragodinde(2, "F", "Rousse", 1, self.genealogie_2)

        # Bi Rousse et Amande
        self.ggp1 = dd_class.Node("Dorée et Orchidée")
        self.ggp2 = dd_class.Node("Orchidée et Rousse")
        self.ggp3 = dd_class.Node("Rousse et Ebène")
        self.ggp4 = dd_class.Node("Turquoise et Rousse")
        self.gp5 = dd_class.Node("Rousse et Prune", None, self.ggp1, self.ggp2)
        self.gp6 = dd_class.Node("Ebène et Ivoire", None, self.ggp3, self.ggp4)
        self.p3 = dd_class.Node("Pourpre et Rousse", None, self.gp5, self.gp6)
        self.gp7 = dd_class.Node("Indigo et Orchidée")
        self.gp8 = dd_class.Node("Amande et Turquoise")
        self.p4 = dd_class.Node("Amande et Indigo", None, self.gp7, self.gp8)
        self.ind_1 = dd_class.Node("Rousse et Amande", None, self.p3, self.p4)
        self.genealogie_3 = dd_class.Genealogie(self.ind_1)
        self.genealogie_3.update_weights()
        self.dd_3 = dd_class.Dragodinde(3, "M", "Rousse et Amande", 2, self.genealogie_3)

        # Bi Pourpre et Orchidée  
        self.ggp5 = dd_class.Node("Rousse et Ebène")
        self.ggp6 = dd_class.Node("Turquoise et Rousse")
        self.ggp7 = dd_class.Node("Rousse et Prune")
        self.ggp8 = dd_class.Node("Dorée et Indigo")
        self.gp9 = dd_class.Node("Dorée et Emeraude", None, self.ggp5, self.ggp6)
        self.gp10 = dd_class.Node("Orchidée et Emeraude", None, self.ggp7, self.ggp8)
        self.p5 = dd_class.Node("Indigo et Ebène", None, self.gp9, self.gp10)
        self.gp11 = dd_class.Node("Amande et Ivoire")
        self.gp12 = dd_class.Node("Indigo et Ivoire")        
        self.p6 = dd_class.Node("Ivoire et Prune", None, self.gp11, self.gp12)
        self.ind_2 = dd_class.Node("Pourpre et Orchidée", None, self.p5, self.p6)
        self.genealogie_4 = dd_class.Genealogie(self.ind_2)
        self.genealogie_4.update_weights()
        self.dd_4 = dd_class.Dragodinde(4, "F", "Pourpre et Orchidée", 6, self.genealogie_4)

        self.elevage = dd_class.Elevage([self.dd_1, self.dd_2, self.dd_3, self.dd_4, 
                                         self.dd_sm1, self.dd_sm2, self.dd_sb1, self.dd_sb2,
                                         self.dd_fb1, self.dd_fb2])

    def uni_test_bad_crosing(self):
        with self.assertRaises(ValueError) as context:
            self.elevage.accouplement_naissance(self.elevage.get_dd_by_id(1), self.elevage.get_dd_by_id(3))

        self.assertEqual(str(context.exception), "Cannot breed dragodindes of the same sex.")

    def test_crosing_mono_mono(self):
        _, dic_probability = self.elevage.accouplement_naissance(self.elevage.get_dd_by_id(1), self.elevage.get_dd_by_id(2))
        expected_probability = {
                "Rousse": 41.019,
                "Amande": 41.019,
                "Rousse et Amande": 7.247,
                "Indigo": 4.337,
                "Ebène": 4.337,
                "Amande et Indigo": 0.957,
                "Rousse et Ebène": 0.957,
                "Indigo et Ebène": 0.128
            }

        print("dic_probability mono-mono: ", dic_probability, '\n')
        self.assertEqual(dic_probability, expected_probability)
    
    def test_crosing_mono_bi(self):
        _, dic_probability = self.elevage.accouplement_naissance(self.elevage.get_dd_by_id(1), self.elevage.get_dd_by_id(4))
        expected_probability = {
                "Amande" : 70.60,
                "Ebène": 10.68,
                "Pourpre et Orchidée": 6.22,
                "Indigo et Ebène": 4.61,
                "Ivoire et Prune": 1.48,
                "Indigo et Ivoire": 1.35,
                "Amande et Ivoire": 1.35,
                "Rousse et Ebène": 0.77,
                "Dorée et Indigo": 0.77,
                "Orchidée et Emeraude": 0.74,
                "Dorée et Emeraude": 0.74,
                "Turquoise et Rousse": 0.45,
                "Rousse et Prune": 0.25
            }

        print("dic_probability mono-bi : ", dic_probability, '\n')
        self.assertEqual(dic_probability, expected_probability)
    
    def test_crosing_bi_bi(self):
        _, dic_probability = self.elevage.accouplement_naissance(self.elevage.get_dd_by_id(3), self.elevage.get_dd_by_id(4))
        expected_probability = {
                "Rousse et Amande" : 16.59,
                "Pourpre et Orchidée" : 13.32,
                "Amande et Indigo" : 10.30,
                "Pourpre et Rousse" : 9.30,
                "Indigo et Ebène" : 8.51,
                "Indigo et Orchidée" : 4.65,
                "Ivoire et Prune" : 4.15,
                "Ebène et Ivoire" : 3.91,
                "Amande et Turquoise" : 3.91,
                "Rousse et Prune" : 3.38,
                "Indigo et Ivoire" : 3.23,
                "Rousse et Ebène" : 3.23,
                "Amande et Ivoire" : 3.23,
                "Turquoise et Rousse" : 2.38,
                "Orchidée et Emeraude" : 2.07,
                "Dorée et Emeraude" : 2.07,
                "Dorée et Orchidée" : 1.55,
                "Orchidée et Rousse" : 1.55,
                "Dorée et Indigo" : 1.51,
                "Pourpre" : 1.13

            }
        
        print("dic_probability bi-bi : ", dic_probability, '\n')
        self.assertEqual(dic_probability, expected_probability)

    def test_crosing_simple_mono_bi(self):
        _, dic_probability = self.elevage.accouplement_naissance(self.elevage.get_dd_by_id(100), self.elevage.get_dd_by_id(201))
        expected_probability = {
                "Rousse" : 83.333,
                "Pourpre et Ivoire" : 16.667
            }
        
        print("dic_probability simple mono-bi : ", dic_probability, '\n')
        self.assertEqual(dic_probability, expected_probability)

    def test_crosing_simple_mono_mono(self):
        _, dic_probability = self.elevage.accouplement_naissance(self.elevage.get_dd_by_id(100), self.elevage.get_dd_by_id(101))
        expected_probability = {
                "Rousse" : 45.455,
                "Amande" : 45.455,
                "Rousse et Amande" : 9.091
            }
        
        print("dic_probability simple mono-mono : ", dic_probability, '\n')
        self.assertEqual(dic_probability, expected_probability)

    def test_crosing_simple_bi_bi(self):
        _, dic_probability = self.elevage.accouplement_naissance(self.elevage.get_dd_by_id(200), self.elevage.get_dd_by_id(201))
        expected_probability = {
                "Indigo et Orchidée" : 60.0,
                "Pourpre et Ivoire" : 40.0,
            }
        
        print("dic_probability simple bi-bi : ", dic_probability, '\n')
        self.assertEqual(dic_probability, expected_probability)

    def test_crosing_first_bi_bi(self):
        _, dic_probability = self.elevage.accouplement_naissance(self.elevage.get_dd_by_id(300), self.elevage.get_dd_by_id(301))
        expected_probability = {
                "Rousse et Dorée" : 19.756,
                "Amande et Dorée" : 19.756,
                "Dorée" : 17.828,
                "Amande" : 17.549,
                "Rousse" : 17.549,
                "Ebène" : 6.887,
                "Rousse et Amande" : 0.676,
            }
        
        print("dic_probability first bi-bi : ", dic_probability, '\n')
        self.assertEqual(dic_probability, expected_probability)

if __name__ == "__main__":
    unittest.main()
