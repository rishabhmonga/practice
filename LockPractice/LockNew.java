package com.LockPractice;

import java.util.concurrent.locks.ReentrantLock;

/**
 * Created by rism on 7/10/14.
 */
public class LockNew
{
    public static void main(String[] args)
    {
        ReentrantLock lock = new ReentrantLock();
        RunObj obj = new RunObj();

        Thread t1 = new Thread(new RunLock(lock, obj, "Thread 1"));
        t1.start();
        Thread t2 = new Thread(new RunLock(lock, obj, "Thread 2"));
        t2.start();
        Thread t3 = new Thread(new RunLock(lock, obj, "Thread 3"));
        t3.start();
        Thread t4 = new Thread(new RunLock(lock, obj, "Thread 4"));
        t4.start();


    }
}
class RunObj
{
    private int count;
    int inc()
    {
        return count++;
    }
}
class RunLock implements Runnable
{
    private ReentrantLock lock;
    private RunObj obj;
    private String threadName;

    RunLock(ReentrantLock lock,RunObj obj, String name)
    {
        this.lock = lock;
        this.obj = obj;
        this.threadName = name;
    }

    public void run()
    {
        try
        {
            lock.lock();
            for(int i = 0; i < 5; i++)
            {
                System.out.println(threadName + "\t" + obj.inc());
                Thread.sleep(200);
            }
        }
        catch (Exception e)
        {
            System.out.println("Thread Interrupted");
        }
        finally
        {
            lock.unlock();
        }

    }


}