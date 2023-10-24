#include <iostream>
#include <string>
#include <fstream>

using namespace std;



string Prefix(string s1, string s2)
{
    string prefix = "";

    int minl = min(s1.size(), s2.size());

    int i = 0;

    while (i < minl && s1[i] == s2[i])
    {
        i++;
        prefix = s1.substr(0, i);
    }

    return prefix;
}



string findPrefix(string* array, int p, int r)
{
    if (p == r)  // only one string
        return array[p];

    if (r > p)
    {
        int middle = (p + r) / 2;

        string s1 = findPrefix(array, p, middle);
        string s2 = findPrefix(array, middle + 1, r);
        return Prefix(s1, s2);
    }

    return "";
}



int main()
{

    int n = 0;

    ifstream file("test.txt");
    
    if (!file.is_open()) cout << "Unable to open file";

    while (file.is_open())
    {

        file >> n;
        cout << n << "\n";

        if (n == 0) exit(1);

        string* test_case = new string[n];

        for (int i = 0; i < n; i++) {
            file >> test_case[i];
            cout << test_case[i] << "\n";
        }

        cout << "Prefisso comune: " << findPrefix(test_case, 0, n - 1) << endl;

        delete[] test_case;
    }

    file.close();

    return 0;
}