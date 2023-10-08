#include <iostream>
#include <string>

using namespace std;

string commonPrefix(string s1, string s2)
{
    string prefix = "";

    int minLength = min(s1.size(), s2.size());

    int i = 0;

    while(i < minLength && s1[i] == s2[i])
    {
        i++;
        prefix = s1.substr(0, i);
    }

    return prefix;
}

string findPrefix(string* array, int start, int end)
{
    if(start == end)  // only one string
        return array[start];

    if(end > start)
    {
        int middle = (start + end) / 2;

        string s1 = findPrefix(array, start, middle);
        string s2 = findPrefix(array, middle + 1, end);
        return commonPrefix(s1, s2);
    }

    return "";
}

int main()
{
    string test[4] = {"apple", "ape", "april", "applied"};

    cout << "COMMON PREFIX FOUND: " << findPrefix(test, 0, 3) << endl;

    return 0;
}