#include <iostream>
#include <cstdlib>

#define BINARY_TREE_BUFFER 512

using namespace std;

struct treap_node
{
    int key;
    int priority = 0;
};

class binary_tree
{
    public:
        int size;
        treap_node array[BINARY_TREE_BUFFER];

        binary_tree(int size)
        {
            for(int i = 0; i < BINARY_TREE_BUFFER; i++)
                array[i].key = NULL;

            this->size = size;
        }

        treap_node get(int index)
        {
            return array[index];
        }

        treap_node left(int index)
        {
            return array[2*index + 1];
        }

        treap_node right(int index)
        {
            return array[2*index + 2];
        }

        void rotateRight(int index)
        {
            
        }

        void rotateLeft(int index)
        {
            
        }

        void insertKey(int key)
        {
            int whereToInsert = 0;
            bool found = false;



            treap_node nodeToInsert;
            nodeToInsert.key = key;
            nodeToInsert.priority = rand() % 100;

            if(array[whereToInsert].key == NULL)
            {
                array[whereToInsert] = nodeToInsert;
                found = true;
            }

            while(!found)
            {
                if(key >= array[whereToInsert].key)
                    whereToInsert = 2*whereToInsert + 2;
                else
                    whereToInsert = 2*whereToInsert + 1;

                if(array[whereToInsert].key == NULL)
                {
                    array[whereToInsert] = nodeToInsert;
                    size = max(size, whereToInsert + 1);
                    found = true;
                }
            }
            
        }

        void print()
        {
            cout << "[ ";

            for(int i = 0; i < size; i++)
            {
                cout << "(" << array[i].key << ", " << array[i].priority << ")";

                if(i < size - 1)
                    cout << ", ";
            }

            cout << " ]" << endl;
        }
};

int main()
{
    binary_tree bt = binary_tree(5);
    bt.insertKey(10);
    bt.insertKey(20);
    bt.insertKey(30);
    bt.insertKey(5);
    bt.insertKey(7);
    bt.insertKey(83);
    bt.insertKey(62);
    bt.insertKey(13);
    bt.insertKey(59);
    bt.insertKey(19);

    bt.print();

    return 0;
}