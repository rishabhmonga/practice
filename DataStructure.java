/**
 * Created by rism on 8/6/14.
 */

import java.util.*;

public class DataStructure
{
    // Create an array
    private final static int SIZE = 15;
    private int[] arrayOfInts = new int[SIZE];

    public DataStructure()
    {
        // fill the array with ascending integer values
        for (int i = 0; i < SIZE; i++)
        {
            arrayOfInts[i] = i;
        }
    }

    public void printEven()
    {
        final int count = 1;
        // Print out values of even indices of the array
        DataStructureIterator iterator = new DataStructureIterator()
        {
            @Override
            public boolean hasNext()
            {
                int i = count;
                return false;
            }

            @Override
            public Integer next()
            {
                return null;
            }

            @Override
            public void remove()
            {

            }
        };
        while (iterator.hasNext())
        {
            System.out.print(iterator.next() + " ");
        }
        System.out.println();
    }

    interface DataStructureIterator extends Iterator<Integer>
    {}

    // Inner class implements the DataStructureIterator interface,
    // which extends the Iterator<Integer> interface

    private class EvenIterator implements DataStructureIterator
    {
        // Start stepping through the array from the beginning
        private int nextIndex = 0;

        public boolean hasNext()
        {
            // Check if the current element is the last in the array
            return (nextIndex <= SIZE - 1);
        }

        @Override
        public void remove()
        {
        }

        public Integer next()
        {
            // Record a value of an even index of the array
            Integer retValue = Integer.valueOf(arrayOfInts[nextIndex]);

            // Get the next even element
            nextIndex += 2;
            return retValue;
        }
    }

    public static void main(String s[])
    {
        // Fill the array with integer values and print out only
        // values of even indices
        DataStructure ds = new DataStructure();
        ds.printEven();
    }
}
