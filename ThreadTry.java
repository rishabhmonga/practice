package com;

/**
 * Created by rism on 7/4/14.
 */
class ThreadDemo implements Runnable
{
    private Thread t;
    private String threadName;

    ThreadDemo(String name)
    {
        this.threadName = name;
        System.out.println("Creating " + threadName);
    }

    public void run()
    {
        System.out.println("Running " + threadName);
        try
        {
            for (int i = 4; i > 0; i--)
            {
                System.out.println("Thread: " + threadName + ", " + i);

                Thread.sleep(50);
            }
        }
        catch(InterruptedException e)
        {
            System.out.println("Thread "+threadName+" interrupted!");
        }
        System.out.println("Thread "+threadName+" Exiting");
     }

    public void start()
    {
        System.out.println("Starting " + threadName);
        if(t == null)
        {
            t = new Thread(this, threadName);
            t.start();
        }
    }
}

public class ThreadTry
{
    public static void main(String[] args)
    {
        ThreadDemo T1 = new ThreadDemo("Thread1");
        T1.start();

        ThreadDemo T2 = new ThreadDemo("Thread2");
        T2.start();
    }
}

