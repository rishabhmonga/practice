package com.BinaryTreePractice;

/**
 * Created by rism on 7/9/14.
 */
public class BinaryTreeNode
{
    public BinaryTreeNode left;
    public BinaryTreeNode right;
    public int value;

    public BinaryTreeNode(int rootValue)
    {
        this.left = null;
        this.right = null;
        this.value = rootValue;
    }
}
