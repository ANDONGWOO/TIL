import java.util.Scanner;

public class BOJ_11021 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n =in.nextInt();
        for(int i=1; i<=n; i++){
            int a =in.nextInt();
            int b =in.nextInt();
            System.out.println("Case #" +i+ ": " + (a+b));
        }
        in.close();
    }
}
