import java.util.Scanner;

public class BOJ_10951 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (in.hasNext()) {
            //입력값이 있으면 True
            //없다 False 
            int a= in.nextInt();
            int b= in.nextInt();
            System.out.println(a+b);
        }
        in.close();
    }
}