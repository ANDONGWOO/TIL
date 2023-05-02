import java.util.Scanner;

public class BOJ_27294 {

    public static void main(String[] args) {
        Scanner in =new Scanner(System.in);
        int a=in.nextInt();
        int b=in.nextInt();

        if(b==0 &&(a>=12 && a<=16)){
            System.out.println(320);
        }else{
            System.out.println(280);
        }
        in.close();
    }
}