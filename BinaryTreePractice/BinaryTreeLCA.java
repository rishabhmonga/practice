package com.BinaryTreePractice;

/**
 * Created by rism on 7/9/14.
 */
public class BinaryTreeLCA
{
    public static BinaryTreeNode findLCA(BinaryTreeNode root, int firstNode, int secondNode)
    {
        if(root == null)
        {
            return null;
        }

        if(root.value == firstNode || root.value == secondNode)
        {
            return root;
        }

        BinaryTreeNode leftLCA = findLCA(root.left, firstNode, secondNode);
        BinaryTreeNode rightLCA = findLCA(root.right, firstNode, secondNode);

        if(leftLCA != null && rightLCA != null)
        {
            return root;
        }

        return (leftLCA != null) ? leftLCA:rightLCA;
    }

    public static void main(String[] args)
    {
        BinaryTreeNode root     = new BinaryTreeNode(1);
        root.left               = new BinaryTreeNode(2);
        root.right              = new BinaryTreeNode(3);
        root.left.left          = new BinaryTreeNode(4);
        root.left.right         = new BinaryTreeNode(5);
        root.right.left         = new BinaryTreeNode(6);
        root.right.right        = new BinaryTreeNode(7);

        System.out.println(findLCA(root, 4, 5).value);
        System.out.println(findLCA(root, 4, 6).value);
        System.out.println(findLCA(root, 3, 4).value);
        System.out.println(findLCA(root, 2, 4).value);

    }
}
