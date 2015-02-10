package SyncTest1;

/**
 * Created by rism on 8/7/14.
 */
public class Sync
{
    public synchronized static void syncStaticMethod(String threadName)
    {
        System.out.println(threadName+":\tStart static sleep");
        try
        {
            Thread.sleep(2000);
        }
        catch (InterruptedException e)
        {
        }
        System.out.println(threadName+":\tEnd static sleep");
    }

    public synchronized void syncInstanceMethod(String threadName)
    {
        System.out.println(threadName+":\tStart instance sleep");
        try
        {
            Thread.sleep(200);
        }
        catch (InterruptedException e)
        {
        }
        System.out.println(threadName+":\tEnd instance sleep");
    }

    public void testMethod(String threadName)
    {
        System.out.println(threadName+":\tTest Method");
    }
}

//class client implements Runnable
//{
//    private String threadName;
//    private Thread t;
//
//    public client(String name)
//    {
//        this.threadName = name;
//    }
//
//    public void start()
//    {
//        if(this.t == null)
//        {
//            this.t = new Thread(this, this.threadName);
//        }
//    }
//
//    public void run()
//    {
//
//    }
//}