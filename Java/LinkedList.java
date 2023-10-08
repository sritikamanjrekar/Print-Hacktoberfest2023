package Linked_List;

//* Node class which empty node class blue-print.
class Node {
    int data; //* Data of node.
    Node next; //* It will contain address of the next node. Which is initially null.

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

//* LinkedList class which contains all the nodes.
class Linked_List {
    static Node head; //* Created a head pointer.

    //* Build a function which add node at beginning of the LinkedList.
    public void insertAtFirst(int data) {
        //* Created a new node.
        Node newNode = new Node(data);

//* Step 1 :-
        //* Check if there is no node present into LL, So we will assign head to that new Node.
        if (head == null) {
            head = newNode;
            return;
        }
//* Step 2 :-
        //* Else there is already have a Node into LL.
        newNode.next = head; //* 1. Points the newNode to already present node.
        head = newNode; //* 2. Assign head to newNode.
    }

    //* Build a function which add node at end of the LinkedList
    public void insertAtEnd(int data) {
        //* Created new node.
        Node newNode = new Node(data);
//* Step 1 :-
        //* Check if head is null, if there is no node present then assign head to new node and return from there.
        if (head == null) {
            head = newNode;
            return;
        }
//* Step 2 :-
        //* Assign head to current node/temp node.
        Node currNode = head;
        //* Traverse the LL till node pointer null.
        while (currNode.next != null) {
            currNode = currNode.next;
        }
//* Step 3 :-
        //* Now, currNode reached at end then assign new node to currNode.next which is already null and that new node have null pointer.
        currNode.next = newNode;
    }

    //* Traverse all the nodes and print the elements.
    public void printLL() {
        //* Assign head to the tempNode.
        Node tempNode = head;

        //* Check either Linked list is empty or not.
        if (head == null) {
            System.out.println("Your Linked List is empty");
            return;
        }

        //* Traverse each node of LL and print that till we can't reach to that not which contains null.
        while (tempNode != null) {
            //* Print every data of node.
            System.out.print(tempNode.data + "-->");
            //* Now, give a refer tempNode to next node.
            tempNode = tempNode.next;
        }
        //* At the end of printing we will print NULL at last which help us to identify we reach at end.
        System.out.print("NULL");
    }
}

//* Main LinkedList class
public class LL {
    public static void main(String[] args) {
        //* Created an object of Linked List Class
        Linked_List ll = new Linked_List();

        //* Insert an element at Beginning function calls
        ll.insertAtFirst(12);
        ll.insertAtFirst(77);
        ll.insertAtFirst(86);

        //* Insert an element at End function calls
        ll.insertAtEnd(24);
        ll.insertAtEnd(75);
        ll.insertAtEnd(424);
        ll.insertAtEnd(264);

        //* Print function call.
        ll.printLL();
    }
}
