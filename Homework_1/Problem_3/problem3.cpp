#include <iostream>

#define BINARY_TREE_BUFFER 512

using namespace std;


class binary_tree
{
    public:
        int size;
        int array[BINARY_TREE_BUFFER];

        binary_tree(int size)
        {
            for(int i = 0; i < BINARY_TREE_BUFFER; i++)
                array[i] = NULL;

            this->size = size;
        }

        int get(int index)
        {
            return array[index];
        }

        int left(int index)
        {
            return array[2*index + 1];
        }

        int right(int index)
        {
            return array[2*index + 2];
        }

        void insert(int value)
        {
            int whereToInsert = 0;
            bool found = false;

            if(array[whereToInsert] == NULL)
            {
                array[whereToInsert] = value;
                found = true;
            }

            while(!found)
            {
                if(value >= array[whereToInsert])
                    whereToInsert = 2*whereToInsert + 2;
                else
                    whereToInsert = 2*whereToInsert + 1;

                if(array[whereToInsert] == NULL)
                {
                    array[whereToInsert] = value;
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
                cout << array[i];

                if(i < size - 1)
                    cout << ", ";
            }

            cout << " ]" << endl;
        }
};

int main()
{
    binary_tree bt = binary_tree(5);
    bt.insert(10);
    bt.insert(20);
    bt.insert(30);
    bt.insert(5);
    bt.insert(7);

    bt.print();

    return 0;
}