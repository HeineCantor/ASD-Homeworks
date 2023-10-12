#include <iostream>

using namespace std;

int getStoppingNode(int depth, int launches, int nodeNumber)
{
    // if it's a leaf node, return the node
    if(depth == 1)
        return nodeNumber;

    int stoppingNode;

    if(launches % 2 == 1) // odd number of launches, go left
        stoppingNode = getStoppingNode(depth - 1, launches / 2 + 1, 2*nodeNumber);
    else
        stoppingNode = getStoppingNode(depth - 1, launches / 2, 2*nodeNumber + 1);

    return stoppingNode;
}

int main()
{
    int depth = 10;
    int launches = 1;

    int stoppingNode = getStoppingNode(depth, launches, 1);

    cout << "STOPPING NODE COMPUTED: " << stoppingNode << endl;

    return 0;
}