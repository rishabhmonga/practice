package BasicTry.Int;

import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by rism on 9/12/14.
 */
class TreeNode
{
    public int value;
    public TreeNode left;
    public TreeNode right;

    public TreeNode(int val)
    {
        this.value = val;
        this.left = null;
        this.right = null;
    }
}
public class BFS
{
    public static void main(String[] args)
    {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);

        BFS t = new BFS();
        t.traverse(root);
        System.out.println();
        bfsOrder.add(root);
        t.traverseRec2();

    }

    public static Queue<TreeNode> bfsOrder = new LinkedList<TreeNode>();

    private void traverse(TreeNode root)
    {
        bfsOrder.add(root);
        while(!bfsOrder.isEmpty())
        {
            TreeNode temp = bfsOrder.remove();
            if(temp.left != null)
            {
                bfsOrder.add(temp.left);
            }
            if(temp.right != null)
            {
                bfsOrder.add(temp.right);
            }
            System.out.print(temp.value);
        }
    }

//    public void traverseRec1(TreeNode root)
//    {
//        bfsOrder.add(root);
//    }

    private void traverseRec2()
    {
        if(bfsOrder.isEmpty())
        {
            return;
        }
        TreeNode root = bfsOrder.remove();
        System.out.print(root.value);
        if(root.left != null)
        {
            bfsOrder.add(root.left);
        }
        if(root.right != null)
        {
            bfsOrder.add(root.right);
        }
        traverseRec2();
    }
}
