package DCLTry;

/**
 * Created by rism on 8/3/14.
 */
public class DCLTest
{
    public static void main(String[] args)
    {
        Thread t1 = new Thread(new client("Client1"));
        Thread t2 = new Thread(new client("Client2"));
        Thread t3 = new Thread(new client("Client3"));
        t1.start();
        t2.start();
        t3.start();
    }
}

class SingletonClass
{
//    private volatile static SingletonClass instance = null;
    private static SingletonClass instance = null;
    private int value;
//    private Object lock = new Object();

    private SingletonClass()
    {
        this.value = 0;
        System.out.println("Object Created");
    }

    public static SingletonClass getInstance()
    {
        if (instance == null)
        {
            synchronized (SingletonClass.class)
            {
                if (instance == null)
                {
                    instance = new SingletonClass();
                }
            }
        }
        return instance;
    }

    public int increment()
    {
        if(instance.value < 10)
        {
            return instance.value++;
        }
        else
        {
            instance.value = instance.value%10;
            return instance.value;
        }
    }

    public static int incrementValue()
    {
        getInstance();
        return instance.increment();
    }
}

class client implements Runnable
{
    private String threadName;

    public client(String name)
    {
        this.threadName = name;
    }

    public void run()
    {
        for (int i = 0; i < 15; i++)
        {
            System.out.println("Thread: " + threadName + ", " + SingletonClass.incrementValue());
        }
        System.out.println("Thread "+threadName+" Exiting");
    }
}