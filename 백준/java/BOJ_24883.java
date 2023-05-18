import java.util.Scanner;

public class BOJ_24883 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String a=in.next();

        if (a.equals("n") || a.equals("N")) {
            System.out.println("Naver D2");
        }else{
            System.out.println("Naver Whale");
        }
        in.close();
    }
}
