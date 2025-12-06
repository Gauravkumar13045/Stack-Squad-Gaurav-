// Given an array containing 0s and 1s, print all the 0s first and then all the 1s
package Round1;

import java.util.Arrays;

public class Ques5 {
    public static void main(String[] args) {
        int[] arr = { 1, 0, 1, 0, 0, 1 };

        for (int i = 0; i < arr.length - 1; i++) {
            int sort = i;
            for (int u = i + 1; u < arr.length; u++) {
                if (arr[sort] > arr[u]) {
                    sort = u;
                }

            }

            int acc = arr[i];
            arr[i] = arr[sort];
            arr[sort] = acc;

        }

        System.out.println("Output : " + Arrays.toString(arr));

    }
}

// Here i have used a very optimized approach of Selection Sort 
// As i have first swaps the number in the accending order accordingly and hence the answer comes ....

// Happy Coding !!!.....
