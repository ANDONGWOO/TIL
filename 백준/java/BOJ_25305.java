import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class BOJ_25305 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        Integer[] c=new Integer[a];
        for (int i = 0; i < a; i++) {
            c[i]=in.nextInt();
        }
        Arrays.sort(c,Collections.reverseOrder());        
        System.out.println(c[b-1]);
        in.close();
    }
}