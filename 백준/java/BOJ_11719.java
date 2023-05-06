import java.util.Scanner;

public class BOJ_11719 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        for(int i=0; i<100; i++){//입력 최대 100
            if (!in.hasNext()) {
                break; 
            }
            String q = in.nextLine();
            System.out.println(q);
        }
        in.close();
    }
}
