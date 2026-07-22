class Solution {
    public int solution(String name) {
        int answer = 0;
        int n = name.length();
        int minMove = n - 1; //기본값 : 순서대로 오른쪽으로만 이동하는 경우

        for(int i = 0; i < n; i++){ //문자열 전체를 탐색하기 위한 크기
            char c = name.charAt(i);

            answer += Math.min(c - 'A', 'Z' - c + 1); //위로 탐색 횟수, 아래로 탐색 횟수

            int next = i + 1;
            while(next < n && name.charAt(next) == 'A'){
                next++;
            }

            minMove = Math.min(minMove, i * 2 + (n - next)); //오른쪽으로 갔다가 -> 다시 돌아왔다가 -> 왼쪽으로 이동
            minMove = Math.min(minMove, (n - next) * 2 + i); //왼쪽으로 갔다가 -> 다시 돌아왔다가 -> 오른쪽으로 이동

        }


        return answer + minMove;
    }
}