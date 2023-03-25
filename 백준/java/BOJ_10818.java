
import java.util.Arrays;
import java.util.Scanner;

public class BOJ_10818 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int[] q = new int[a];
        for(int i=0; i<a; i++){
            q[i]=in.nextInt();
        }
        Arrays.sort(q);
        System.out.println(q[0]+" "+q[a-1]);
        in.close();
    }
}
