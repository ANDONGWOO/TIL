import java.util.Scanner;

public class BOJ_2475 {

    public static void main(String[] args) {
        Scanner in =new Scanner(System.in);
        int s=0;
        for (int i = 0; i < 5; i++) {//고유 번호 5자리
            int q =in.nextInt();
            s+=Math.pow(q, 2);//5자리 2제곱 총합s           
        }
        System.out.println(s%10);//s/10 나머지 출력
        in.close();
    }
}