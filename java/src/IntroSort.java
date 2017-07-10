import java.util.Random;

import static java.lang.Math.log;


public class IntroSort {

    public static int ARRAY_LENGTH = 10;
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
     * Call QuickSort
     * If recursion's depth >= log n,
     * then call HeapSort for O(n * loh n)
     */
    public static void main(String[] args) {
        initArray();
        printArray();

        QuickSort.intro_trigger = true;
        QuickSort.initSort();
        printArray();

        System.out.println("depth: " + QuickSort.depth);
        if (QuickSort.depth >= log(ARRAY_LENGTH)) {
            System.out.println(">>> change QuickSort to HeapSort");
            HeapSort.sort(array);
        }
        printArray();
    }
}
