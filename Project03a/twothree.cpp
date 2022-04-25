//Prototypes for the 2-3 tree class

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#include "TwoThree.h"

using namespace std;

//Prototypes for the 2-3 tree class

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "time.h"
#include <iomanip>
#include <sstream>

#include "TwoThree.h"

using namespace std;

bool TwoThree::isEmpty() {
    return root == nullptr;
}

// void TwoThree::contains() const{
//    string input;
//    node *foundNode = NULL;
//    cout << "Search word: ";
//    cin >> input;
//     	if(containsHelper(input, root, foundNode)){ //CALL NODE FIND()
// 	    cout << "Line Numbers: " << foundNode->lines[0];
// 	    for(int i = 1; i < foundNode->lines.size(); i++)
// 		cout << ", " <<foundNode->lines[i]; 
// 	    cout << '\n';
// 	    }
// 	else
// 	    cout << '\"' << input <<"\" is not in the document\n";
// }

void TwoThree::printTree(ostream & out) const {
	out << "2-3 Tree Index:\n-------------------------\n";
	printTreeHelper(root, out);
}


void TwoThree::buildTree(ifstream & input){
    int line = 1, numWords = 0, distWords = 0, treeHeight = 0;
	stringstream tempWord;
	double totalTime, finishTime, startTime = clock();
	while (!input.eof()) {
		string tempLine, tempWord;

		//Read a whole line of text from the file
		getline(input, tempLine);
		for (int i = 0; i < tempLine.length(); i++) {
		    //Insert valid chars into tempWord until a delimiter( newline or space) is found
		    while (tempLine[i] != ' '&& tempLine[i] != '\n' && i < tempLine.length() ) {
			tempWord.insert(tempWord.end(), tempLine[i]);
			i++;
		    }
		   
            //Trim any punctuation off end of word. Will leave things like apostrophes
            //and decimal points
            while(tempWord.length() > 0 && !isalnum(tempWord[tempWord.length() - 1]))
			    tempWord.resize(tempWord.size() -1);   
			
            if (tempWord.length() > 0)
            {
                //Once word is formatted,call insert with the word, the line of the input
                //file it came from, the root of our tree, and the distinct word counter
                if(root == nullptr){
                    root = &TwoThreeNode({tempWord},{{line}},{nullptr,nullptr},nullptr);
                }else{
                    root->add(tempWord, line);
                }
                //Increment our total number of words inserted
                numWords++;
                //Clear out tempWord so we can use it again
                tempWord.clear();
		    }
			
		}
		line++;
        	//Do time and height calculation
        finishTime = clock();
        totalTime = (double) (finishTime - startTime)/CLOCKS_PER_SEC;
        //treeHeight = findHeight(root);

        //Print output
        cout << setw(40) << std::left;
        cout << "Total number of words: " << numWords<< endl;

        cout << setw(40) << std::left 
        << "Total number of distinct words: " << distWords << endl;

        cout << setw(40) << std::left 
        <<"Total time spent building index: " << totalTime << endl;

        cout << setw(40) << std::left
        <<"Height of 2-3 Tree is : " << treeHeight << endl;
    }
}



//Called by printTree(), does the actual formatted printing
void TwoThree::printTreeHelper(TwoThreeNode *t, ostream & out) const{
    if(t == NULL)
		return;
    if(t->children.size() == 0)
    {
        for(int i = 0; i < t->keys.size(); i++){
            out << setw(30) << std::left;
		    out << t->keys.at(i) << " ";
            out << t->lines.at(0).at(0);

            for(int j = 0; j < t->lines.size(); j++){
                for(int k = 1; k < t->lines.at(j).size(); k++){
                    out << ", " << t->lines.at(j).at(k);
                }
            }
        }
        out << endl;
    }
    else if(t->children.size() == 1){
        printTreeHelper(t->children.at(0), out);
        for(int i = 0; i < t->keys.size(); i++){
            out << setw(30) << std::left;
		    out << t->keys.at(i) << " ";
            out << t->lines.at(0).at(0);

            for(int j = 0; j < t->lines.size(); j++){
                for(int k = 1; k < t->lines.at(j).size(); k++){
                    out << ", " << t->lines.at(j).at(k);
                }
            }
        }
    }
	else if(t->children.size() == 2){
		printTreeHelper(t->children.at(0), out);
        for(int i = 0; i < t->keys.size(); i++){
            out << setw(30) << std::left;
		    out << t->keys.at(i) << " ";
            out << t->lines.at(0).at(0);

            for(int j = 0; j < t->lines.size(); j++){
                for(int k = 1; k < t->lines.at(j).size(); k++){
                    out << ", " << t->lines.at(j).at(k);
                }
            }
        }
        out << endl;
		printTreeHelper(t->children.at(1), out);
	}
    else if(t->children.size() == 3) {
        printTreeHelper(t->children.at(0), out);
        for(int i = 0; i < t->keys.size(); i++){
            out << setw(30) << std::left;
		    out << t->keys.at(i) << " ";
            out << t->lines.at(0).at(0);

            for(int j = 0; j < t->lines.size(); j++){
                for(int k = 1; k < t->lines.at(j).size(); k++){
                    out << ", " << t->lines.at(j).at(k);
                }
            }
        }
        out << endl;
        printTreeHelper(t->children.at(1), out);
        for(int i = 0; i < t->keys.size(); i++){
            out << setw(30) << std::left;
		    out << t->keys.at(i) << " ";
            out << t->lines.at(0).at(0);

            for(int j = 0; j < t->lines.size(); j++){
                for(int k = 1; k < t->lines.at(j).size(); k++){
                    out << ", " << t->lines.at(j).at(k);
                }
            }
        }
        out << endl;
        printTreeHelper(t->children.at(2), out);
    }
}

//Returns height of tree. If tree has only one node, height is 1    
// int TwoThree::findHeight(TwoThreeNode *t){
//     if(t == NULL)
// 	return 0;
//     else{
// 	int leftHeight = findHeight(t->left), rightHeight = findHeight(t->right);
// 	if(leftHeight > rightHeight)
// 	    return(leftHeight+1);
// 	else 
// 	    return(rightHeight+1);
//     }
// }