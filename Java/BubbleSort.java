
public class BubbleSort {

    public static void main(String[] args) {

int[] nums = {100,98,4,2,3,1};
search(nums);
System.out.println(Arrays.toString(nums));

int n = nums.length-1;
int ans =1;
        for (int i = n-2; i <=n; i++) {

            ans = ans*nums[i];
        }
        System.out.println(ans);
    }


static void search(int[] nums){

        boolean swapped;

        int n = nums.length;

    for (int i = 0; i < n; i++) {
swapped=false;
        for (int j = 1; j < (n-i); j++) {

            if (nums[j]<nums[j-1]){
                int temp = nums[j];
                nums[j]=nums[j-1];
                nums[j-1]=temp;
                swapped=true;
            }

        }

        //if you did not swap for a particular value of i, it means the array is sorted
if (!swapped){
    break;
}

    }


}


}
