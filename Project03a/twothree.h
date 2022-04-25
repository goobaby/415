
#ifndef TWOTHREE_H
#define TWOTHREE_H

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "TwoThreeNode.h"

using namespace std;

class TwoThree{
    public: 
        TwoThree();
        void contains() const;
        bool isEmpty();
        void printTree(ostream & out = cout) const;
        void buildTree(ifstream & input);
    private:
	TwoThreeNode * root = nullptr;
	void insertHelper(const string &X, int line, TwoThreeNode *& t, int &distWords);
	bool containsHelper(const string & x, TwoThreeNode * t, TwoThreeNode* &result) const;
	void printTreeHelper(TwoThreeNode *t, ostream & out) const;
	int findHeight(TwoThreeNode *t);
};
	
#endif	
    
	