package com.InterruptTry;

/**
 * Created by rism on 8/27/14.
 */
public class InterruptTry
{
    public static void main(String[] args){
        TryInt t1 = new TryInt();
        TryInt1 t2 = new TryInt1();

        t1.setInt1(t2);
        t2.setInt1(t1);

        t1.start();
        t2.start();
    }

}
class TryInt extends Thread {
    private TryInt1 int1;

    public void setInt1(final TryInt1 int1){
        this.int1 = int1;
    }


    public void run(){

        int1.interrupt();

    }
}

class TryInt1 extends Thread {
    private TryInt int1;

    public void setInt1(final TryInt int1){
        this.int1 = int1;
    }
    public void run(){
        int1.interrupt();
    }
}