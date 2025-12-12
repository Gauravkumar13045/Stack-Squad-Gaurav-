//  Write a program that takes an array as input and prints all its elements.

package round1_gaurav;

import java.util.Arrays;
import java.util.Scanner;

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


// This is a java program as i am doing my DSA in java ....
// At first i have imported the important libaries as my need.
// Then as i have to take the input of my user as i have used the scanner function which will take the user input.
// After that i have asked the use that how many number he/she wants to input.
// According to that input i have run a loop in which my function will ask me that times to input.
// For Example : user inputs 5 then my function runs till the 5 number should be inputed.
// At the very last i have displayed it....

// Happy Coding !!!!.....
