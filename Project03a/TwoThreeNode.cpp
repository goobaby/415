#include <iostream>
#include <string>
#include <utility>
#include <vector>

#include "TwoThreeNode.h"

bool TwoThreeNode::isTwoNode() {
    return this->keys.size() == 1;
}

bool TwoThreeNode::isLeaf() {
    for(int i = 0; i < this->children.size(); i++){
        if (this->children[i] != nullptr) {
            return false;
        }
    }
    return true;
}

int TwoThreeNode::addTo(std::string key, std::vector<int> lines) {
    int i = 0;
    while (i < this->keys.size()){
        if (key < this->keys[i]){
            break;
        }
        i++;
    }
    this->keys.push_back(nullptr);
    this->lines.push_back({});
    for(int j = i; j < this->keys.size()-1; j++){
        this->keys[j+1] = this->keys[j];
        this->lines[j+1] = this->lines[j];
    }
    this->keys[i] = key;
    this->lines[i] = lines;

    this->children.push_back(nullptr);
    for(int j = i; j < this->children.size()-1; j++){
        this->children[j+1] = this->children[j];
    }
    this->children[i] = nullptr;
    return i;
}

void TwoThreeNode::promote() {
    std::string promotedKey = this->keys[1];
    int promotedPos = 0;
    if (this->parent != nullptr){
        promotedPos = this->parent->addTo(this->keys[1],this->lines[1]);
    } else{
        TwoThreeNode cplusplusIsBad = TwoThreeNode({this->keys[1]},{this->lines[1]},{nullptr,nullptr},nullptr);
        this->parent = &cplusplusIsBad;
    }
    TwoThreeNode cplusplusIsReallyBad = TwoThreeNode({this->keys[0]},{this->lines[0]},{this->children[0],this->children[1]},this->parent);
    TwoThreeNode cplusplusIsIncrediblyBad = TwoThreeNode({this->keys[2]},{this->lines[2]},{this->children[2],this->children[3]},this->parent);
    this->parent->children[promotedPos] = &cplusplusIsReallyBad;
    this->parent->children[promotedPos+1] = &cplusplusIsIncrediblyBad;
    if (this->parent->keys.size() > 3){
        this->parent->promote();
    }
    delete this;
}

void TwoThreeNode::insert(std::string key) {
    if(this->isLeaf()){
        this->addTo(key,{});
        if (this->keys.size() > 2){
            this->promote();
        }
    } else{
        for(int i = 0; i < this->keys.size(); i++){
            if (key < this->keys[i]){
                this->children[i]->insert(key);
            }
        }
        this->children[this->keys.size()]->insert(key);
    }
}

TwoThreeNode * TwoThreeNode::find(std::string key){
    for(int i = 0; i < this->keys.size(); i++){
            if (key < this->keys[i]){
                return this->children[i]->find(key);
            }
            if (key == this->keys[i]) {
                return this;
            }
        }
        return this->children[this->keys.size()]->find(key);
}

void TwoThreeNode::add(std::string key, int line){
    TwoThreeNode* nodeWithKey = this->find(key);
    if(nodeWithKey == nullptr){
        this->insert(key);
        nodeWithKey = this->find(key);
    }
    for(int i = 0; i < nodeWithKey->keys.size(); i++){
        if (nodeWithKey->keys[i] == key){
            nodeWithKey->lines[i].push_back(line);
            return;
        }
    }
    //ERROR STATE!
}