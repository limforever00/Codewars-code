package saturday0603;

import java.util.Arrays;

public class intervals {

	public static int sumIntervals(int[][] intervals) {
	    if (intervals == null || intervals.length == 0) {
	        return 0;
	    }

	    // 구간을 시작 시간별로 정렬
	    Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

	    int res = 0;
	    int currentStart = intervals[0][0];
	    int currentEnd = intervals[0][1];

	    // 겹치는 구간이 있으면 마지막에 한번에 계산하고
	    // 별개의 구간은 ELSE문에서 각각을 바로 처리 
	    // 길이만큼 FOR문 돌면서 계산하면 3개이상 겹치는 구간을 제외하기가 쉽지않아서 이렇게 수정
	    for (int i = 1; i < intervals.length; i++) {
	        if (intervals[i][0] <= currentEnd) {
	        	//intervals[i][0] 기준으로 sort했기때문에 작은수부터 시작	
	            currentEnd = Math.max(currentEnd, intervals[i][1]);
	            System.out.println("여기는 if문이야 " + currentEnd);
	        } else {
	            // 겹치지 않는 구간, 이전 구간의 길이를 ret에 더함
	        	System.out.println("여기는 안겹치는 구간인가 ?" + intervals[i][0]);
	        	res += currentEnd - currentStart;

	            // 새로운 구간 시작
	            currentStart = intervals[i][0];
	            currentEnd = intervals[i][1];
	        }
	    }

	    // 마지막 구간의 길이를 더함
	    res += currentEnd - currentStart;

	    return res;
	}

	public static void main(String[] args) {
	    int[][] arr = new int[][]{{-7, 8}, {-2, 5}, {5, 13}, {15,16} };

	    if (sumIntervals(arr) == 22) {
	        System.out.println("정답");
	    } else {
	        System.out.println("오답");
	    }
	}

}
