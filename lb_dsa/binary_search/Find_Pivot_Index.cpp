
// #include <iostream>
// using namespace std;
// #include <vector>

// int pivotIndex(vector<int> &nums)
// {
//     // easy methoad
//     int total_sum = 0;
//     for (int ele : nums)
//     {
//         total_sum += ele;
//     };

//     int left_sum = 0;

//     for (int i = 0; i < nums.length; i++)
//     {
//         if (left_sum * 2 == totalSum - nums[i])
//             return i; // Return the pivot index...
//         left_sum += nums[i];
//     }

//     return -1;
// }

// int main()
// {
//     vector<int> arr = {1, 7, 3, 6, 5, 6};
//     cout << pivotIndex(arr);
// }