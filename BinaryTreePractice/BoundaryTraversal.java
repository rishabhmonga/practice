package com.BinaryTreePractice;

/**
 * Created by rism on 7/9/14.
 */
public class BoundaryTraversal
{
    private static void printLeaves(BinaryTreeNode root)
    {
        if(root != null)
        {
            printLeaves(root.left);

            if((root.left == null) && (root.right == null))
            {
                System.out.println(root.value);
            }
            printLeaves(root.right);
        }
    }

    private static void printBoundaryLeft(BinaryTreeNode root)
    {
        if(root != null)
        {
            if (root.left != null)
            {
                System.out.println(root.value);
                printBoundaryLeft(root.left);
            }
            else if (root.right != null)
            {
                System.out.println(root.value);
                printBoundaryLeft(root.right);
            }
        }
    }

    private static void printBoundaryRight(BinaryTreeNode root)
    {
        if(root != null)
        {
            if (root.right != null)
            {
                printBoundaryRight(root.right);
                System.out.println(root.value);
            }
            else if (root.left != null)
            {
                printBoundaryRight(root.left);
                System.out.println(root.value);
            }
        }
    }

    private static void printBoundary(BinaryTreeNode root)
    {
        if(root != null)
        {
            System.out.println(root.value);

            printBoundaryLeft(root.left);

            printLeaves(root.left);
            printLeaves(root.right);

            printBoundaryRight(root.right);
        }
    }

    public static void main(String[] args)
    {
        BinaryTreeNode myTree       = new BinaryTreeNode(20);
        myTree.left                 = new BinaryTreeNode(8);
        myTree.left.left            = new BinaryTreeNode(4);
        myTree.left.right           = new BinaryTreeNode(12);
        myTree.left.right.left      = new BinaryTreeNode(10);
        myTree.left.right.right     = new BinaryTreeNode(14);
        myTree.right                = new BinaryTreeNode(22);
        myTree.right.right          = new BinaryTreeNode(25);

        printBoundary(myTree);

    }
}
