class Solution {
    public List<Integer> majorityElement(int[] nums) {
        Arrays.sort(nums);

        int i = 0;
        int value;
        int count;
        int j;
        List<Integer> output = new ArrayList<>();
        while(i < nums.length){
            value = nums[i];
            count = 1;
            j = i;
            while(j+1 < nums.length && nums[j] == nums[j+1]){
                j++;
                count++;
            }
            if (count > nums.length/3){
                output.add(value);
            }
            i = j+1;
        }
        return output;
    }
}