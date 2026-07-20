import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;

class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        Map<String, Integer> scores = new LinkedHashMap<>();

        scores.put("RT", 0); //음수 및 0이 좌측(R), 1이상일 경우 우측(T), 이하 동일
        scores.put("CF", 0);
        scores.put("JM", 0);
        scores.put("AN", 0);

        //기능 구현 요
        for(int i = 0; i < survey.length; i++) {
            String st = survey[i];
            int val = choices[i] - 4; //범위가 1 - 7 이므로 -3 - 3 으로 조정

            char a = st.charAt(0);
            char b = st.charAt(1);

            String now = "";
            if(!scores.containsKey(st)) {
                now += b;
                now += a;
                val = -val;
            }
            else {
                now = st;
            }

            scores.put(now, scores.get(now) + val);


        }

        for (Map.Entry<String, Integer> entry : scores.entrySet()) {
            String key = entry.getKey();
            int value = entry.getValue();

            if (value > 0) {
                answer += key.charAt(1);
            }
            else {
                answer += key.charAt(0);
            }

        }

        return answer;
    }
}