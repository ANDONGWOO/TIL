import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;


public class BOJ_5597 {
        public static int[] removeDuplicates(int[] arr) {
            return Arrays.stream(arr).distinct().toArray();
        }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        List<Integer> a=new ArrayList<Integer>();
        List<Integer> b=new ArrayList<Integer>();
        for (int i = 0; i < 28; i++) {
            a.add(in.nextInt());
        }
        for (int i = 1; i < 31; i++) {
            b.add(i);
        }
        b.removeAll(a);
        for (Integer integer : b) {
            System.out.println(integer);
        }
        in.close();
    }
}