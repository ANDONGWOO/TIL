import java.math.BigInteger;
import java.util.Scanner;

public class BOJ_1271 {
    public static void main(String[] args) {
        Scanner in =new Scanner(System.in);
        BigInteger a = in.nextBigInteger();
        BigInteger b = in.nextBigInteger();

        System.out.println(a.divide(b));//나눗셈
        System.out.println(a.remainder(b));//나머지 
        in.close();
    }
}
