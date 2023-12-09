class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        
        // 첫 글자를 대문자로 시작하기 위해 'true'로 설정
        boolean isNewWord = true;
        
        for (char ch : s.toCharArray()) {
            if (ch == ' ') {
                isNewWord = true;
                answer.append(ch);
            } else {
                if (isNewWord) {
                    answer.append(Character.toUpperCase(ch));
                    isNewWord = false;
                } else {
                    answer.append(Character.toLowerCase(ch));
                }
            }
        }
        
        return answer.toString();
    }
}