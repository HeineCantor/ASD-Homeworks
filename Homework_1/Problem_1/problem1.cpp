#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <stdexcept>

using namespace std;

#define MAX_TEST_LENGTH 500000
#define MAX_VALUE 999999999

class TestCase
{
    public:
        int length;

        TestCase(int length = 1)
        {
            this->length = length;
        }

        int* getArray()
        {
            return (int*) &(this->values[0]);
        }

        void insertValue(int value)
        {
            values.push_back(value);
        }

    private:
        vector<int> values;
};

vector<TestCase> generateTestCaseFromFile(string testPath)
{
    vector<TestCase> testCases;
    TestCase* tempCase;

    ifstream testFile;
    testFile.open(testPath);

    string line;
    bool readingTest = false;
    int internalCounter = -1;

    while(getline(testFile, line))
    {
        if(internalCounter == 0)
        {
            readingTest = false;
            testCases.push_back(*tempCase);
        }

        if(!readingTest)
        {
            internalCounter = atoi(line.c_str());

            if(internalCounter > MAX_TEST_LENGTH)
                throw out_of_range("Max test length exceeded.");

            tempCase = new TestCase(internalCounter);
            readingTest = true;
        }
        else
        {
            int value = atoi(line.c_str());

            if (value > MAX_VALUE)
                throw out_of_range("Max value exceeded.");

            tempCase->insertValue(value);
            internalCounter--;
        }
    }

    return testCases;
}

void printVector(int* A, int length)
{
    cout << "[";

    for(int i = 0; i < length; i++)
    {
        cout << A[i];

        if(i < length - 1)
            cout << ", ";
    }

    cout << "]";
}

uint mergeInversions(int* A, int p, int q, int r)
{
    int len_L = q - p + 1;
    int len_R = r - q;

    int i, j, k;

    int L[len_L], R[len_R];

    for(i = 0; i < len_L; i++)
        L[i] = A[p + i];
    for(j = 0; j < len_R; j++)
        R[j] = A[q + 1 + j];

    i = j = 0;

    uint inversions = 0;
    bool counted = false;

    for(k = p; k < r; k++)
    {
        if(!counted && R[j] < L[i])
        {
            inversions += len_L - i;
            counted = true;
        }

        if(L[i] <= R[j])
        {
            A[k] = L[i];
            i++;
        }
        else
        {
            A[k] = R[j];
            j++;
            counted = false;
        }
    }

    return inversions;
}

uint inversionCount(int* A, int p, int r)
{
    uint inversions = 0;

    if(p < r)
    {
        int q = (p + r) /2;

        inversions += inversionCount(A, p, q);
        inversions += inversionCount(A, q+1, r);
        inversions += mergeInversions(A, p, q, r);
    }

    return inversions;
}

int main()
{
    vector<TestCase> testCases = generateTestCaseFromFile("personal_testcase.txt");

    for(int i = 0; i < testCases.size(); i++)
    {
        TestCase actualTestCase = testCases[i];

        cout << "VECTOR: ";
        printVector(actualTestCase.getArray(), actualTestCase.length);

        uint inversions = inversionCount(actualTestCase.getArray(), 0, actualTestCase.length - 1);

        cout << "| NUMBER OF INVERSIONS: " << inversions << endl;
    }

    return 0;
}