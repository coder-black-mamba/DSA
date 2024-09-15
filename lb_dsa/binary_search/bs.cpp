#include <iostream>
using namespace std;

int iterative_binary_search(int target, int arr[])
{
    int low = 0;
    int high = sizeof(arr) / sizeof(arr[0]);
    // if high = 2^31-1 and low = 2^31-1 so mid=high+low will overflow of integer range
    //
    // dont use this
    // int mid=(high+low)/2;
    // use this
    int mid = high + (low - high) / 2;
    while (high >= low)
    {
        if (arr[mid] == target)
        {
            return mid;
            break;
        }
        else if (arr[mid] > target)
        {
            high = mid - 1;
        }
        else if (arr[mid] < target)
        {
            low = mid + 1;
        }
        mid = high + (low - high) / 2;
    }
    return -1;

    return 0;
}

int main()
{
    int arr_r[] = {1, 2, 3, 4, 5};

    cout << iterative_binary_search(3, arr_r);
}