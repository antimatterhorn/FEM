from fem import *

class SolidPhysics:
    def __init__(self,fem_grid,rho0,youngs_modulus,possion_ratio):
        self.fem_grid   = fem_grid
        self.rho0       = rho0
        self.E          = youngs_modulus
        self.nu         = possion_ratio
