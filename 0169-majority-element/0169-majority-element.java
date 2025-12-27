class Solution {
    public int majorityElement(int[] nums) {
        int n = nums.length/2;
        int i = 0;
        int j = i;
        int count = 0;
        int val;

        for(i = 0; i < nums.length; i++){
            count = 0;
            val = nums[i];
            for(j = i; j < nums.length; j++){
                if(nums[j] == val){
                    count++;
                }
            }
            if(count > n){return(nums[i]);}
        }
        return 0;

    }
}