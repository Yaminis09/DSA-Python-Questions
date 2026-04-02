class MaxElement {

    public static int findMax(int[] arr) {
        int element_max = arr[0];

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > element_max) {
                element_max = arr[i];
            }
        }
        return element_max;
    }

    public static void main(String[] args) {
        int[] arr = {-3, 7, 2, 9, 4};
        System.out.println(findMax(arr));
    }
}

/*
class Main {
    public static void main(String[] args) {
        int[] arr = {-3, 7, 2, 9, 4};
        int element_max = arr[0];
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > element_max) {
                element_max = arr[i];
            }
        }
        System.out.println(element_max);  
    }
}
*/
