class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        
        for(int i = 0; i < n; i ++){
            System.out.println(x);
            answer[i] = (long)(i+1) * x;

        }
        
        return answer;
    }
}