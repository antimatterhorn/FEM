class Material:
    def __init__(self, name=None, youngs_modulus=None, poisson_ratio=None, density=None, properties=None):
        if properties is not None:
            self.name           = properties.get("name")
            self.youngs_modulus = properties.get("youngs_modulus")
            self.poisson_ratio  = properties.get("poisson_ratio")
            self.density        = properties.get("density")
        else:
            self.name           = name
            self.youngs_modulus = youngs_modulus
            self.poisson_ratio  = poisson_ratio
            self.density        = density

    def __str__(self):
        return f"Material: {self.name}\nYoung's Modulus: {self.youngs_modulus}\nPoisson's Ratio: {self.poisson_ratio}\nDensity: {self.density}"

class Materials:

    steel = {
        "name": "Steel",
        "youngs_modulus": 200e9,
        "poisson_ratio": 0.3,
        "density": 7800
    }

    aluminum = {
        "name": "Aluminum",
        "youngs_modulus": 70e9,
        "poisson_ratio": 0.33,
        "density": 2700
    }

    concrete = {
        "name": "Concrete",
        "youngs_modulus": 30e9,
        "poisson_ratio": 0.2,
        "density": 2400
    }

    rubber = {
        "name": "Rubber",
        "youngs_modulus": 0.01e9,
        "poisson_ratio": 0.48,
        "density": 1200
    }

    copper = {
        "name": "Copper",
        "youngs_modulus": 110e9,
        "poisson_ratio": 0.34,
        "density": 8900
    }

    titanium = {
        "name": "Titanium",
        "youngs_modulus": 110e9,
        "poisson_ratio": 0.34,
        "density": 4500
    }

    stainless_steel = {
        "name": "Stainless Steel",
        "youngs_modulus": 200e9,
        "poisson_ratio": 0.3,
        "density": 7900
    }

    glass = {
        "name": "Glass",
        "youngs_modulus": 70e9,
        "poisson_ratio": 0.23,
        "density": 2500
    }

    wood = {
        "name": "Wood",
        "youngs_modulus": 10e9,
        "poisson_ratio": 0.3,
        "density": 500
    }

    hdpe = {
        "name": "HDPE",
        "youngs_modulus": 1e9,
        "poisson_ratio": 0.4,
        "density": 950
    }

    brass = {
        "name": "Brass",
        "youngs_modulus": 100e9,
        "poisson_ratio": 0.33,
        "density": 8500
    }


if __name__ == "__main__":
    # Example usage:
    steel = Material(properties=Materials.steel)
    aluminum = Material(name="Aluminum", youngs_modulus=70e9, poisson_ratio=0.33, density=2700)

    print(steel)
    print("\n")
    print(aluminum)