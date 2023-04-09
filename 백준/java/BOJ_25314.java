import java.util.Scanner;

public class BOJ_25314 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n =in.nextInt();
        in.close();
        for(int i=0; i<n;i++){
            if(i%4==0){
                System.out.print("long ");
            }
        }
        System.out.println("int");

    }
}