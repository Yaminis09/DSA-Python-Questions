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
