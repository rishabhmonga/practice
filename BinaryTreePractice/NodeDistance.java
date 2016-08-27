package com.BinaryTreePractice;

/**
 * Created by rism on 7/9/14.
 */

public class NodeDistance
{
    public static int findDistance(BinaryTreeNode root, int firstKey, int secondKey)
    {
        BinaryTreeNode LCA = BinaryTreeLCA.findLCA(root, firstKey, secondKey);

        return pathLength(LCA, firstKey) + pathLength(LCA, secondKey);

    }

    public static int pathLength(BinaryTreeNode root, int key)
    {
        if(root == null)
        {
            return -1;
        }
        if(root.value == key)
        {
            return 0;
        }

        int dl = pathLength(root.left, key);
        if(dl != -1)
        {
            return 1+dl;
        }

        int dr = pathLength(root.right, key);
        if(dr != -1)
        {
            return 1+dr;
        }

        return -1;
    }

    public static void main(String[] args)
    {
        BinaryTreeNode root = new BinaryTreeNode(1);
        root.left = new BinaryTreeNode(2);
        root.right = new BinaryTreeNode(3);
        root.left.left = new BinaryTreeNode(4);
        root.left.right = new BinaryTreeNode(5);
        root.right.left = new BinaryTreeNode(6);
        root.right.right = new BinaryTreeNode(7);

        System.out.println(findDistance(root, 4,5));
    }
}