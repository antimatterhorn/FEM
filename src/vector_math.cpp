// vector_math.cpp

#include <vector>
#include <string>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace VectorMath {
    template <int dim>
    class Vector {
    public:
        std::vector<double> values;

        // Constructors
        Vector() : values(dim, 0.0) {}

        // Constructor with initializer list
        Vector(std::initializer_list<double> init) : values(init) {
            if (init.size() != dim) {
                throw std::invalid_argument("Invalid number of arguments for Vector constructor");
            }
        }

        // Constructor with individual values
        template <typename... Args>
        Vector(Args... args) : values{static_cast<double>(args)...} {
            static_assert(sizeof...(args) == dim, "Invalid number of arguments for Vector constructor");
        }

        // Methods
        Vector<dim> add(const Vector<dim>& other) const {
            Vector<dim> result;
            for (int i = 0; i < dim; ++i) {
                result.values[i] = values[i] + other.values[i];
            }
            return result;
        }

        double dotProduct(const Vector<dim>& other) const {
            double result = 0.0;
            for (int i = 0; i < dim; ++i) {
                result += values[i] * other.values[i];
            }
            return result;
        }

        Vector<3> crossProduct(const Vector<3>& other) const {
            Vector<3> result = {
                values[1] * other.values[2] - values[2] * other.values[1],
                values[2] * other.values[0] - values[0] * other.values[2],
                values[0] * other.values[1] - values[1] * other.values[0]
            };
            return result;
        }

        Vector<dim> scalarProduct(double scalar) const {
            Vector<dim> result;
            for (int i = 0; i < dim; ++i) {
                result.values[i] = values[i] * scalar;
            }
            return result;
        }

        // Getter methods for individual components
        double x() const {
            return values.size() > 0 ? values[0] : 0.0;
        }

        double y() const {
            return values.size() > 1 ? values[1] : 0.0;
        }

        double z() const {
            return values.size() > 2 ? values[2] : 0.0;
        }

        std::string toString() const {
            std::string result = "(";
            for (int i = 0; i < dim; ++i) {
                if (i > 0) {
                    result += ", ";
                }
                result += std::to_string(values[i]);
            }
            result += ")";
            return result;
        }

        double mag2() const {
            double result = 0.0;
            for (double value : values) {
                result += value*value;
            } 
            return result;
        }

        double magnitude() const {
            return std::sqrt(mag2());
        }

    private:
        template <typename T, typename... Args>
        void initialize(T first, Args... rest) {
            values.push_back(static_cast<double>(first));
            initialize(rest...);
        }

        void initialize() {}
    };

    // Define commonly used types
    using Vector1D = Vector<1>;
    using Vector2D = Vector<2>;
    using Vector3D = Vector<3>;
}
