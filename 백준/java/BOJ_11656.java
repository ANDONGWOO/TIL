import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class BOJ_11656 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s =in.next();
        List<String> q=new ArrayList<String>();
        //s에서 요소 하나씩 버리면서
        for (int i = 0; i < s.length(); i++) {
            //리스트에 저장
            q.add(s.substring(i));
        }
        Collections.sort(q);
        //배열 사전순으로 정렬
        for (String i : q) {
            //리스트 하나씩 출력
            System.out.println(i);
        }
        in.close();
    }
}
//문자 자르기
//정렬
//리스트요소(반복문)