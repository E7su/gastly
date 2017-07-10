import java.util.Random;

import static java.lang.Math.log;


public class QuickSort {
    public static int ARRAY_LENGTH = 10;
    public static double LOGN = log(ARRAY_LENGTH);

    // Trigger for IntroSort
    // If this sort call from IntroSort, then true
    public static boolean intro_trigger;
    public static int depth = 0;

    private static int[] array = new int[ARRAY_LENGTH];
    private static Random generator = new Random();


    /**
     * Init array with random values
     */
    public static void initArray() {
        for (int i = 0; i < ARRAY_LENGTH; i++) {
            array[i] = generator.nextInt(100);
        }
    }


    /**
     * Print array
     */
    public static void printArray() {
        for (int i = 0; i < ARRAY_LENGTH; i++) {
            System.out.print(array[i] + " ");
        }
        System.out.println();
    }


    /**
     * Get first and last elements of array and start sort
     */
    public static void initSort() {
        int startIndex = 0;
        int endIndex = ARRAY_LENGTH - 1;
        quickSort(startIndex, endIndex);
    }

    /**
     * QuickSort algorithm
     *
     * @param start - first element of array
     * @param end   - last element of array
     * @return sorted array
     */
    private static int[] quickSort(int start, int end) {
        int[] currentArray = new int[ARRAY_LENGTH];

        if (start >= end) {
            return new int[ARRAY_LENGTH];
        }

        // If this sort call from IntroSort, then check recursion's depth
        if (intro_trigger) {
            System.out.println("depth: " + depth + "; log n = " + LOGN);
            depth++;

            // Check recursion's depth
            // If recursion's depth >= log n, then call HeapSort for O(n * loh n)
            if (depth >= LOGN) {
                System.out.println(">>> max depth of recursion");
                currentArray = array;
                return currentArray;
            } else {
                currentArray = new int[ARRAY_LENGTH];
            }

        }

        int i = start, j = end;
        // because java.lang.StackOverflowError
        int supportElem = i - (i - j) / 2;

        // while i != supporting element
        // (if i == j, then i == supportElem == j)
        while (i < j) {

            // from left to right
            while ((array[i] <= array[supportElem]) && (i < supportElem)) {
                i++;
            }

            // from right to left
            while ((array[supportElem] <= array[j]) && (j > supportElem)) {
                j--;
            }

            // swap elements i <-> j
            swapElem(i, j);
            // select new supporting element
            supportElem = selectSupportElem(i, j, supportElem);
        }

        // quickSort left fragment
        quickSort(start, supportElem);
        // quickSort right fragment
        quickSort(supportElem + 1, end);
        return currentArray;
    }


    /**
     * Select new supporting element if i or j equal supporting element
     *
     * @param i           - index of the left element
     * @param j           - index of the right element
     * @param supportElem - supporting element
     * @return new supporting element
     */
    private static int selectSupportElem(int i, int j, int supportElem) {
        if (i == supportElem)
            supportElem = j;
        else if (j == supportElem)
            supportElem = i;
        return supportElem;
    }


    /**
     * Swap elements i <-> j
     *
     * @param i - index of the left element
     * @param j - index of the right element
     */
    private static void swapElem(int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }


    public static void main(String[] args) {
        initArray();
        printArray();
        initSort();
        printArray();
    }
}

