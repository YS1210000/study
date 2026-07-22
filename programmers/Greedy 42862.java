class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        int[] student = new int[n+1]; //최대 학생 30명 : 1 ~ 30 사용, -1 = 도난당한 학생, 0 = 체육복을 입은 학생, 1 = 여분이 있는 학생

        for(int i = 0; i < lost.length; i++){
            if(student[lost[i]] == 0){
                student[lost[i]] = -1; //도난당한 학생
            }
        }
        for(int j = 0; j < reserve.length; j++){
            if(student[reserve[j]] == 0){
                student[reserve[j]] = 1; //여분이 있어 빌려줄 수 있는 학생
            }
            else if(student[reserve[j]] == -1){
                student[reserve[j]] = 0; //여분이 있으나 자신이 도난당한 학생 = 자신이 입게 됨
            }
        }

        for(int count = 1; count < student.length; count++){
            if(student[count] == 0 || student[count] == 1){
                answer++;
            }
            else if(student[count] == -1){
                if(count-1 > 0 && student[count-1] == 1){ //앞에서 발리기
                    student[count] = 0;
                    student[count-1] = 0;
                    answer++;
                }
                else if(count+1 < student.length && student[count+1] == 1){ //뒤에서 발리기
                    student[count] = 0;
                    student[count+1] = 0;
                    answer++;
                }


            }
        }

        return answer;
    }
}