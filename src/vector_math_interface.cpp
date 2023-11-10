#include "vector_math.cpp"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

// Binding for the Vector class
template <int dim>
void bindVector(py::module &m) {
    using VectorType = VectorMath::Vector<dim>;

    py::class_<VectorType>(m, ("Vector" + std::to_string(dim)).c_str())
        .def(py::init<>())
        .def(py::init<std::initializer_list<double>>())
        .def("add", &VectorType::add)
        .def("dotProduct", &VectorType::dotProduct)
        .def("crossProduct", &VectorType::crossProduct)
        .def("scalarProduct", &VectorType::scalarProduct)
        .def("__str__", &VectorType::toString);
}

PYBIND11_MODULE(VectorMath, m) {
    bindVector<1>(m);
    bindVector<2>(m);
    bindVector<3>(m);
}