import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BOJ_27889 {

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String n = br.readLine();
        if (n.equals("NLCS")) {
            System.out.println("North London Collegiate School");
        }else if (n.equals("BHA")) {
            System.out.println("Branksome Hall Asia"); 
        }else if (n.equals("KIS")) {
            System.out.println("Korea International School");           
        }else if(n.equals("SJA")){
            System.out.println("St. Johnsbury Academy");
        }
    }
}
//문자열 비교