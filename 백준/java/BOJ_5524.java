import java.util.Scanner;

/**
 * BOJ_5524
 */
public class BOJ_5524 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n =in.nextInt();
        for (int i = 0; i < n; i++) {
            String q=in.next();
            System.out.println(q.toLowerCase());
        }
        in.close();
    }
}