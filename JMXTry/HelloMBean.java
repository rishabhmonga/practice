package JMXTry;

/**
 * Created by rism on 9/26/14.
 */
public interface HelloMBean {
    public void setMessage(String message);
    public String getMessage();
    public void sayHello();
}