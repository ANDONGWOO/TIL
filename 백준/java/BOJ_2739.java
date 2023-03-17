import java.util.Scanner;

public class BOJ_2739 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        byte n= in.nextByte();
        for(byte j=1; j<10; j++){
            System.out.println(n+" * "+j+" = "+n*j);
        }
        in.close();
    }
}
// n 1이상 9이하 byte 자료형 
// n*j n곱하기 j 1씩 증가하면서 반복