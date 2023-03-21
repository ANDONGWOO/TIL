import java.util.Scanner;

public class BOJ_2908 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        int q=(a/100)+(a%10)*100+((a%100)/10)*10;
        int w=(b/100)+(b%10)*100+((b%100)/10)*10;
        if(q>w){
            System.out.println(q);
        }else{
            System.out.println(w);
        }
        in.close();
    }
}