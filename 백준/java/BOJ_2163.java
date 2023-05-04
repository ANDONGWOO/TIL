import java.util.Scanner;

public class BOJ_2163 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n =in.nextInt();
        int m =in.nextInt();
        int s=0;
        int a=n*m;

        while (true) {
            if (a==1) {//총조각 1이면 
                System.out.println(s);
                break;
            }else{//a는 총조각 1아니면 a-1/s+1
                a--;//1조각 -1빼고
                s++;//1조각 +1카운터
            }
        }
        in.close();
    }
}
