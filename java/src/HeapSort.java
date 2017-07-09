import java.util.Random;

public class HeapSort {
    private static int[] a;
    private static int n;
    private static int left;
    private static int right;
    private static int largest;

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

    // build heap
    public static void buildHeap(int[] a) {
        n = a.length - 1;
        for (int i = n / 2; i >= 0; i--) {
            System.out.println(i);
            getMaxFromHeap(a, i);
        }
    }

    // get max element from heap
    public static void getMaxFromHeap(int[] a, int i) {
        left = 2 * i;
        right = 2 * i + 1;

        if (left <= n && a[left] > a[i]) {
            largest = left;
        } else {
            largest = i;
        }

        if (right <= n && a[right] > a[largest]) {
            largest = right;
        }
        if (largest != i) {
            swap(i, largest);
            getMaxFromHeap(a, largest);
        }
    }

    // swap two elements
    public static void swap(int i, int j) {
        int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }

    // heap sort
    public static void sort(int[] array) {
        a = array;
        buildHeap(a);

        for (int i = n; i > 0; i--) {
            swap(0, i);
            n--;
            getMaxFromHeap(a, 0);
        }
    }

    public static void main(String[] args) {
        initArray();
        printArray();
        sort(array);
        printArray();
    }
}
