import java.util.Scanner;

public class BOJ_24723 {
    public static void main(String[] args) {
        Scanner in =new Scanner(System.in);
        int s= in.nextInt();
        int q= (int)Math.pow(2, s);//(int)제곱  (int)없다면 소수점으로 출력
        System.out.println(q);
        in.close();
    }
}
//제곱