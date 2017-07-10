import java.util.Random;

public class HeapSort {
    private static int n;
    private static int left;
    private static int right;
    private static int largest;

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
            System.out.print(HeapSort.array[i] + " ");
        }
        System.out.println();
    }


    /**
     * Build heap
     *
     * @param array - array for sort
     */
    public static void buildHeap(int[] array) {
        n = array.length - 1;
        for (int i = n / 2; i >= 0; i--) {
            getMaxFromHeap(array, i);
        }
    }


    /**
     * Get max element from heap
     *
     * @param array - array for sort
     * @param i     - lvl
     */
    public static void getMaxFromHeap(int[] array, int i) {
        left = 2 * i;
        right = 2 * i + 1;

        if (left <= n && array[left] > array[i]) {
            largest = left;
        } else {
            largest = i;
        }

        if (right <= n && array[right] > array[largest]) {
            largest = right;
        }
        if (largest != i) {
            swap(i, largest);
            getMaxFromHeap(array, largest);
        }
    }


    /**
     * Swap two elements
     *
     * @param i - left element
     * @param j - right element
     */
    public static void swap(int i, int j) {
        int tmp = array[i];
        array[i] = array[j];
        array[j] = tmp;
    }


    /**
     * Heap sort
     *
     * @param array - array for sort
     * @return sorted array
     */
    public static int[] sort(int[] array) {
        buildHeap(array);

        for (int i = n; i > 0; i--) {
            swap(0, i);
            n--;
            getMaxFromHeap(array, 0);
        }
        return array;
    }


    public static void main(String[] args) {
        initArray();
        printArray();
        array = sort(array);
        printArray();
    }
}

