class Solution {
    public int[] solution(int brown, int yellow) {
        int whole = brown + yellow;
        int width = (int)Math.sqrt(whole);
        int height = width;

        while (width * height != whole || (width - 2) * (height - 2) != yellow) {
            if (width * height > whole) {
                height--;
            } else {
                width++;
            }
        }

        return new int[]{width, height};
    }
}