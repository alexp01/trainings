Object e variabila ce primeste un class
Method e o functie intro clasa
Property e o 'variabila' intro clas
argument e variabila trimisa cand apelam o metoda dintro clasa. Primul parametru e dedicata pt self.
parametru e variabila ce o poate primi o metoda : exemplu def alex (name):


- "class.__name__" will give you the class name


Rules:
- staticmethods should not be used. If used you needt o be sure that that object will not be inherited
- classmethod will be used when you do not want to use the self from the inherited class, and you prefer using you own internal self

