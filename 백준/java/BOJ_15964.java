import java.util.Scanner;

public class BOJ_15964 {
    public static void main(String[] args) {
        Scanner in =new Scanner(System.in);

        int a=in.nextInt();
        int b=in.nextInt();
        int c;
        c=(a+b)*(a-b);
        System.out.println(c);
        in.close();
    }
}
