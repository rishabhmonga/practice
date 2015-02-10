package BasicTry.Int;

/**
 * Created by rism on 9/12/14.
 */
class LinkedListNode
{
    int value;
    LinkedListNode next;

    public LinkedListNode(int val)
    {
        this.value = val;
        next = null;
    }
}
public class RecursiveReverse
{
    public static void main(String[] args)
    {
        RecursiveReverse r = new RecursiveReverse();
        LinkedListNode head = new LinkedListNode(1);
        head.next = new LinkedListNode(2);
        head.next.next = new LinkedListNode(3);
        head.next.next.next = new LinkedListNode(4);
        head.next.next.next.next = new LinkedListNode(5);
        head.next.next.next.next.next = new LinkedListNode(6);

        printList(head);

        head = reverseIterative(head);
        System.out.println();
        printList(head);

        head = r.reverseRecursive(head);
//        r.reverseRecursive(head);
        System.out.println();
        printList(head);
    }

    public static void printList(LinkedListNode head)
    {
        while(head != null)
        {
            System.out.print(" " + head.value);
            head = head.next;
        }
    }

    public static LinkedListNode reverseIterative(LinkedListNode head)
    {
        LinkedListNode prev = null;
        LinkedListNode current = head;
        LinkedListNode temp = null;

        while (current != null)
        {
            temp = current.next;
            current.next = prev;
            prev = current;
            current = temp;
        }
        return prev;
    }

    public LinkedListNode reverseRecursive(LinkedListNode list)
    {
        if (list == null)
            return null;

        if(list.next == null)
        {
            return list;
        }

        LinkedListNode secondElement = list.next;
        list.next = null;
        LinkedListNode reverseRest  = reverseRecursive(secondElement);
        secondElement.next = list;
        return reverseRest;
    }
}
