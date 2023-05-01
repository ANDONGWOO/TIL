import java.util.Scanner;

public class BOJ_1978 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int q;
        int w=0;
        for (int i = 0; i < n; i++) {
            q = in.nextInt();
            for (int j = 2; j <= q; j++) {
                if(j==q){
                    w++;
                }
                if (q%j==0) {
                    break;
                }
            }
        }
        System.out.println(w);
        in.close();
    }
}