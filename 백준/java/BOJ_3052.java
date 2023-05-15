
import java.util.HashSet;
import java.util.Scanner;

public class BOJ_3052 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        HashSet<Integer> b = new HashSet<>();//중복 허용x
        for (int i = 0; i < 10; i++) {//입력수
            int a=in.nextInt();
            b.add(a%42);//추가 
        }
        System.out.println(b.size());//길이
        in.close();
    }
}

//set