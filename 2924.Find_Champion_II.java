// There are n teams numbered from 0 to n - 1 in a tournament; each team is also a node in a DAG.

// You are given the integer n and a 0-indexed 2D integer array edges of length m representing the DAG, where edges[i] = [ui, vi] indicates that there is a directed edge from team ui to team vi in the graph.

// A directed edge from a to b in the graph means that team a is stronger than team b and team b is weaker than team a.

// Team a will be the champion of the tournament if there is no team b that is stronger than team a.

// Return the team that will be the champion of the tournament if there is a unique champion, otherwise, return -1.
 
// Notes

    // A cycle is a series of nodes a1, a2, ..., an, an+1 such that node a1 is the same node as node an+1, the nodes a1, a2, ..., an are distinct, and there is a directed edge from the node ai to node ai+1 for every i in the range [1, n].
    // A DAG is a directed graph that does not have any cycle.
    

class Solution {
    // Function to check if there are any incoming nodes for a node.
    // O(E)
    private boolean zeroIncoming (int source, int[][] edges) {
        for (int i=0; i<edges.length; i++) {
            if (edges[i][1] == source) {
                return false;
            }
        }

        return true;

    }
    public int findChampion(int n, int[][] edges) {
        if (n == 1 ) {
            return 0;
        }

        // Winners list
        List<Integer> winners = new ArrayList<>();
        // Visited list
        Set<Integer> visited = new HashSet<>();
	
	// O(E)
        for (int i=0; i < edges.length; i++) {
            // if the current vertex is not visited
	    // O(V)
            if (!visited.contains(edges[i][0])) {
                // No incoming edges
                if (zeroIncoming(edges[i][0], edges)) {
                    winners.add(edges[i][0]); // add those to the winners list
                }
            }

            // Mark the current vertices as visited
            visited.add(edges[i][0]);
            visited.add(edges[i][1]);

        }

        // If all the vertices are visited and the size of the winners is exactly 1, then return that winner
        if (winners.size() == 1 && visited.size() == n) {:
            return winners.get(0);
        }

        // else return -1, stating that there are more than 1 winners
        return -1;

    }
}

// Total complexity: O(E^2)

