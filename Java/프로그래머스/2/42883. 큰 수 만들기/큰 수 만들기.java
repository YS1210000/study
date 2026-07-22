import java.util.Stack;

class Solution {
    public String solution(String number, int k) {
        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < number.length() ; i++){
            char nowChar = number.charAt(i);

            while (sb.length() > 0 && k > 0 && nowChar > sb.charAt(sb.length()-1)){
                sb.deleteCharAt(sb.length()-1);
                k--;
            }

            sb.append(nowChar);

        }

        return sb.substring(0, sb.length() - k);
    }
}