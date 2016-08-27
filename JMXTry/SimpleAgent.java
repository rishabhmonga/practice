package JMXTry;

import javax.management.MBeanServer;
import javax.management.ObjectName;
import java.lang.management.ManagementFactory;

/**
 * Created by rism on 9/26/14.
 */
public class SimpleAgent {
    private MBeanServer mbs = null;

    public SimpleAgent(){
        mbs = ManagementFactory.getPlatformMBeanServer();

        Hello hello = new Hello();
        ObjectName helloName = null;

        try {
            helloName = new ObjectName("FOO:name=HelloBean");
            mbs.registerMBean(hello, helloName);
        } catch(Exception e) {
            e.printStackTrace();
        }
    }

    private static void waitForEnterPressed() {
        try {
            System.out.println("Press  to continue...");
            System.in.read();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
//        SimpleAgent agent = new SimpleAgent();
        System.out.println("SimpleAgent is running...");
        SimpleAgent.waitForEnterPressed();
    }
}
