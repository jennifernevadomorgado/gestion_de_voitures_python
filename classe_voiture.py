class voiture:
    def __init__(self,plaque,marque):
        self.plaque = plaque
        self.marque = marque 
        self.assuree = False # faux par defaut
    
    def assurer (self):
        self.assuree = True

    def resilier (self):
        self.assuree = False

    def afficher (self):
        print (self.plaque, self.marque, self.assuree)
