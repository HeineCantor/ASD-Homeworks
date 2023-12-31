#include <iostream>
#define MIN -9999999

int max(int a, int b) {
    if (a > b) return a;
    else return b;
};

int max(int a, int b, int c) {
    return max(max(a, b), c);
};


int maxMidSum(int* a, int start, int mid, int end) {

    int sum = 0;
    int left_sum = MIN;

    for (int i = mid; i >= start; i--) {
        sum += a[i];
        if (sum > left_sum)
            left_sum = sum;
    }

    sum = 0;
    int right_sum = MIN;

    for (int i = mid ; i <= end; i++) {
        sum += a[i];
        if (sum > right_sum)
            right_sum = sum;
    }
    return max(left_sum + right_sum - a[mid], left_sum, right_sum);
};


int maxSum(int* a, int start, int end) {

    if (start == end)
        return a[start];

    int mid = (start + end) / 2;

    return max(maxSum(a, start, mid), maxSum(a, mid + 1, end), maxMidSum(a, start, mid, end));
};



int main()
{
    
    int array[] = { 13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7 };

    int n = sizeof(array) / sizeof(int);

    std::cout << "max sum is: " << maxSum(array, 0, n - 1);

}
