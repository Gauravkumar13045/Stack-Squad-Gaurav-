
package round1_gaurav;

import java.util.Arrays;

public class Ques6 {
    public static void main(String[] args) {
        int arr[] = { -1, 2, -3, 4, -5, 6 };

        int neg = 0, pos = arr.length - 1;

        while (neg <= pos) {
            if (arr[neg] < 0) {
                neg++;
            } else {
                int sort = arr[neg];
                arr[neg] = arr[pos];
                arr[pos] = sort;
                pos--;
            }
        }
        System.out.println("Sorted Array (Red-White-Blue): " + Arrays.toString(arr));

    }
}
