#include <iostream>
using namespace std;
#include <vector>


// insertion sort not the best approches
void insertion_sort1(int arr[], int n)
{
    for (int i = 1; i < n; i++)
    {
        int key = arr[i];
        int j;
        for (j=i-1; j >=0; j--)
        {
            if (arr[j]>key)
            {
                arr[j+1]=arr[j];
            }else{
                break;
            }
        }
        arr[j+1]=key;
    }
}
// insertion sort best approches
void insertion_sort(int arr[], int n)
{
    for (int i = 1; i < n; i++)
    {
        int key = arr[i];
        int j = i - 1;
        
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            arr[j + 1] = arr[j];
            j--;
        }
        
        arr[j + 1] = key;
    }
}

int main()
{
    int arr[] = {5, 4, 3, 2, 1};
    int n = sizeof(arr) / sizeof(arr[0]);
    insertion_sort(arr, n);
    for (int i : arr)
    {
        cout << i;
    }
}
