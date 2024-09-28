class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int i=0,j=0,n=nums.size();
        int ans=INT_MIN,cur=0;
        while(j<n)
        {
            cur+=nums[j];
            ans=max(ans,cur);
            while(cur<0)
            {
                cur-=nums[i];
                i++;
            }
            j++;
        }
        return ans;
    }
};