import java.util.Arrays;
import java.util.Scanner;

public class BOJ_2750 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int q[] =new int[n];
        for(int i=0; i<n; i++){
            q[i] = in.nextInt();
        }
        Arrays.sort(q);
        for(int i=0; i<n; i++){
            System.out.println(q[i]);
        }
        in.close();
    }
}
