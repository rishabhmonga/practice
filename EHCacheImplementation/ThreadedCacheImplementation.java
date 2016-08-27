//package src.com.EHCacheImplementation;
//
//import net.sf.ehcache.*;
//
///**
//* Created by rism on 7/14/14.
//*/
//class BuildCache
//{
////    TODO: read about singleton cache manager
//
//    public static CacheManager cchMan = CacheManager.getInstance();
//
//    public BuildCache(String cchName)
//    {
//        cchMan.addCache(cchName);
//    }
//
//    public void put(String cchName, String key, String value)
//    {
//        Cache cache = cchMan.getCache(cchName);
//        cache.put(new Element(key, value));
//    }
//
//    public String get(String cchName, String key)
//    {
//        Cache cache = cchMan.getCache(cchName);
//        Element elt = cache.get(key);
//        return elt.getObjectValue().toString();
////        return elt.toString();
//    }
//}
//
//class CacheThread implements Runnable
//{
//    private String ThreadName;
//    private String ThreadKey;
//    private String ThreadValue;
////    private Thread t;
//
//    public CacheThread(String name, String key, String value)
//    {
//        this.ThreadName = name;
//        this.ThreadKey = key;
//        this.ThreadValue = value;
//    }
//
//    public void run()
//    {
//        System.out.println("(get)" + ThreadName + " :\t" + getValue(ThreadedCacheImplementation.BC, "Hello"));
//        updateElement();
//        System.out.println("(put)" + ThreadName + " :\t" + getValue(ThreadedCacheImplementation.BC, ThreadKey));
//    }
//
//    public void updateElement()
//    {
//        putElement(ThreadedCacheImplementation.BC, "Test", ThreadKey, ThreadValue);
//    }
//
//    private void putElement(BuildCache BC, String cchName, String key, String value)
//    {
//        BC.put(cchName, key, value);
//    }
//
//    private String getValue(BuildCache BC, String key)
//    {
//        return BC.get("Test", key);
//    }
//}
//
//public class ThreadedCacheImplementation
//{
//    public static BuildCache BC = new BuildCache("Test");
//
//    public static void main(String[] args)
//    {
//        BC.put("Test", "Hello", "World");
//        System.out.println("Cache: Test  Key: Hello  Value: " + BC.get("Test", "Hello"));
//        Thread t1 = new Thread(new CacheThread("Thread 1", "Hello" ,"First Thread"));
//        t1.start();
//        Thread t2 = new Thread(new CacheThread("Thread 2", "Hello", "Second Thread"));
//        t2.start();
//
//        BuildCache.cchMan.removeAllCaches();
//        BuildCache.cchMan.shutdown();
//    }
//
//}
