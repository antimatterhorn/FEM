from PYB11Generator import *
PYB11namespaces = ["VectorMath"]
PYB11includes = ['"vector_math.cpp"']

from vector_math import *

Vector1d = PYB11TemplateClass(Vector,
                              template_parameters = ("1"),
                              cppname = "Vector<1>",
                              pyname = "Vector1d",
                              docext = " (1D).")
Vector2d = PYB11TemplateClass(Vector,
                              template_parameters = ("2"),
                              cppname = "Vector<2>",
                              pyname = "Vector2d",
                              docext = " (2D).")
Vector3d = PYB11TemplateClass(Vector,
                              template_parameters = ("3"),
                              cppname = "Vector<3>",
                              pyname = "Vector3d",
                              docext = " (3D).") 