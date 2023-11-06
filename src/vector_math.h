// vector_math.h

#ifndef VECTOR_MATH_H
#define VECTOR_MATH_H

#include <vector>

namespace VectorMath {
    class Vector {
    public:
        std::vector<double> values;

        // Constructor with initializer list
        Vector(std::initializer_list<double> init);

        // Getter method for values
        const std::vector<double>& getValues() const;
    };
}

#endif // VECTOR_MATH_H
