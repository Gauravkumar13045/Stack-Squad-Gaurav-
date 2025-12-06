package Round1;

public class Ques4 {
    public static void main(String[] args) {
        int[] arr = {15, 10, 5, 25, 20};

        int min = arr[0];
        int max = arr[0];

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
            if (arr[i] > max) {
                max = arr[i];
            }
        }

        System.out.println("Minimum Value : " + min);
        System.out.println("Maximum Value : " + max);
    }
}

// i have assumed the min and max value to be the first one means arr[0] and then the loop will run and verify by tallying the number 
// whether it is maximum or minimum and at the it is printed.