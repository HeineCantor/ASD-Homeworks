#include <iostream>

using namespace std;

// Non va bene così! Non va trovato il punto medio, bensì il punto che minimizza la somma delle distanze (il punto mediano).
// Per fare questo va fatto un sorting (MergeSort magari).

int getMinimumDistancePoint(int* array, int start, int end)
{
    if(start == end)
        return array[start];

    if(start < end)
    {
        int middle = (start + end) / 2;

        int firstPoint = getMinimumDistancePoint(array, start, middle);
        int secondPoint = getMinimumDistancePoint(array, middle+1, end);
        return (firstPoint + secondPoint) / 2;
    }
}

int main()
{
    int test[4] = {6, 4, 2, 0};

    int minimumDistance = getMinimumDistancePoint(test, 0, 3);

    cout << "FOUND MINIMUM DISTANCE POINT: " << minimumDistance << endl;

    return 0;
}