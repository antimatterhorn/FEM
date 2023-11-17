class Material:
    def __init__(self, name=None, youngs_modulus=None, poisson_ratio=None, density=None, properties=None):
        if properties is not None:
            self.name = properties.get("name")
            self.youngs_modulus = properties.get("youngs_modulus")
            self.poisson_ratio = properties.get("poisson_ratio")
            self.density = properties.get("density")
        else:
            self.name = name
            self.youngs_modulus = youngs_modulus
            self.poisson_ratio = poisson_ratio
            self.density = density

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
        "name": "Steel",
        "youngs_modulus": 70e9,
        "poisson_ratio": 0.33,
        "density": 2700
    }

if __name__ == "__main__":
    # Example usage:
    steel = Material(properties=Materials.steel)
    aluminum = Material(name="Aluminum", youngs_modulus=70e9, poisson_ratio=0.33, density=2700)

    print(steel)
    print("\n")
    print(aluminum)