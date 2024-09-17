// Questions Solved:
// - Find Pivot in an Sorted & Rotated Array using Binary Search
// - Search an Element in a Sorted & Rotated array using Binary Search
// - Find Square Root of an Integer[both int & floating part] using Binary Search
#include <iostream>
using namespace std;
#include <vector>

// Pivot Finding Function
int findPivot(vector<int>& nums){
    int s=0;
    int e = nums.size()-1;
    int mid=s+(e-s)/2;

    while (s<e)
    {
        if(nums[mid]>=nums[0]){
            s=mid+1;
        }else{
            e=mid;
        }
        mid=s+(e-s)/2;
    }
    return s;
    
}
int binary_search(vector<int> nums , int target , int s , int e)
{
    
    
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







int main(){
    vector<int> arr={4,5,6,7,0,1,2};
    int target=6;
    int pivot=findPivot(arr);
    int n=arr.size();
    
    if(target>=arr[pivot] && target<=arr[n-1]){
        return binary_search(arr,target,pivot,n-1);
    }else{
        return binary_search(arr,target,0,pivot-1);

    }
}