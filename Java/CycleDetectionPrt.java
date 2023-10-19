import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CycleDetectionPrt {

    public static void main(String[] args) {
        
        Map<Integer, List<Integer>> graph = new HashMap<>();
        graph.put(0, List.of(1, 2));
        graph.put(1, List.of(2));
        graph.put(2, List.of(0, 3));
        graph.put(3, List.of(3));

        if (containsCycle(graph)) {
            System.out.println("The graph contains a cycle.");
        } else {
            System.out.println("The graph does not contain a cycle.");
        }
    }

    public static boolean containsCycle(Map<Integer, List<Integer>> graph) {
        //track of visited vertices during DFS
        boolean[] visited = new boolean[graph.size()];
        // track of vertices in the current DFS traversal
        boolean[] currentlyInStack = new boolean[graph.size()];

        for (int vertex : graph.keySet()) {
            if (!visited[vertex] && isCyclic(graph, vertex, visited, currentlyInStack)) {
                return true;
            }
        }

        return false;
    }

    private static boolean isCyclic(Map<Integer, List<Integer>> graph, int vertex,
                                    boolean[] visited, boolean[] currentlyInStack) {
        visited[vertex] = true;
        currentlyInStack[vertex] = true;

        if (graph.containsKey(vertex)) {
            for (int neighbor : graph.get(vertex)) {
                if (!visited[neighbor]) {
                    if (isCyclic(graph, neighbor, visited, currentlyInStack)) {
                        return true;
                    }
                } else if (currentlyInStack[neighbor]) {
                    return true; //Cycle detected
                }
            }
        }

        currentlyInStack[vertex] = false; //Backtrack

        return false;
    }
}
