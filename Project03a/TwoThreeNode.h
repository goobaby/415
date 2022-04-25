#ifndef TWOTHREENODE_H
#define TWOTHREENODE_H

#include<iostream>
#include<string>
#include<vector>

class TwoThreeNode {
    public:
        TwoThreeNode(std::vector<std::string> keys, std::vector<std::vector<int>> lines, std::vector<TwoThreeNode *> children, TwoThreeNode * parent) : keys(keys), lines(lines), children(children), parent(parent) {};
        std::vector<std::string> keys;
        std::vector<std::vector<int>> lines;
        std::vector<TwoThreeNode *> children;
        TwoThreeNode * parent;

        bool isTwoNode();
        void insert(std::string key);
        TwoThreeNode * find(std::string key);
        void add(std::string key, int line);
        bool isLeaf();
    private:
        void promote();
        int addTo(std::string key, std::vector<int> lines);
        //void traverse(std::string key);
        
};
#endif