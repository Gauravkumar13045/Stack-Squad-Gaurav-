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


// This is a java program as i am doing my DSA in java ....
// i have taken a array ok... then i have taken a new array empty so that i could copy the output in it ... 
// bcoz in array nothing can be directly altered in it we have to copy the output . 
// So, at last i have taken a loop which continuously run till it mutiply every number in the array.
// At the end : - Simple print statement !!!

// Happy Coding !!!!......

