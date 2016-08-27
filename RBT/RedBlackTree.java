package com.RBT;

/**
 * Created by rism on 7/5/14.
 */
import java.util.*;

class RedBlackNode
{
    RedBlackNode left, right;
    int element;
    Color color;

    public RedBlackNode(int elementValue)
    {
        this(elementValue, null,null);
    }

    public RedBlackNode(int elementValue, RedBlackNode lt, RedBlackNode rt)
    {
        this.left = lt;
        this.right = rt;
        this.element = elementValue;
        this.color = Color.BLACK;
    }
}

class RBTree
{
    private RedBlackNode current;
    private RedBlackNode parent;
    private RedBlackNode grand;
    private RedBlackNode great;
    private RedBlackNode header;
    private static RedBlackNode nil;

    static
    {
        nil = new RedBlackNode(0);
        nil.left = nil;
        nil.right = nil;
    }

    public RBTree(int negInf)
    {
        header = new RedBlackNode(negInf);
        header.left = nil;
        header.right = nil;
    }

    public boolean isEmpty()
    {
        return header.right == nil;
    }

    public void makeEmpty()
    {
        header.right = nil;
    }

    public void insert(int item)
    {
        current = parent = grand = header;
        nil.element = item;
        while (current.element != item)
        {
            great = grand;
            grand = parent;
            parent = current;
            current = item < current.element ? current.left : current.right;

            if(current.left.color == Color.RED && current.right.color == Color.RED)
            {
                handleReOrient(item);
            }
        }

        if(current != nil)
        {
            return;
        }

        current = new RedBlackNode(item, nil, nil);

        if(item < parent.element)
        {
            parent.left = current;
        }

        else
        {
            parent.right = current;
        }

        handleReOrient(item);
    }

    private void handleReOrient(int item)
    {
        current.color = Color.RED;
        current.left.color = Color.BLACK;
        current.right.color = Color.BLACK;

        if(parent.color == Color.RED)
        {
            grand.color = Color.RED;

            if((item < grand.element) != (item < parent.element ))
            {
                parent = rotate(item, grand);
            }
            current = rotate(item, great);
            current.color = Color.BLACK;
        }
        header.right.color = Color.BLACK;
    }

    private RedBlackNode rotate(int item, RedBlackNode parent)
    {
        if(item < parent.element)
        {
            return parent.left = item < parent.left.element ? rotateWithLeftChild(parent.left) : rotateWithRightChild(parent.left) ;
        }
        else
        {
            return parent.right = item < parent.right.element ? rotateWithLeftChild(parent.right) : rotateWithRightChild(parent.right);
        }
    }

    private RedBlackNode rotateWithLeftChild(RedBlackNode k2)
    {
        RedBlackNode k1 = k2.left;
        k2.left = k1.right;
        k1.right = k2;
        return k1;
    }

    private RedBlackNode rotateWithRightChild(RedBlackNode k1)
    {
        RedBlackNode k2 = k1.right;
        k1.right = k2.left;
        k2.left = k1;
        return k2;
    }

    public int nodeCount()
    {
        return nodeCount(header.right);
    }

    private int nodeCount(RedBlackNode r)
    {
        if(r == nil)
        {
            return 0;
        }
        else
        {
            int l = 1;
            l += nodeCount(r.left);
            l += nodeCount(r.right);
            return l;
        }
    }

    public boolean search(int val)

    {

        return search(header.right, val);

    }

    private boolean search(RedBlackNode r, int val)
    {
        boolean found = false;
        while ((r != nil) && !found)
        {
            int rVal = r.element;
            if(val < rVal)
            {
                r = r.left;
            }
            else
            {
                if(val > rVal)
                {
                    r = r.right;
                }
                else
                {
                    found = true;
                    break;
                }
            }
            found = search(r, val);
        }
        return found;
    }

    public void inOrder()
    {
        inOrder(header.right);
    }

    private void inOrder(RedBlackNode r)
    {
        if(r != nil)
        {
            inOrder(r.left);
            String c = "BLACK";
            if(r.color == Color.RED)
            {
                c = "RED";
            }

            System.out.println(r.element + " " + c);

            inOrder(r.right);
        }
    }

    public void preOrder()
    {
        preOrder(header.right);
    }

    private void preOrder(RedBlackNode r)
    {
        if(r != nil)
        {
            String c = "BLACK";
            if(r.color == Color.RED)
            {
                c = "RED";
            }
            System.out.println(r.element + " " + c);
            inOrder(r.left);
            inOrder(r.right);
        }
    }

    public void postOrder()
    {
        postOrder(header.right);
    }

    private void postOrder(RedBlackNode r)
    {
        if(r != nil)
        {
            inOrder(r.left);
            inOrder(r.right);
            String c = "BLACK";
            if(r.color == Color.RED)
            {
                c = "RED";
            }
            System.out.println(r.element + " " + c);
        }
    }

    public void levelOrder()
    {
        levelOrder(header.right);
    }

    private void levelOrder(RedBlackNode r)
    {
        Queue<RedBlackNode> orderQueue = new LinkedList<RedBlackNode>();
        Queue<RedBlackNode> auxQueue = new LinkedList<RedBlackNode>();
        orderQueue.add(r);
        while(!orderQueue.isEmpty())
        {
            RedBlackNode current = orderQueue.remove();
            String c = "BLACK";
            if(current.color == Color.RED)
            {
                c = "RED";
            }
            System.out.print(current.element + "-" + c +"\t");
            if(current.left != nil)
            {
                auxQueue.add(current.left);
            }
            if(current.right != nil)
            {
                auxQueue.add(current.right);
            }
            if(orderQueue.isEmpty())
            {
                while (!auxQueue.isEmpty())
                {
                    orderQueue.add(auxQueue.remove());
                }
                System.out.println();
            }
        }
    }
}

public class RedBlackTree
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);

        RBTree rbt = new RBTree(Integer.MIN_VALUE);
        char ch = 'y';

        do
        {
            System.out.println("\nRed Black Tree Operations\n");

            System.out.println("1. insert ");

            System.out.println("2. search");

            System.out.println("3. count nodes");

            System.out.println("4. check empty");

            System.out.println("5. clear tree");

            System.out.println("6. Level Order");

            System.out.println("0. Exit");

            int choice = in.nextInt();

            switch (choice)
            {
                case 1:
                    System.out.println("Enter integer element to be inserted:\t");
                    rbt.insert(in.nextInt());
                    break;

                case 2:
                    System.out.println("Enter integer element to be inserted:\t");
                    System.out.println("Search result : "+ rbt.search(in.nextInt()));
                    break;

                case 3:
                    System.out.print("Node Count in Tree is:\t" + rbt.nodeCount());
                    break;

                case 4:
                    System.out.println("Empty Status:\t" + rbt.isEmpty());
                    break;

                case 5:
                    System.out.println("Tree Cleared!");
                    rbt.makeEmpty();
                    break;

                case 6:
                    System.out.println();
                    rbt.levelOrder();
                    break;

                case 0:
                    ch = ' ';
                    break;

                default:
                    System.out.println("Invalid Entry");
                    break;
            }

        } while(ch == 'Y' || ch == 'y');
    }
}
