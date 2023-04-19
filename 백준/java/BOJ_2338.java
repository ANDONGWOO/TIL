import java.math.BigInteger;
import java.util.Scanner;

public class BOJ_2338 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        BigInteger a = in.nextBigInteger();//int범위 x 10진수로 1,000자리
        BigInteger b = in.nextBigInteger();//int범위 x 10진수로 1,000자리

        System.out.println(a.add(b));
        System.out.println(a.subtract(b));
        System.out.println(a.multiply(b));
        in.close();
    }
}
