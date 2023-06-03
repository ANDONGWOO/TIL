import java.util.Scanner;

public class BOJ_2845 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a=in.nextInt();
        int b=in.nextInt();

        for (int i = 0; i < 5; i++) {//정수 5개
            int q= in.nextInt();
            System.out.print(q-(a*b)+" ");//q-(a*b)공백 출력 5번반복한다
        }
        in.close();
    }
}
