import java.util.Scanner;

public class BOJ_9655 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int s = in.nextInt();
        if(s%2==0){
            System.out.println("CY");
        }else{
            System.out.println("SK");
        }
        in.close();
    }
}