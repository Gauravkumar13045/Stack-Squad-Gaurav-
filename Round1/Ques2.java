// Print Array Elements After Multiplying by 5
package Round1;

import java.util.Arrays;

public class Ques2 {
    public static void main(String[] args) {
        int[] arr = {5, 10, 15, 20, 25};
        int[] newArr = new int[arr.length];

        for (int i = 0; i < arr.length; i++) {
            newArr[i] = arr[i] * 5;
        }
        System.out.println("Output : " + Arrays.toString(newArr));
    }
}




