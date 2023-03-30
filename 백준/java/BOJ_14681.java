import java.util.Scanner;

public class BOJ_14681 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int x =in.nextInt();
        int y =in.nextInt();
        if(x>0 && y>0){//양수 양수
            System.out.println(1);
        }else if(x>0 && y<0){//양수 음수
            System.out.println(4);  
        }else if(x<0 && y>0){//음수 양수
            System.out.println(2);
        }else if(x<0 && y<0){//음수 음수
            System.out.println(3);
        }

        in.close();
    }
}
