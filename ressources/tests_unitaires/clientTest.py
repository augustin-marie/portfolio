from ..Domain.client import Client
import unittest

class ClientTestCase(unittest.TestCase):
    def test_creeClient(self):
        # Arrange
        camille = Client("Marie", "Camille", 21, "251 rue des Postes")
        # Act

        # Assert
        self.assertIsNotNone(camille)
        self.assertEqual(camille.nom, "Marie")
        self.assertEqual(camille.prenom, "Camille")
        self.assertEqual(camille.age, 21)
        self.assertEqual(camille.adresse, "251 rue des Postes")

if __name__ == '__main__':
    unittest.main()