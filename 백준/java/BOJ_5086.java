import java.util.Scanner;

public class BOJ_5086 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (true) {
            int a=in.nextInt();
            int b=in.nextInt();
            if (a==0 && b==0) {
                break;
            }
            if (b % a == 0) {
                System.out.println("factor");//약수
            }else if(a%b==0){
                System.out.println("multiple");//배수
            }else{
                System.out.println("neither");//둘 다 아니라면
            }
        }
        in.close();
    }
}

//배수 약수