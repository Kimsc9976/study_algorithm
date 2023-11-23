import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        
        Map<String, HashSet<String>> hm = new HashMap<String, HashSet<String>>();
        Map<String, Integer> reportCount = new HashMap<String, Integer>();
        
        for (int n = 0; n < report.length; n ++){
            String reportInfo = report[n];
            String[] _report = reportInfo.split(" ");
            String reporter = _report[0];
            String target = _report[1];
            
            HashSet<String> targets = hm.getOrDefault(reporter, new HashSet<>());
            targets.add(target);
            hm.put(reporter, targets);
        } 
        
        for (String key : hm.keySet()) {
            HashSet<String> targets = hm.get(key);
            
            for (String target : targets){
                Integer cnt = reportCount.getOrDefault(target, 0);
                cnt ++;
                reportCount.put(target, cnt);
            }
        }

    for (int i = 0; i < id_list.length; i++) {
        String reporter = id_list[i];
        HashSet<String> targets = hm.getOrDefault(reporter, new HashSet<>());
        int c = 0;

        for (String target : targets) {
            Integer cnt = reportCount.getOrDefault(target, 0);
            if (cnt >= k) {
                c++;
            }
        }
        answer[i] = c;
    }
        
        
        return answer;
    }
}