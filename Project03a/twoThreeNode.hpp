#include<iostream>
#include<string>
#include<vector>

#ifndef TWOTHREENODE_H
#define TWOTHREENODE_H

class TwoThreeNode {
    public:
        TwoThreeNode(vector<string> keys, vector<node *> children) :keys(keys), children(children) {};
        vector<string> keys;
        vector<node *> children;
        node * parent;
        bool isTwoNode();
        void insert(string key);
        void find(string key);
        //void traverse(string key);
        bool isLeaf();
}

#endif