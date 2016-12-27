package com.LRUImplementation;

/**
 * Created by rism on 7/11/14.
 */
public class QNode
{
    QNode prev, next;
    int pageNumber;

    public QNode(int pNum)
    {
        this.pageNumber = pNum;
        prev = null;
        next = null;
    }
}
