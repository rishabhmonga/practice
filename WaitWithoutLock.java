/**
 * Created by rism on 8/7/14.
 */
public class WaitWithoutLock
{
    public static PrintLog pL = new PrintLog();
    public static void main(String[] args)
    {
        client c1 = new client("Thread1");
        client c2 = new client("Thread2");
        client c3 = new client("Thread3");
        c1.start();
        c2.start();
        c3.start();
    }
}

class PrintLog
{
    public void printLog(String name)
    {
        System.out.println(name + ":\tTrying to Print");
    }
}

class client implements Runnable
{
    private String threadName;
    private Thread t;

    public client(String name)
    {
        this.threadName = name;
    }

    public void run()
    {
        try
        {
            t.wait();
        }
        catch (InterruptedException ie)
        {
            System.out.println(this.threadName + " Interrupted");
        }
        WaitWithoutLock.pL.printLog(threadName);
    }

    public void start()
    {
        if(t == null)
        {
            t = new Thread(this, threadName);
            t.start();
        }
    }

//    public void run()
//    {
//        synchronized (t)
//        {
//            try
//            {
//                if(t == null)
//                {
//                    t = new Thread(this, threadName);
//                    t.start();
//                }
//                t.wait(10);
//            }
//            catch (InterruptedException ie)
//            {
//                System.out.println(this.threadName + " Interrupted");
//            }
//        }
//        WaitWithoutLock.pL.printLog(threadName);
//    }
}