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
        if(nums[mid]>nums[0]){
            s=mid+1;
        }else{
            e=mid;
        }
        mid=s+(e-s)/2;
    }
    return s;
    
}







int main(){
    vector<int> arr={4,5,6,7,0,1,2};
    cout<<findPivot(arr);
    cout<<arr.size();
}