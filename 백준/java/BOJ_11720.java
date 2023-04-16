import java.util.Scanner;

public class BOJ_11720 {

    public static void main(String[] args) {
        Scanner in =new Scanner(System.in);

        int n = in.nextInt();
        String q = in.next();

        long s =0;
        for(int i=0; i<n; i++){
            s+= q.charAt(i)-'0';
        }
        System.out.println(s);
        in.close();
    }
}