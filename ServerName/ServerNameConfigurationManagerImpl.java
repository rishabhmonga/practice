//package ServerName;
//
//import java.io.File;
//import java.io.FileInputStream;
//import java.io.IOException;
//import java.io.InputStream;
//import java.util.Properties;
//
///**
// * Created by rism on 12/18/14.
// */
//public class ServerNameConfigurationManagerImpl implements ConfgurationManager {
//    private static String Property_Server_Name_1 = "wrapper.app.parameter.6";
//    private static String Property_Server_Name_2 = "wrapper.app.parameter.13";
//    public static final String Server_Name = ConfigurationTypesFactory.Server_Name;
//
//    private ConfigurationType configurationType;
//
//
//
//    public void setServer_Name(RuntimeComponentEx runtimeComponent, String server_name) {
//        File customWrapperConf = new File(AccessCustomWrapper.getRootDirectoryContext(runtimeComponent.getProduct()));
//        Properties p = new Properties();
//        InputStream fis = null;
//        try{
//            fis = new FileInputStream(customWrapperConf);
//            p.load(fis);
//            p.setProperty(Property_Server_Name_1, server_name);
//            p.setProperty(Property_Server_Name_2, server_name);
//
//        }
//        catch (Exception e){
//
//        }
//    }
//}
