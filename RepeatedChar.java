package src.com;

/**
 * Created by rism on 7/21/14.
 */
public class RepeatedChar
{
    public static void main(String[] args)
    {
        System.out.println(findStart("aaabbbbbbcddccc"));
        System.out.println(findStart("vfdaaafgggbbb"));
    }

    private static int findStart(String str)
    {
        int start = 0;
        int[] len = new int[str.length()];
        len[0] = 1;
        for(int i = 1; i < str.length(); i++)
        {
            if(str.charAt(i) == str.charAt(i-1))
            {
                len[i] = len[i-1]+1;
            }
            else
            {
                len[i] = 1;
            }
        }
        int max = len[0];

        for(int i = 0; i < len.length; i++)
        {
            if(len[i] > max)
            {
                max = len[i];
                start = i;
            }
            System.out.print(len[i]);
        }
        System.out.print("\t");
        return start - len[start] + 1;
    }
}
