from PYB11Generator import *

@PYB11template("dim")
class Vector:
    "the vector class for linear algebra"
    def pyinit(self):
        "default constructor"
        return
    #def pyinit3(self,x="double",y="double",z="double"):
    #    return
    def __add__(self):
        return
    def __mul__(self):
        return
    @PYB11pycppname("__mul__")
    def __mul__f(self,rhs="double()"):
        return    
    @PYB11cppname("toString")
    def __repr__(self):
        return



    x = PYB11property("double", getter="x", doc="The x coordinate.")
    y = PYB11property("double", getter="y", doc="The y coordinate.")
    z = PYB11property("double", getter="z", doc="The z coordinate.")

    magnitude = PYB11property("double", getter="magnitude", doc="The magnitude of the vector.")
     