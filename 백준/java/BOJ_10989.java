import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ_10989 {

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());
        int q[] =new int[t];

        for (int i = 0; i < t; i++) {//for 반복
            q[i]=Integer.parseInt(br.readLine());
        }
        Arrays.sort(q);
        for(int i : q) {//for 요소
			sb.append(i).append('\n');
		}
		System.out.println(sb);
    }
}
