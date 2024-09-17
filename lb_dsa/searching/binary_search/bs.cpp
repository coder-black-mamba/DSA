#include <iostream>
using namespace std;
#include <vector>
// if high = 2^31-1 and low = 2^31-1 so mid=high+low will overflow of integer range
//
// dont use this
// int mid=(high+low)/2;
// use this
int binary_search(vector<int> nums, int target)
{
    int s = 0;
    int e = nums.size() - 1;

    int mid = s + (e - s) / 2;
    while (e >= s)
    {
        if (nums[mid] == target)
        {
            return mid;
            break;
        }
        else if (nums[mid] > target)
        {
            e = mid - 1;
        }
        else if (nums[mid] < target)
        {
            s = mid + 1;
        }
        mid = s + (e - s) / 2;
    }
    return -1;

    return 0;
}

int main()
{
    vector<int>arr = {1, 2, 3, 4, 5};

    cout << binary_search(arr,3);
}