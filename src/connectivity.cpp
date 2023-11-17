#include <iostream>
#include <vector>
#include <unordered_map>

class Node {
public:
    int id;
    // Other properties/methods...

    Node(int _id) : id(_id) {}
};

class Element {
public:
    int id;
    // Other properties/methods...

    Element(int _id) : id(_id) {}

    // Assuming a method like this exists for shared nodes check
    bool shares_nodes(const Element& other) const {
        // Implementation of shared nodes check...
        return false;
    }
};

namespace Connectivity {
    
    std::unordered_map<int, std::vector<int>> build_connectivity_map(const std::vector<Node>& nodes, const std::vector<Element>& elements) {
        std::cout << "Building connectivity map..." << std::endl;
        std::unordered_map<int, std::vector<int>> connectivity_map;

        for (const Element& element1 : elements) {
            for (const Element& element2 : elements) {
                if (element1.id != element2.id && element1.shares_nodes(element2)) {
                    connectivity_map[element1.id].push_back(element2.id);
                }
            }
        }

        std::cout << "Connectivity map built." << std::endl;
        return connectivity_map;
    }

}

