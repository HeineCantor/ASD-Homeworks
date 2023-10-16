#include <iostream>
#include <cstdlib>

using namespace std;

class treapNode
{
    public:
        int key;
        int priority = 0;

        treapNode* left;
        treapNode* right;

        treapNode(int key)
        {
            this->key = key;
            this->priority = rand() % 20;
        }
};

class treap
{
    public:
        int depth = 0;
        int size = 0;

        treap() {};

        treapNode* root() const
        {
            return this->treeRoot;
        }

        void insert(int key)
        {
            treeRoot = insert(treeRoot, key);
        }

        treapNode* insert(treapNode* root, int key)
        {
            if(root == NULL)
                return new treapNode(key);

            if(key >= root->key) // to the right
            {
                root->right = insert(root->right, key);

                if(root->right->priority < root->priority)
                    root = rotateLeft(root);
            }
            else
            {
                root->left = insert(root->left, key);

                if(root->left->priority < root->priority)
                    root = rotateRight(root);
            }

            return root;
        }

        void rotateRight()
        {
            treeRoot = rotateRight(treeRoot);
        }

        treapNode* rotateRight(treapNode* node)
        {
            treapNode* leftSon = node->left;
            treapNode* rightSonOfLeft = node->left->right;

            node->left = rightSonOfLeft;
            leftSon->right = node;

            return leftSon;
        }

        void rotateLeft()
        {
            treeRoot = rotateLeft(treeRoot);
        }

        treapNode* rotateLeft(treapNode* node)
        {
            treapNode* rightSon = node->right;
            treapNode* leftSonfOfRight = node->right->left;

            node->right = leftSonfOfRight;
            rightSon->left = node;

            return rightSon;
        }

        void print()
        {
            recursivePrint(treeRoot, 1, true, 0);
        }

        void recursivePrint(treapNode* root, int level, bool left, int parent)
        {
            cout << "D=" << level << ", L=" << left << ", P=" << parent << ": (" << root->key << ", " << root->priority << ")" << endl;

            if(root->left != NULL)
                recursivePrint(root->left, level+1, true, root->key);
            if(root->right != NULL)
                recursivePrint(root->right, level+1, false, root->key);
        }

        bool validate()
        {
            return validate(treeRoot);
        }

        bool validate(treapNode* root)
        {
            if(root->left == NULL && root->right == NULL)
                return true;

            bool leftIsValid = false;
            bool rightIsValid = false;

            if(
                root->left != NULL &&
                root->left->key <= root->key &&
                root->left->priority >= root->key
            )
                leftIsValid = validate(root->left);

            if(
                root->right != NULL &&
                root->right->key >= root->key &&
                root->right->priority >= root->key
            )
                rightIsValid = validate(root->right);

            return (leftIsValid || root->left == NULL) && (rightIsValid || root->right == NULL);
        }

    private:
        treapNode* treeRoot = NULL;
};

int main()
{
    srand (time(NULL));

    treap testTreap = treap();

    testTreap.insert(10);
    testTreap.insert(20);
    testTreap.insert(30);
    testTreap.insert(5);
    testTreap.insert(7);
    testTreap.insert(83);
    testTreap.insert(62);
    testTreap.insert(13);
    testTreap.insert(59);
    testTreap.insert(19);

    testTreap.print();

    return 0;
}