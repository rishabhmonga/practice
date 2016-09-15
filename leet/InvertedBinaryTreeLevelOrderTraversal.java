import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Stack;

/**
 * Created by rishabh on 9/14/2016.
 */
public class InvertedBinaryTreeLevelOrderTraversal {
    public static void main(String[] args) {
        InvertedBinaryTreeLevelOrderTraversal traversal = new InvertedBinaryTreeLevelOrderTraversal();
        BinaryTree root = new BinaryTree(1);
        root.left = new BinaryTree(2);
        root.right = new BinaryTree(3);
        root.left.left = new BinaryTree(4);
        root.left.right = new BinaryTree(5);
        root.right.left = new BinaryTree(6);
        root.right.right = new BinaryTree(7);
        List<List<Integer>> order = traversal.levelOrderBottom(root);
//        List<List<Integer>> order = traversal.levelOrderBottom(null);
        for (List<Integer> list : order) {
            for (int num : list) {
                System.out.print(num + "\t");
            }
            System.out.println();
        }
    }
    private List<List<Integer>> levelOrderBottom(BinaryTree root) {
        if (root == null) {
            return Collections.EMPTY_LIST;
        }
        Queue<BinaryTree> orderedQueue = new LinkedList<>();
        Queue<BinaryTree> auxQueue = new LinkedList<>();
        orderedQueue.add(root);
        Stack<List<Integer>> inverseStack = new Stack<>();
        List<Integer> levelList = new ArrayList<>();
        while (!orderedQueue.isEmpty()) {
            BinaryTree current = orderedQueue.remove();
            levelList.add(current.val);
            if(current.left != null) {
                auxQueue.add(current.left);
            }
            if(current.right != null) {
                auxQueue.add(current.right);
            }
            if(orderedQueue.isEmpty()) {
                while (!auxQueue.isEmpty()) {
                    orderedQueue.add(auxQueue.remove());
                }
                inverseStack.add(levelList);
                levelList = new ArrayList<>();
            }
        }
        List<List<Integer>> result = new ArrayList<>();
        while (!inverseStack.isEmpty()) {
            result.add(inverseStack.pop());
        }
        return result;
    }
}
