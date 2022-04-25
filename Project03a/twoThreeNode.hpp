#include<iostream>
#include<string>
#include<vector>


class twoThreeNode {
    public:
        twoThreeNode(std::string name)
        {
            _name = name;
            _listContainer = new std::vector<twoThreeNode *>;
        }
    private:
        std::string _name;
        std::vector<twoThreeNode *> *_listContainer;
}