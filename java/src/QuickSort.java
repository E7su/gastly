import java.util.Random;


public class QuickSort {
    public static int ARRAY_LENGTH = 10;
    private static int[] array = new int[ARRAY_LENGTH];
    private static Random generator = new Random();

    // init array with random values
    public static void initArray() {
        for (int i = 0; i < ARRAY_LENGTH; i++) {
            array[i] = generator.nextInt(100);
        }
    }

    public static void printArray() {
        for (int i = 0; i < ARRAY_LENGTH; i++) {
            System.out.print(array[i] + " ");
        }
        System.out.println();
    }

    // get first and last elements of array and start sort
    public static void initSort() {
        int startIndex = 0;
        int endIndex = ARRAY_LENGTH - 1;
        quickSort(startIndex, endIndex);
    }

    private static void quickSort(int start, int end) {
        if (start >= end)
            return;
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
    }

    /**
     * select new supporting element if i or j equal supporting element
     */
    private static int selectSupportElem(int i, int j, int supportElem) {
        if (i == supportElem)
            supportElem = j;
        else if (j == supportElem)
            supportElem = i;
        return supportElem;
    }

    /**
     * swap elements i <-> j
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
