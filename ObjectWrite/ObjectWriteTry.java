package ObjectWrite;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.InputStream;
import java.util.Map;
import java.util.Properties;

/**
 * Created by rism on 12/23/14.
 */
public class ObjectWriteTry {
    public static void main(String[] args) {
        File conf = new File("/Users/rism/file", "props.conf");
        Properties p = new Properties();
        InputStream fis = null;
        FileWriter fileWriter = null;
        try {
            fis = new FileInputStream(conf);
            p.load(fis);
            fileWriter = new FileWriter("/Users/rism/file/writeProps.conf");
            for (Map.Entry entry : p.entrySet()){
                fileWriter.write(entry.toString());
                fileWriter.write("\n");
            }
            fileWriter.flush();

            if (fileWriter != null) {
                fileWriter.close();
            }
            if (fis != null) {
                fis.close();
            }
        }
        catch (Exception e) {
            System.out.println("Exception: "+ e.getMessage() + " ## " + e.getCause());

        }
        finally {

        }
    }

}
