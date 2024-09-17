#include <iostream>
using namespace std;
#include <vector>

void bubble_sort(int arr[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        bool swaped = false;
        for (int j = 0; j < n - (i + 1); j++)
        {
            if (arr[j + 1] < arr[j])
            {
                swap(arr[j + 1], arr[j]);
                swaped = true;
            }
        }

        if (!swaped)
        {
            break;
        }
        cout << "Step" << i;
    }
}

int main()
{
    int arr[] = {6, 0, 3, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    bubble_sort(arr, n);
    cout << endl;
    for (int i : arr)
    {
        cout << i;
    }
}