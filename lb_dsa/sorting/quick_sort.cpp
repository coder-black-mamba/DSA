#include <iostream>
#include <vector>

using namespace std;

int partition(vector<int> &arr , int low ,int high){
    // choose a pivovt 
    int pivot=arr[high];
    // index of the smaller elements an
    int i =low-1;

    for (int j = low; j <=high; j++)
    {
        if (arr[j]<pivot)
        {
            i++;
            swap(arr[i],arr[j]);
        }
        
    }
    swap(arr[i+1],arr[high]);
    return i+1;
    
}




void quickSort(vector<int>& arr,int low,int high){
    if (low<high)
    {
        // pi is the partion index
        int pi=partition(arr,low,high);
        // recursion call for samlelr elements
        quickSort(arr,low,pi-1);
        // recursion call for samlelr elements
        quickSort(arr,pi+1,high);
    }
    
}


int main(){
    vector<int> arr={4,5,3,2,8,1};
    int n=arr.size()-1;
    quickSort(arr,0,n);
    for(int i:arr){
        cout<<i;
    }
}