package InterruptTry;

/**
 * Created by rism on 8/27/14.
 */
public class TestInt
{
    public static void main(String[] args){
        TryInt1 t2 = new TryInt1();
        TryInt t1 = new TryInt(t2);
        t1.start();
        t2.start();
        t1.interrupt();
    }

}
class TryInt extends Thread {
    private TryInt1 int1;
    TryInt(TryInt1 int1){
        this.int1 = int1;
    }
    public void run(){
        try
        {
            Thread.sleep(1000);
        }catch (InterruptedException e){
            System.out.println("Interup");
        }
        int1.interrupt();
    }
}

class TryInt1 extends Thread {

    public void run(){
        try
        {
            Thread.sleep(8000);
        }
        catch (InterruptedException e){
            System.out.println("Interupted");

        }
    }
}