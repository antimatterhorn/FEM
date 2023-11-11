from PYB11Generator import *

@PYB11template("dim")
class Vector:
    "the vector class for linear algebra"
    def pyinit(self):
        "default constructor"
        return
    def pyinit1(self,x="double"):
        return
    def pyinit2(self,x="double",y="double"):
        return
    def pyinit3(self,x="double",y="double",z="double"):
        return
    def __add__(self):
        return
    def __sub__(self):
        return
    def __neg__(self):
        return
    def __mul__(self):
        return
    def __eq__(self):
        return
    def __ne__(self):
        return
    @PYB11pycppname("__mul__")
    def __mul__f(self,rhs="double()"):
        return    
    @PYB11cppname("toString")
    def __repr__(self):
        return
    # @PYB11implementation("[](const Vector<%(dim)s> &values, size_t i) -> double { if (i >= Vector<%(dim)s>::numElements) throw py::index_error(); return Vector<%(dim)s>::values[i]; }") 
    # @PYB11returnpolicy("reference_internal")
    # def __getitem__(self):
    #     "Python indexing to get a coordinate."
    #     return "double"

    @PYB11pyname("cross")
    def crossProduct(self):
        return

    x = PYB11property("double", getter="x", doc="The x coordinate.")
    y = PYB11property("double", getter="y", doc="The y coordinate.")
    z = PYB11property("double", getter="z", doc="The z coordinate.")

    magnitude = PYB11property("double", getter="magnitude", doc="The magnitude of the vector.")
     