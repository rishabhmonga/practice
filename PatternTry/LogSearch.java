package PatternTry;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Created by rism on 12/12/14.
 */
public class LogSearch {
    public static void main(String[] args) {
        System.out.println(isLogFile("terracotta-server.log"));
        System.out.println(isLogFile("terracotta-logging.lock"));
        System.out.println(isLogFile("terracotta-server.1.log"));
    }

    private static Boolean isLogFile(String fileName) {
        Pattern pattern = Pattern.compile(".*.log$");
        Matcher matcher = pattern.matcher(fileName);
        boolean b = matcher.matches();
//        boolean b = Pattern.matches(fileName, ".*.log$");
        return b;
    }
}
