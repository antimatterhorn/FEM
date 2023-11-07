// vector_math.h

#ifndef VECTOR_MATH_H
#define VECTOR_MATH_H

#include <vector>
#include <string>

namespace VectorMath {
    template <int dim>
    class Vector {
    public:
        std::vector<double> values;

        // Constructors
        Vector() : values(dim, 0.0) {}

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
            std::stringstream ss;
            ss << "(";
            for (int i = 0; i<dim-1;++i)
                ss << values[i] << ",";
            ss << values[dim-1] << ")";
            return ss.str();
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
    };

    // Define commonly used types
    using Vector1D = Vector<1>;
    using Vector2D = Vector<2>;
    using Vector3D = Vector<3>;
}

#endif // VECTOR_MATH_H
