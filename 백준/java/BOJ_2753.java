import java.util.Scanner;

public class BOJ_2753 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        short q= in.nextShort();//4000이하수
        if(q%4==0 && q%100!=0){
            System.out.println("1");
        }else if(q%400==0){
            System.out.println("1");
        }
        else{
            System.out.println("0");
        } 
        in.close();
    }
}
// q 자료형 short 4000이하 수
// 윤년이면 1 아니면 0
// %나눈 후 나머지