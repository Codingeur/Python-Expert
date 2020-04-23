import abc

class Produit:
    @property
    def forme(self):
        return self._forme
    @forme.setter
    def forme(self, forme):
        self._forme = forme
    @property
    def couleur(self):
        return self._couleur
    @couleur.setter
    def couleur(self, couleur):
        self._couleur = couleur
    def __str__(self):
        return 'Produit forme = %s couleur = %s' %(self.forme, self.couleur)

class Monteur:
    @property
    def produit(self):
        return self._produit
    @produit.setter
    def produit(self, produit):
        self._produit = produit
    def creerProduit(self):
        self.produit = Produit()
    @abc.abstractclassmethod
    def concevoirForme(self):
        return
    @abc.abstractclassmethod
    def concevoirCouleur(self):
        return

class MonteurCubeBleu(Monteur):
    def concevoirForme(self):
        self.produit.forme = "Cube"
    def concevoirCouleur(self):
        self.produit.couleur = "Bleu"

class MonteurSphereRouge(Monteur):
    def concevoirForme(self):
        self.produit.forme = "Shere"
    def concevoirCouleur(self):
        self.produit.couleur = "Rouge"

class MonteurPyramideJaune(Monteur):
    def concevoirForme(self):
        self.produit.forme = "Pyramide"
    def concevoirCouleur(self):
        self.produit.couleur = "Jaune"

class Directeur:
    @property
    def monteur(self):
        return self._monteur
    @monteur.setter
    def monteur(self, monteur):
        self._monteur = monteur
    def concevoirProduit(self):
        self.monteur.creerProduit()
        self.monteur.concevoirForme()
        self.monteur.concevoirCouleur()
        return self.monteur.produit

directeur = Directeur()
directeur.monteur = MonteurSphereRouge()
produit = directeur.concevoirProduit()
print(produit)
