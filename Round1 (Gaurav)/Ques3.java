//  Write a program to find whether a given target value exists in the array or not.


package Round1;

public class Ques3 {
    public static void main(String[] args) {
        int[] arr = {5, 10, 15, 20, 25};
        int target = 15;
        int index = -1;

        for (int i = 0; i < arr.length; i++) {
            if(target == arr[i] ){
                index = i;
                break;
            }
            
        }


        if(index >= 0){
                    System.out.println("Target found at : " + index);

        }else{
            System.out.println("No match found");
        }
    }
}

// I hv to find the index of the target value okii 
// So, i have taken a array, a target value, a index;
// index to be taken as -1 coz a -ve value tells us that the number is out of array.
// Concept:
// A for loop will run until it matches the number if found it will breaks and goes to if statement and prints it's index 
// Otherwise it will goes as a else statement stating that no match found ....

// Happy Coding !!!!....