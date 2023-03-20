import java.util.Scanner;

public class BOJ_10869 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        short a = in.nextShort();
        short b = in.nextShort();
        System.out.println(a+b);
        System.out.println(a-b);
        System.out.println(a*b);
        System.out.println(a/b);
        System.out.println(a%b);
        in.close();
    }
}
