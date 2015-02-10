package com;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

/**
 * Created by rism on 7/8/14.
 */
class BinaryTreeNode
{
    BinaryTreeNode left;
    BinaryTreeNode right;
    int value;

    public BinaryTreeNode(int val)
    {
        this.value = val;
        this.left = null;
        this.right = null;
    }

    void compute()
    {
        try
        {
            notifyAll();
            wait();
//            Thread.sleep(3000);
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}

class NodeAdd implements Runnable
{
    private NodeAdd t;
    private String tName;
    private int num;
    public static BinaryTreeNode MyTree = new BinaryTreeNode(10);

    static
    {
        MyTree.left = new BinaryTreeNode(20);
        MyTree.right = new BinaryTreeNode(30);
        MyTree.left.left = new BinaryTreeNode(40);
        MyTree.left.right = new BinaryTreeNode(50);
        MyTree.right.left = new BinaryTreeNode(60);
        MyTree.right.right = new BinaryTreeNode(70);
    }

    public NodeAdd(String name, int num)
    {
        this.tName = name;
        this.num = num;
    }

    public void run()
    {
        traverse(MyTree);
    }

    public void traverse(BinaryTreeNode current)
    {
        if(current != null)
        {
            traverse(current.left);
            current.value += this.num;
            System.out.println(this.tName +"\t"+ current.value);
            current.compute();
            traverse(current.right);
        }
    }
}

public class DSFThread
{
//    private static Future taskTwo = null;
//    private static Future taskThree = null;

    public static void main(String[] args)
    {

        ExecutorService ES1 = Executors.newFixedThreadPool(3);
        Runnable taskOne = new NodeAdd("Thread 1", 1);
        ES1.execute(taskOne);

        Runnable taskTwo = new NodeAdd("Thread 2", 100);
        ES1.execute(taskTwo);

        Runnable taskThree = new NodeAdd("Thread 3", 1000);
        ES1.execute(taskThree);

        ES1.shutdown();
    }
}
