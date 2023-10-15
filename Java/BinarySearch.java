public class BinarySearch {
    public static void search(int arr[],int key,int s,int e){
        // int s=0;
        // int e=arr.length-1;
        int m=(s+e)/2;
        while(s<=e){
            if(arr[m]==key){
                System.out.println("Element found at index = "+ m);
                break;
            }
            
            else if(arr[m]<key){
                s=m+1;
            }
            else{
                e=m-1;
            }
            m=(s+e)/2;
        }
    }
    public static void main(String[] args) {
        int arr[]={1,2,3,4,5};
        int key=1;
        search(arr,key,0,arr.length-1);
    }
}
