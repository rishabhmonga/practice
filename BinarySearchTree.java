package com;

import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by rism on 7/7/14.
 */
class bstNode
{
    bstNode left;
    bstNode right;
    int value;

    public bstNode(int val)
    {
        this.value = val;
        this.left = null;
        this.right = null;
    }
}

class bst
{
    private bstNode root;
    private bstNode parent;
    private bstNode current;

    public bst(int val)
    {
        root = new bstNode(val);
    }

    public void insert(int val)
    {
        current = parent = root;
        while (current != null)
        {
            if(current.value > val)
            {
                parent = current;
                current = current.left;
            }
            else
            {
                if(current.value < val)
                {
                    parent = current;
                    current = current.right;
                }
            }
        }
        if(parent.value < val)
        {
            parent.right = new bstNode(val);
        }
        else
        {
            parent.left = new bstNode(val);
        }
    }

    public void levelOrder()
    {
        levelOrder(root);
    }

    private void levelOrder(bstNode r)
    {
        Queue<bstNode> orderQueue = new LinkedList<bstNode>();
        Queue<bstNode> auxQueue = new LinkedList<bstNode>();
        orderQueue.add(r);
        while(!orderQueue.isEmpty())
        {
            bstNode current = orderQueue.remove();

            System.out.print(current.value + "\t");
            if(current.left != null)
            {
                auxQueue.add(current.left);
            }
            if(current.right != null)
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

public class BinarySearchTree
{
    public static void main(String[] args)
    {
        bst t1 = new bst(10);
        t1.insert(5);
        t1.levelOrder();
        System.out.println();
        t1.insert(15);
        t1.levelOrder();
        System.out.println();
        t1.insert(25);
        t1.levelOrder();
        System.out.println();
        t1.insert(20);
        t1.levelOrder();
        System.out.println();
        t1.insert(35);
        t1.levelOrder();
        System.out.println();
    }
}
