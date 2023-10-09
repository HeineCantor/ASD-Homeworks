#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <stdexcept>

using namespace std;

#define MAX_TEST_LENGTH 500000
#define MAX_VALUE 999999999

#pragma region TEST_CASES
class TestCase
{
    public:
        int length;

        TestCase(int length = 1)
        {
            this->length = length;
        }

        int* getArray() const
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
#pragma endregion

#pragma region UTILS
void printVector(int* array, int length)
{
    cout << "[";

    for(int i = 0; i < length; i++)
    {
        cout << array[i];

        if(i < length - 1)
            cout << ", ";
    }

    cout << "]";
}
#pragma endregion

uint mergeInversions(int* array, int start, int middle, int end)
{
    int len_L = middle - start + 1;
    int len_R = end - middle;

    int i, j, k;

    int L[len_L], R[len_R];

    for(i = 0; i < len_L; i++)
        L[i] = array[start + i];
    for(j = 0; j < len_R; j++)
        R[j] = array[middle + 1 + j];

    i = j = 0;

    uint inversions = 0;
    bool counted = false;

    for(k = start; k <= end; k++)
    {
        if(!counted && R[j] < L[i])
        {
            inversions += len_L - i;
            counted = true;
        }

        if(i < len_L && j < len_R)
        {
            if(L[i] <= R[j])
            {
                array[k] = L[i];
                i++;
            }
            else
            {
                array[k] = R[j];
                j++;
                counted = false;
            }
        }
        else
        {
            if(i < len_L)
            {
                array[k] = L[i];
                i++;
            }
            else
            {
                array[k] = R[j];
                j++;
            }
        }
    }

    return inversions;
}

uint inversionCount(int* array, int start, int end)
{
    uint inversions = 0;

    if(start < end)
    {
        int middle = (start + end) /2;

        inversions += inversionCount(array, start, middle);
        inversions += inversionCount(array, middle+1, end);
        inversions += mergeInversions(array, start, middle, end);
    }

    return inversions;
}

int main(int argc, char* argv[])
{
    if(argc <= 1)
    {
        cout << "No input test case detected. Usage: './problem1 [TEST_CASE_NAME.txt]'" << endl;
        return 1;
    }
    
    vector<TestCase> testCases = generateTestCaseFromFile(argv[1]);

    for(int i = 0; i < testCases.size(); i++)
    {
        TestCase actualTestCase = testCases[i];

        cout << "VECTOR: ";
        printVector(actualTestCase.getArray(), actualTestCase.length);

        uint inversions = inversionCount(actualTestCase.getArray(), 0, actualTestCase.length - 1);

        printVector(actualTestCase.getArray(), actualTestCase.length);

        cout << "| NUMBER OF INVERSIONS: " << inversions << endl;
    }

    return 0;
}