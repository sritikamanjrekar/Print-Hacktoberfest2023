https://leetcode.com/problems/minimum-processing-time
class Solution {
    // Method to calculate the minimum processing time
    public int minProcessingTime(List<Integer> processorTime, List<Integer> tasks) {
        // Sorting the processor times in ascending order
        Collections.sort(processorTime);
        // Sorting the tasks in descending order
        Collections.sort(tasks, Collections.reverseOrder());
        // Initializing variables for iteration and tracking max processing time
        int i = 0, j = 0, o = 0, max = Integer.MIN_VALUE;
        // Loop through tasks list
        while (i < tasks.size()) {
            // Calculate the current processing time by adding processor time and task time
            int curr = processorTime.get(j) + tasks.get(i);
            // Update the maximum processing time encountered so far
            max = Math.max(curr, max);
            // Increment counters for tasks and rounds of processing
            o++;
            i++;
            // Check if 4 tasks have been processed and there are more processors available
            if (o == 4 && j < processorTime.size() - 1) {
                // Reset round counter and move to the next processor
                o = 0;
                j++;
            }
        }
        // Return the maximum processing time
        return max;
    }
}
