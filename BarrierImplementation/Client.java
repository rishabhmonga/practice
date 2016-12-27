//package BarrierImplementation;
//
///**
// * Created by rism on 8/19/14.
// */
//public class Client implements Runnable
//{
//    private Thread t;
//
//    public void run()
//    {
//        increment();
//    }
//
//    public void start()
//    {
//        if(t == null)
//        {
//            t = new Thread(this);
//            t.start();
//        }
//    }
//
//    private int increment()
//    {
//        return BarrierTry.getNumber() + 1;
//    }
//
//
//}
