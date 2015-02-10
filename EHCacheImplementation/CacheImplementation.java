//package EHCacheImplementation;
//
//import net.sf.ehcache.*;
//import net.sf.ehcache.config.CacheConfiguration;
//
///**
//* Created by rism on 7/11/14.
//*/
//public class CacheImplementation
//{
//    public static void main(String[] args)
//    {
//        CacheManager cchMan = CacheManager.getInstance();
//
//        cchMan.addCache("Test");
//
//        Cache cch = cchMan.getCache("Test");
//
//        CacheConfiguration config = cch.getCacheConfiguration();
//        config.setTimeToIdleSeconds(60);
//        config.setTimeToLiveSeconds(120);
//        config.setMaxEntriesLocalHeap(10000);
//        config.setMaxEntriesLocalDisk(1000000);
//
//        cch.put(new Element("Hello", "World"));
//
//        Element elt = cch.get("Hello");
//
////        String str = elt.getObjectValue().toString();
//        String str = (elt == null ? null : elt.getObjectValue().toString());
//
//        System.out.println(str);
//        String str2 = cch.get("Hello").toString();
//        System.out.println(str2);
//        System.out.println(cch.getName());
//
//
//
//        cchMan.removeAllCaches();
////        cchMan.shutdown();
//
//    }
//}
