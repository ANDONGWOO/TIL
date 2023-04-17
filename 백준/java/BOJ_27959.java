import java.util.Scanner;

public class BOJ_27959 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        if(n*100>=m){//100원 동전 n*100  크거나 같다
            System.out.println("Yes");
        }else{
            System.out.println("No");
        }
        in.close();
    }
}