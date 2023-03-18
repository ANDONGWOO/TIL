import java.util.Scanner;
public class BOJ_11718 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        for(int i=0; i<100; i++){//입력 최대 100
            if (!in.hasNext()) {
                break; 
            }
            String q = in.nextLine();
            System.out.println(q);
        }
        in.close();
    }
}
// hasNext() 읽어올 요소가 남아있는지 여부  요소 있다 True 없다면 false
// if문에서 없다면 부정하고 True이면 break