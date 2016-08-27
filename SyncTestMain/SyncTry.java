package SyncTestMain;

import SyncTest1.Sync;

/**
 * Created by rism on 8/7/14.
 */
public class SyncTry
{
    public static void main(String[] args)
    {
        for (int i = 0; i < 3; ++i)
        {
            new Thread(new Runnable()
            {
                public void run()
                {
                    Sync.syncStaticMethod("StaticThread");
                    new Sync().testMethod("Static TestMethodThread");
                }
            }
            ).start();
        }

        for (int i = 0; i < 10; ++i)
        {
            new Thread(new Runnable()
            {
                public void run()
                {
                    new Sync().syncInstanceMethod("InstanceThread");
                    new Sync().testMethod("Instance TestMethodThread");
                }
            }
            ).start();
        }

//        for (int i = 0; i < 20; ++i)
//        {
//            new Thread(new Runnable()
//            {
//                public void run()
//                {
//                    new Sync().testMethod("TestMethodThread");
//                }
//            }
//            ).start();
//        }
    }
}
