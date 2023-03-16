import java.util.Scanner;

public class BOJ_9498 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        byte q = in.nextByte();//100이하 수
        if(100>=q && 90<=q){
            System.out.println("A");
        }else if(89>=q && 80<=q){
            System.out.println("B");
        }else if(79>=q && 70<=q){
            System.out.println("C");
        }else if(69>=q && 60<=q){
            System.out.println("D");
        }else if(q<=59){
            System.out.println("F");
        }
        in.close();
    }
}
// q 자료형 byte 100이하 수
// &&는 and연산자 
