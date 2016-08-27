package com.LRUImplementation;

import java.util.HashMap;

/**
 * Created by rism on 7/11/14.
 */
public class LRUCache
{
    protected static HashMap<Integer, QNode> hash = new HashMap<Integer, QNode>(10);

    public static void enQueue(LRUQueue queue, int pageNum)
    {
        if(queue.areAllFramesFull())
        {
            hash.remove(pageNum);
            queue.deQueue();
        }
        QNode node = queue.enQueue(pageNum);
        hash.put(pageNum, node);
        queue.count++;
        System.out.println("Count: " + queue.count);
    }

    public static void referencePage(LRUQueue queue, int pageNum)
    {
        QNode regPage = hash.get(pageNum);

        if(!hash.containsKey(pageNum))
        {
            enQueue(queue, pageNum);
        }

        else if(regPage != queue.peek())
        {
            queue.deQueue(regPage);
            enQueue(queue, pageNum);
        }
    }

    public static void main(String[] args)
    {
        LRUQueue q = new LRUQueue(4);
        referencePage(q, 1);
        referencePage(q, 2);
        referencePage(q, 3);
        referencePage(q, 1);
        referencePage(q, 4);
        referencePage(q, 5);

        q.printQueue();

        // Let us print cache frames after the above referenced pages

    }
}
