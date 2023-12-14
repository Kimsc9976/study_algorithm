class Solution {
    public int[] solution(int brown, int yellow) {
        int whole = brown + yellow;

        for (int width = whole; width >= 3; width--) {
            if (whole % width == 0) { // 세로 길이 계산 가능
                int height = whole / width;
                if ((width - 2) * (height - 2) == yellow) {
                    return new int[]{width, height};
                }
            }
        }
        return new int[]{0, 0}; // 정답을 찾지 못한 경우
    }
}