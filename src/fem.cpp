// fem.cpp

#include <vector>
#include "vector_math.cpp"

namespace FEM {
    class Node {
    public:
        int id;
        VectorMath::Vector coordinates;

        Node(int nodeId, const VectorMath::Vector& nodeCoords) : id(nodeId), coordinates(nodeCoords) {}
    };

    class Element {
    public:
        int id;
        std::vector<Node*> nodes;

        Element(int elementId, const std::vector<Node*>& elementNodes) : id(elementId), nodes(elementNodes) {}
    };

    class FiniteElementGrid {
    public:
        std::vector<Node> nodes;
        std::vector<Element> elements;

        void addNode(const VectorMath::Vector& coordinates) {
            int nodeId = nodes.size() + 1;
            nodes.emplace_back(nodeId, coordinates);
        }

        void addElement(const std::vector<Node*>& elementNodes) {
            int elementId = elements.size() + 1;
            elements.emplace_back(elementId, elementNodes);
        }
    };
}
