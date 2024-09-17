#include <iostream>
using namespace std;
#include <vector>

void selection_sort(int arr[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        int min_index = i;

        for (int j = i + 1; j < n; j++)
        {
            cout<<" J"<<j;
            cout<<"arr[j]"<<arr[j];
            if (arr[min_index] > arr[j])
            {
                min_index = j;
            }
        }

        swap(arr[min_index], arr[i]);
        cout<<endl;
    }
}

int main()
{
    int arr[] = {5, 3, 4, 8, 7, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    cout<<n;
    selection_sort(arr, n);
    for (int i : arr)
    {
        cout << i;
    }
}