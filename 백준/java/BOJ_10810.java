
import java.util.Scanner;

public class BOJ_10810 {

    public static void main(String[] args) {
        Scanner in =new Scanner(System.in);
        int n=in.nextInt();
        int m=in.nextInt();
        int[] q=new int[n];
        for (int i = 0; i < q.length; i++) {
            q[i]=0;
        }
        for (int i = 0; i < m; i++) {
            int a=in.nextInt()-1;
            int b=in.nextInt();
            int c=in.nextInt();
            for (; a < b; a++) {
                q[a]=c;
            }
        }
        for (int i = 0; i < q.length; i++) {
            System.out.print(q[i]+" ");
        }


        in.close();
    }
}
//0 배열