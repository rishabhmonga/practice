package com.LockPractice;

import com.sun.tools.doclets.internal.toolkit.util.SourceToHTMLConverter;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;

/**
 * Created by rism on 7/10/14.
 */
class MyLock implements Lock
{

    private boolean isLocked = false;

    public synchronized void lock()
    {
        while(isLocked)
        {
            try
            {
                wait();

            }
            catch (Exception e)
            {
                System.out.println("Thread Interrupted");
            }

        }
        isLocked = true;
    }

    @Override
    public void lockInterruptibly() throws InterruptedException
    {

    }

    @Override
    public boolean tryLock()
    {
        return false;
    }

    @Override
    public boolean tryLock(long l, TimeUnit timeUnit) throws InterruptedException
    {
        return false;
    }

    public synchronized void unlock()
    {
        isLocked = false;
        notify();
    }

    @Override
    public Condition newCondition()
    {
        return null;
    }

}

class ThreadImplement implements Runnable
{

    private MyLock lock = new MyLock();

    public int inc()
    {
        lock.lock();
        int newCount = ++LockTry.count;
        lock.unlock();
        return newCount;
    }

    public void run()
    {
        for(int i=0; i < 5; i++)
        {
            try
            {
                System.out.println(inc());
                Thread.sleep(200);
            }
            catch (Exception e)
            {
                System.out.println("Thread Interrupted again!");
            }
        }
    }



}

public class LockTry
{
    public static int count;
    public static void main(String[] args)
    {
        Thread t1 = new Thread(new ThreadImplement());
        t1.start();
        Thread t2 = new Thread(new ThreadImplement());
        t2.start();
        Thread t3 = new Thread(new ThreadImplement());
        t3.start();
        Thread t4 = new Thread(new ThreadImplement());
        t4.start();
        Thread t5 = new Thread(new ThreadImplement());
        t5.start();
    }

}
