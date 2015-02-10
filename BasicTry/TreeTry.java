package com.BasicTry;

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
}
public class TreeTry
{
    private static BinaryTreeNode MyTree = new BinaryTreeNode(10);

    static
    {
        MyTree.left = new BinaryTreeNode(20);
        MyTree.right = new BinaryTreeNode(30);
        MyTree.left.left = new BinaryTreeNode(40);
        MyTree.left.right = new BinaryTreeNode(50);
        MyTree.right.left = new BinaryTreeNode(60);
        MyTree.right.right = new BinaryTreeNode(70);
    }
    public static void traverse(BinaryTreeNode current)
    {
        if(current != null)
        {
            traverse(current.left);
            System.out.println(current.value);
            traverse(current.right);
        }
    }

    public static void main(String[] args)
    {
        traverse(MyTree);
    }
}
