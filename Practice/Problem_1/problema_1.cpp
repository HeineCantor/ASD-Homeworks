#include <iostream>
#include <math.h>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

void merge(int* array, int start, int middle, int end)
{
    int lengthL = middle - start + 1;
    int lengthR = end - middle;

    int fullLength = lengthL + lengthR;

    int i, j, k;

    int* leftArray = new int(lengthL);
    int* rightArray = new int(lengthL);

    for(i = 0; i < lengthL; i++)
        leftArray[i] = array[start + i];
    
    for(j = 0; j < lengthR; j++)
        rightArray[j] = array[middle + 1 + j];

    i = j = 0;
    k = start;

    for(k = start; k <= end; k++)
    {
        if(i < lengthL && j < lengthR)
        {
            if(leftArray[i] <= rightArray[j])
            {
                array[k] = leftArray[i];
                i++;
            }
            else
            {
                array[k] = rightArray[j];
                j++;
            }
        }
        else
        {
            if(i < lengthL)
            {
                array[k] = leftArray[i];
                i++;
            }
            else
            {
                array[k] = rightArray[j];
                j++;
            }
        }
    }

    free(leftArray);
    free(rightArray);
}

void mergeSort(int* array, int start, int end)
{
    if(start >= end)
        return ;

    int middle = (start + end) / 2;

    mergeSort(array, start, middle);
    mergeSort(array, middle + 1, end);
    merge(array, start, middle, end);
}

void printVector(int* array, int length)
{
    cout << "[";

    for(int i = 0; i < length; i++)
    {
        cout << array[i];

        if(i < length - 1)
            cout << ", ";
    }

    cout << "]" << endl;
}

inline int findMedian(int* array, int length)
{
    if(length % 2 == 1)
        return array[length / 2];
    else
        return (array[length / 2 - 1] + array[length / 2]) / 2;
}

int sumOfMinimumDistances(int* array, int length, int median)
{
    int sum = 0;

    for(int i = 0; i < length; i++)
        sum += abs(array[i] - median);

    return sum;
}

struct TestCase
{
    int length;
    int* array;
};

// C'è un problema con questo metodo, perché non carica i numeri a due cifre :)
vector<TestCase> buildTestCases(string filePath)
{
    ifstream testFile;
    testFile.open(filePath);
    
    string line;
    int internalCounter = 0;

    vector<TestCase> testCases;

    getline(testFile, line); // initial get line to get rid out of useless number of tests number

    while(getline(testFile, line))
    {
        TestCase testCase;

        testCase.length = (int)(line[0] - '0');
        testCase.array = new int(testCase.length);

        int arrayCounter = 0;

        for(int i = 1; i < line.size(); i++)
        {
            if(line[i] != ' ')
                testCase.array[arrayCounter++] = (int)(line[i] - '0');
        }

        testCases.push_back(testCase);
    }

    return testCases;
}

int main()
{
    vector<TestCase> testCases = buildTestCases("testcase_1.txt");

    for(TestCase testCase : testCases)
    {
        cout << "=======================" << endl;

        cout << "\tARRAY: ";
        printVector(testCase.array, testCase.length);

        mergeSort(testCase.array, 0, testCase.length - 1);
        
        int median = findMedian(testCase.array, testCase.length);
        
        cout << "\tFOUND MEDIAN: " << median << endl;
        cout << "\tSUM OF MINIMUM DISTANCES: " << sumOfMinimumDistances(testCase.array, testCase.length, median) << endl;

        cout << "=======================" << endl;
    }

    return 0;
}