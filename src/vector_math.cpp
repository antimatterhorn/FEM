// vector_math.cpp (C++ code for vector math operations)

#include <vector>

namespace VectorMath {
    class Vector {
    public:
        std::vector<double> values;

        
        // Default constructor
        Vector() {}

        // Constructor with initializer list
        Vector(std::initializer_list<double> init) : values(init) {}

        // Method for vector addition
        Vector add(const Vector& other) const {
            Vector result;
            for (size_t i = 0; i < values.size(); ++i) {
                result.values.push_back(values[i] + other.values[i]);
            }
            return result;
        }

        // Method for dot product
        double dotProduct(const Vector& other) const {
            double result = 0.0;
            for (size_t i = 0; i < values.size(); ++i) {
                result += values[i] * other.values[i];
            }
            return result;
        }

        // Method for cross product (3D only!!)
        Vector crossProduct(const Vector& other) const {
            Vector result = {
                values[1] * other.values[2] - values[2] * other.values[1],
                values[2] * other.values[0] - values[0] * other.values[2],
                values[0] * other.values[1] - values[1] * other.values[0]
            };
            return result;
        }

        // Method for scalar product
        Vector scalarProduct(double scalar) const {
            Vector result;
            for (size_t i = 0; i < values.size(); ++i) {
                result.values.push_back(values[i] * scalar);
            }
            return result;
        }

        // Getter method for values
        const std::vector<double>& getValues() const {
            return values;
        }
    };
}
