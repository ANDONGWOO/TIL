import java.util.Scanner;

public class BOJ_10156 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a=in.nextInt();
        int b=in.nextInt();
        int c=in.nextInt();
        if (a*b-c<=0) {
            System.out.println(0);
        }else{
            System.out.println(a*b-c);
        }
        in.close();
    }
}