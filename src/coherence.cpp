// coherence.cpp

#include <vector>
#include <unordered_set>

namespace FEM {

    // Function to check shared nodes for 1D elements (edges for 2D, faces for 3D)
    template<int Dimension>
    bool check_shared_nodes(const std::vector<std::vector<int>>& elements) {
        std::unordered_set<std::vector<int>> unique_edges;

        for (const auto& element : elements) {
            std::vector<int> sorted_element = element;
            std::sort(sorted_element.begin(), sorted_element.end());
            if (!unique_edges.insert(sorted_element).second) {
                return false;  // Not a coherent mesh, shared edge/face found
            }
        }

        return true;  // Mesh is coherent, no shared edges/faces
    }
}