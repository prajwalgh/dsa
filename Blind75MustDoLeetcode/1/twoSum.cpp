#include <vector>
#include <iostream>
#include <map>
using namespace std;
class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        map<int, int> index;
        int size1 = nums.size();
        for (int i = 0; i < size1; i++)
        {
            int diff = target - nums[i];
            if (index.find(diff) != index.end())
            {
                return {i, index[diff]};
            }
            else
            {
                index[nums[i]] = i;
            }
        }
        return {};
    }
};