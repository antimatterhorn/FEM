// vector_math.cpp

#include <vector>
#include <string>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace VectorMath {
    template <int dim>
    class Vector {
    public:
        // Use std::array instead of std::vector
        std::array<double, 3> values;

        // Constructors
        Vector() {
            // Initialize values array based on the dimension
            for (int i = 0; i < dim; ++i) {
                values[i] = 0.0;
            }
        }

        // Constructor with initializer list
        Vector(std::initializer_list<double> init) {
            if (init.size() != dim) {
                throw std::invalid_argument("Invalid number of arguments for Vector constructor");
            }
            
            // Copy values from initializer list to array
            std::copy(init.begin(), init.end(), values.begin());
        }

        // Methods
        Vector<dim> add(const Vector<dim>& other) const {
            Vector<dim> result;
            for (int i = 0; i < dim; ++i) {
                result.values[i] = values[i] + other.values[i];
            }
            return result;
        }

        Vector<dim> sub(const Vector<dim>& other) const {
            Vector<dim> result;
            for (int i = 0; i < dim; ++i) {
                result.values[i] = values[i] - other.values[i];
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

        Vector<dim> scalarProduct(double scalar) const {
            Vector<dim> result;
            for (int i = 0; i < dim; ++i) {
                result.values[i] = values[i] * scalar;
            }
            return result;
        }

        Vector<dim> operator+(const Vector<dim>& other) const {
            return add(other);
        }

        Vector<dim> operator-(const Vector<dim>& other) const {
            return sub(other);
        }

        Vector<dim> operator*(const double other) const {
            return scalarProduct(other);
        }

        Vector<dim> operator-() const {
            return scalarProduct(-1.0);
        }

        double operator*(const Vector<dim> other) const {
            return dotProduct(other);
        }

        Vector<dim> operator/(const double other) const {
            return scalarProduct(1.0/other);
        }

        bool operator==(const Vector<dim> other) const {
            bool result = true;
            for (int i = 0; i < dim; ++i) {
                if(values[i] != other.values[i])
                    result = false;
                    break;
            }
            return result;
        }

        bool operator!=(const Vector<dim> other) const {
            bool result = true;
            for (int i = 0; i < dim; ++i) {
                if(values[i] != other.values[i])
                    result = false;
                    break;
            }
            return !result;
        }

        Vector<3> crossProduct(const Vector<dim>& other) const {
            Vector<3> result = {
                values[1] * other.values[2] - values[2] * other.values[1],
                values[2] * other.values[0] - values[0] * other.values[2],
                values[0] * other.values[1] - values[1] * other.values[0]
            };
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

        static const unsigned numElements = dim;

    private:

    };

    // Define commonly used types
    using Vector1D = Vector<1>;
    using Vector2D = Vector<2>;
    using Vector3D = Vector<3>;

}

double computeQuadArea(const VectorMath::Vector2D& p1, const VectorMath::Vector2D& p2, const VectorMath::Vector2D& p3, const VectorMath::Vector2D& p4) {
    // Calculate centroid
    VectorMath::Vector2D centroid = (p1+p2+p3+p4)/4.0;

    // Sort points based on angle with respect to the centroid
    std::vector<const VectorMath::Vector2D*> sortedPoints = {&p1, &p2, &p3, &p4};
    std::sort(sortedPoints.begin(), sortedPoints.end(), [&centroid](const VectorMath::Vector2D* a, const VectorMath::Vector2D* b) {
        double angleA = std::atan2(a->values[1] - centroid.values[1], a->values[0] - centroid.values[0]);
        double angleB = std::atan2(b->values[1] - centroid.values[1], b->values[0] - centroid.values[0]);
        return angleA < angleB;
    });

    // Calculate signed area using the sorted points
    double area = 0.0;
    for (int i = 0; i < 4; ++i) {
        int nextIndex = (i + 1) % 4;
        area += (sortedPoints[i]->values[0] * sortedPoints[nextIndex]->values[1] - sortedPoints[nextIndex]->values[0] * sortedPoints[i]->values[1]);
    }

    return 0.5 * area;
}