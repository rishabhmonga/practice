package com.LRUImplementation;

import java.util.*;

/**
 * Created by rism on 7/11/14.
 */
public class LRUQueue
{
    int count;
    int numberOfFrames;

    private java.util.Queue<QNode> queue;

    public LRUQueue(int numberOfFrames)
    {
        this.count = 0;
        this.queue = new LinkedList<QNode>();
        this.numberOfFrames = numberOfFrames;
    }

    public boolean areAllFramesFull()
    {
        return (this.count == this.numberOfFrames);
    }

    public boolean isEmpty()
    {
        return this.queue.isEmpty();
    }

    public QNode enQueue(int val)
    {
        QNode node = new QNode(val);
        this.queue.add(node);
        return node;
    }

    public QNode enQueue(QNode node)
    {
        this.queue.add(node);
        return node;
    }

    public QNode deQueue()
    {
        return this.queue.remove();
    }

    public boolean deQueue(QNode node)
    {
        return this.queue.remove(node);
    }

    public QNode peek()
    {
        return queue.peek();
    }

    public void printQueue()
    {
        Iterator<QNode> it = queue.iterator();

        while (it.hasNext())
        {
            int iteratorValue = it.next().pageNumber;
            System.out.println(iteratorValue);
        }
    }


}
