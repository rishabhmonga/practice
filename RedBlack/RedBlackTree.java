package com.RedBlack;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

/**
 * Created by rism on 7/7/14.
 */

class RedBlackNode
{
    RedBlackNode left, right;
    RedBlackNode parent;
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
        this.parent = null;
        this.element = elementValue;
        this.color = Color.RED;
    }

    public RedBlackNode getParent()
    {
        return this.parent;
    }

    public void setParent(RedBlackNode r)
    {
        this.parent = r;
    }

    public Color getColor()
    {
        return this.color;
    }

    public void setColor(Color c)
    {
        this.color = c;
    }

    public RedBlackNode getGrandParent()
    {
        if(this.parent != null)
        {
            return this.parent.parent;
        }
        else
        {
            return null;
        }
    }

    public RedBlackNode getUncle()
    {
        RedBlackNode grand = this.getGrandParent();
        if(grand == null)
        {
            return null;
        }
        if(this.parent == grand.left)
        {
            return grand.right;
        }
        else
        {
            return grand.left;
        }
    }

    public void leftRotate()
    {
//        Left Rotation on A
//
//                C                   C
//              /   \                / \
//             A          --->      B
//               \                 /
//                B               A
//               /                 \
//              X                   X

        if(this.parent != null && this.right != null && this.left != null )
        {
            this.right.left.parent = this;
            RedBlackNode temp = this.right.left.parent;
            this.right.parent = this.getParent();
            this.parent = this.right;
            this.right.getParent().left = this.right;
            this.getParent().left = this;
            this.right = temp;
        }
    }

    public void rightRotate()
    {
//        Right rotate on C
//
//            C                 B
//           / \               / \
//          B       ---->     A   C
//         / \                   /
//        A  X                  X
//
//        this.left.right.parent = this;
//        RedBlackNode temp = this.left.right;        //Saved right child of B
//        this.left.parent = this.parent;             //Parent of C is now parent of B
//        this.getParent().left = this.right;
//        this.parent = this.left;
//        this.left.right = this;
//        this.left = temp;
        if(this.parent != null && this.right != null && this.left != null )
        {
            RedBlackNode temp = this.left.right;
            RedBlackNode savedParent = this.getParent();

            this.getParent().left = this.left;
            this.left.right = this;
            this.left = temp;

            this.setParent(this.left.getParent());
            this.left.setParent(this);
            this.getParent().setParent(savedParent);
        }
    }

}

class RBTree
{
    private RedBlackNode root;
    private RedBlackNode father;
    private RedBlackNode current;

    public RBTree(int negInf)
    {
        root = new RedBlackNode(negInf);
        root.left = null;
        root.right = null;
    }

    public void insert(int item)
    {
        current = father = root;
        while(current != null)
        {
            if(current.element > item)
            {
                father = current;
                current = current.left;
            }
            else
            {
                if(current.element < item)
                {
                    father = current;
                    current = current.right;
                }
            }
        }
        if(father.element < item)
        {
            father.right = new RedBlackNode(item);
            current = father.right;
        }
        else
        {
            father.left = new RedBlackNode(item);
            current = father.left;
        }
        current.setParent(father);

        System.out.println(current.element + " going to case 1");

        insert_case1(current);
      }

    public void insert_case1(RedBlackNode x)
    {
        if(x.parent == null)    //X is ROOT
        {
            x.setColor(Color.BLACK);
        }
        else
        {
            System.out.println(x.element + " going to case 2");

            insert_case2(x);
        }
    }

    public void insert_case2(RedBlackNode x)
    {
        if(x.parent.getColor() == Color.BLACK)
        {
            return;
        }
        else
        {
            System.out.println(x.element + " going to case 3");

            insert_case3(x);
        }
    }

    public void insert_case3(RedBlackNode x)
    {
        if((x.getUncle() != null) && x.getUncle().getColor() == Color.RED)
        {
            x.getParent().setColor(Color.BLACK);
            x.getUncle().setColor(Color.BLACK);
            x.getGrandParent().setColor(Color.RED);

            System.out.println(x.getGrandParent().element + " going to case 1");

            insert_case1(x.getGrandParent());
        }
        else
        {
            System.out.println(x.element + " going to case 4");
            insert_case4(x);
        }
    }

    public void insert_case4(RedBlackNode x)
    {
        if((x == x.getParent().right) && x.getGrandParent() != null && (x.getParent() == x.getGrandParent().right))
        {
            x.getParent().leftRotate();
            x = x.left;
        }
        else if((x == x.getParent().left) && x.getGrandParent() != null && x.getParent() == x.getGrandParent().right)
        {
            x.getParent().rightRotate();
            x = x.right;
        }
        System.out.println(x.element + " going to case 5");
        insert_case5(x);
    }

    public void insert_case5(RedBlackNode x)
    {
        x.getParent().setColor(Color.BLACK);
        if(x.getGrandParent() != null)
        {
            x.getGrandParent().setColor(Color.RED);
        }
        if(x == x.getParent().left && x.getGrandParent() != null)
        {
            x.getGrandParent().rightRotate();
        }
        else
        {
            if(x.getGrandParent() != null)
            {
                x.getGrandParent().leftRotate();
            }
        }
    }

    public void levelOrder()
    {
        levelOrder(root);
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
//            if(current.left != nil)
            if(current.left != null)
            {
                auxQueue.add(current.left);
            }
//            if(current.right != nil)
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

public class RedBlackTree
{
    public static void main(String[] args)
    {
        RBTree t1 = new RBTree(10);
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
