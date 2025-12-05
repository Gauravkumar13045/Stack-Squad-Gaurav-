//  Write a program that takes an array as input and prints all its elements.

package Round1;

import java.util.Scanner;
import java.util.Arrays;

public class Ques1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the size of the array: ");
        int n = sc.nextInt();

        int[] newArray = new int[n];

        System.out.println("Enter " + n + " elements:");
        for (int i = 0; i < n; i++) {
            newArray[i] = sc.nextInt();

        }

        System.out.println("Entered Array : " + Arrays.toString(newArray));

        sc.close();
    }
}
