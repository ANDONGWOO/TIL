
import java.util.Arrays;
import java.util.Scanner;

public class BOJ_2752 {

    public static void main(String[] args) {
        Scanner in =new Scanner(System.in);
        int[] q = new int[3];
        for (int i = 0; i < 3; i++) {
            q[i]=in.nextInt();
        }
        Arrays.sort(q);
        for (int j = 0; j < 3; j++) {
            System.out.print(q[j] +" ");
        }

        in.close();
    }
}