//Prototypes for the 2-3 tree class

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#include "twoThreeNode.hpp"

using namespace std;

class twoThree{
    public:
        twoThree(): _root(nullptr) {};
        void insert(twoThreeNode *nNode);
        twoThreeNode *find(std:: string name);
        void print() {print(return _root);};
        twoThreeNode *getRoot() {return _root; };
    private:
        void print(twoThreeNode *_root);
        twoThreeNode *_root;


}