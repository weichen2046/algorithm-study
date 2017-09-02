class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        quickSort(nums, 0, nums.size() - 1);
        int sum = 0;
        for (int i=0; i<nums.size();) {
            sum += nums[i];
            i += 2;
        }
        return sum;
    }

    void quickSort(vector<int>& nums, int left, int right) {
        if (left >= right) {
            return;
        }
        int p = partion(nums, left, right);
        quickSort(nums, left, p - 1);
        quickSort(nums, p + 1, right);
    }

    int partion(vector<int>& nums, int left, int right) {
        int pivot = left + (right - left) / 2;
        int pivotVal = nums[pivot];

        // exchange the value of index pivot and right
        int tmp = nums[pivot];
        nums[pivot] = nums[right];
        nums[right] = tmp;

        int finalPosOfPivotVal = left;

        for (int i = left; i < right; i++) {
            if (nums[i] <= pivotVal) {
                if (i != finalPosOfPivotVal) {
                    int tmp = nums[finalPosOfPivotVal];
                    nums[finalPosOfPivotVal] = nums[i];
                    nums[i] = tmp;
                }
                finalPosOfPivotVal++;
            }
        }

        // make the pivot value to right position
        tmp = nums[finalPosOfPivotVal];
        nums[finalPosOfPivotVal] = nums[right];
        nums[right] = tmp;

        return finalPosOfPivotVal;
    }
};