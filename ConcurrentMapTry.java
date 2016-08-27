package com;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

/**
 * Created by rism on 7/4/14.
 */

class MyThread implements Runnable
{
//    private Thread t;
    private String threadName;

    MyThread(String name)
    {
        this.threadName = name;
        System.out.println("Creating " + threadName);
    }

    public void run()
    {
        System.out.println("Running " + threadName);
//        try
//        {
            for ( Integer i : ConcurrentMapTry.m.keySet())
            {
                ConcurrentMapTry.m.put(i, threadName);
                System.out.println( i +" "+ConcurrentMapTry.m.get(i));
                // Let the thread sleep for a while.
//                Thread.sleep(50);
            }
//        }
//        catch(InterruptedException e)
//        {
//            System.out.println("Thread "+threadName+" interrupted!");
//        }
        System.out.println("Thread "+threadName+" Exiting");
    }

//    public void start()
//    {
//        System.out.println("Starting " + threadName);
//        if(t == null)
//        {
//            t = new Thread(this, threadName);
//            t.start();
//        }
//    }
}

public class ConcurrentMapTry
{
    public static ConcurrentHashMap <Integer, String> m = new ConcurrentHashMap<Integer, String>(10,0.75f,1);

    public static void main(String[] args)
    {
        m.put(1," ");
        m.put(2," ");
        m.put(3," ");
        m.put(4," ");
        m.put(5," ");

        Thread T1 = new Thread(new MyThread("Thread1"));
        T1.start();

        Thread T2 = new Thread(new MyThread("Thread2"));
        T2.start();

        Thread T3 = new Thread(new MyThread("Thread3"));
        T3.start();

        Thread T4 = new Thread(new MyThread("Thread4"));
        T4.start();

    }
}
