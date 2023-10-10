

public class ReverseLinkedList {
        int val;
        ReverseLinkedList next;
        ReverseLinkedList(){}
        ReverseLinkedList(int val){
            this.val=val;
        }
        ReverseLinkedList(int val,ReverseLinkedList next){
            this.val=val;
            this.next=next;
        }
        public static ReverseLinkedList head;


    //Add  a new element to the end of the LinkedList    

    public static ReverseLinkedList addEnd(ReverseLinkedList head,int val){
        if(head==null){
            ReverseLinkedList ele=new ReverseLinkedList(val);
            return ele;
        }
        ReverseLinkedList dum=head;
        while(dum.next!=null){
            dum=dum.next;
        }
        dum.next=new ReverseLinkedList(val);
        return head;
    }
    

    //function to reverse the linkedlist
    public static ReverseLinkedList reverse(ReverseLinkedList head){
        if(head==null){
            return null;
        }
        ReverseLinkedList prev=head;
        ReverseLinkedList curr=prev.next;
        while(curr!=null){
            ReverseLinkedList nxt=curr.next;
            curr.next=prev;
            prev=curr;
            curr=nxt;
        }
        head.next=null;
        return prev;
    }
    
    //Print the linkedlist
    public static void printList(ReverseLinkedList head){
        ReverseLinkedList dum=head;
        while(dum!=null){
            System.err.print(dum.val+" ");
            dum=dum.next;
        }
    }
    public static void main(String[] args) {
         int a[]={3,4,5,56,20};
         for(int i:a){
           head=addEnd(head,i);
         }
         ReverseLinkedList ans=reverse(head);
         printList(ans);
    }
}
