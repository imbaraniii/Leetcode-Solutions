// class Main {
//     public static void main (String[] args) {
//         int[] rungs = {3, 6, 8, 10};
//         int dist = 1;
//         Solution sol = new Solution();
//         System.out.println(sol.addRungs(rungs, dist));
//     }

// }

class Solution {
    public int addRungs(int[] rungs, int dist) {
        int extra_lad = 0;  // Count the extra ladders needed
        int current_height = 0; // Track the current height
	
	// O(n)
        for (int i=0; i<rungs.length; i++) {
            int dist_diff = rungs[i] - current_height; // Find the height difference between the current height and the next ladder

            // If the difference is greater than that of the maximums jumps that they can make
            if (dist_diff > dist) {
                current_height = rungs[i]; // Update the current height with the next height

                // First we check how many ladders can we put with height 'dist' between current position and the next ladder
                // if dist_diff is a multiple of dist, then we reduce one from their multiple.
                // if dist_diff is not a multiple of dist, then we add extra_lad with their multiple.
                extra_lad += (dist_diff%dist == 0 ? (dist_diff / dist) - 1 : (dist_diff / dist));
                continue;
            }
            
            // Update the current height
            current_height += dist_diff;
        }

        return extra_lad;
    }

    
}

// Time Complexity - O(n)
// Beats 100% - 1 ms


