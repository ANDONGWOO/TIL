import java.util.Scanner;

public class BOJ_11943 {
    public static void main(String[] args) {
        Scanner in =new Scanner(System.in);
        int a=in.nextInt();
        int b=in.nextInt();
        int c=in.nextInt();
        int d=in.nextInt();
        int min;
        if (a+d>b+c){
            min=b+c;
        }else{
            min=a+d;
        }
        System.out.println(min);
        in.close();
    }
}
