
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
	node * root = nullptr;
	void insertHelper(const string &X, int line, node *& t, int &distWords);
	bool containsHelper(const string & x, node * t, node* &result) const;
	void printTreeHelper(node *t, ostream & out) const;
	int findHeight(node *t);
};
	
#endif	
    
	