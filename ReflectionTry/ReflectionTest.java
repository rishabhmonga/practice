package ReflectionTry;

import java.lang.reflect.*;

/**
 * Created by rism on 8/14/14.
 */
public class ReflectionTest
{
    public static void main(String[] args)
    {
        Method[] methods = TryClass.class.getDeclaredMethods();

        for(Method method : methods)
        {
            System.out.println("method = " + method.getName());
        }

        int modifiers = TryClass.class.getModifiers();

        System.out.println(modifiers);
    }
}
