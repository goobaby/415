//Description: Takes a text file supplied by the user
//             and turns it into a word index, implemented
//             through the use of a BST 

#include <iostream>
#include <fstream>
#include "bst.h"
#include "TwoThree.h"

using namespace std;

int main(int argc, char* argv[]) {
	int choice;
	std::string upperchoice;
	if (argc != 2) {
	    cout << "Incorrect input. Correct format: ./<exectuable.out> <inputtext.txt>\n";
	    return 1;
	}

	ifstream input(argv[1]);
	BST myTree;
	TwoThree tree2;


	if(input.is_open()){

		upperchoice = "0";
		//myTree.buildTree(input);
		//tree2.buildTree(input);
		//input.close();

		cout << "Options: (a) BST, (b) 2-3 Tree, (c) Compare BST and 2-3 Tree\n";
		
		cin >> upperchoice;

		if (upperchoice == "b" or upperchoice == "B"){
			cout<< "buh";
			tree2.buildTree(input);

			input.close();
			while(1){
			choice = 0;
			cout <<"Options: (1) display index, (2) search, (3) save index, (4) quit\n";
			cin >> choice;

			//Print index
				if(choice == 1)
					tree2.printTree(cout);
			
			//Search index for a word
			else if(choice == 2){
					//tree2.contains();
			}

			//Save index
				else if(choice == 3){
				string outputFile;
					cout << "Enter a filename to save your index to (Suggested: <filename>.txt) : ";
				cin >> outputFile;
				ofstream output(outputFile.c_str());
					tree2.printTree(output);
					output.close();
				cout << "Saved\n";
				}

			//Quit	
				else
				break;
				}
		}
		else if(upperchoice == "a" or upperchoice == "A") {
			myTree.buildTree(input);
			input.close();

			while(1){
			choice = 0;
			cout <<"Options: (1) display index, (2) search, (3) save index, (4) quit\n";
			cin >> choice;

			//Print index
				if(choice == 1)
					myTree.printTree(cout);
			
			//Search index for a word
			else if(choice == 2)
					myTree.contains();

			//Save index
				else if(choice == 3){
				string outputFile;
					cout << "Enter a filename to save your index to (Suggested: <filename>.txt) : ";
				cin >> outputFile;
				ofstream output(outputFile.c_str());
					myTree.printTree(output);
					output.close();
				cout << "Saved\n";
				}

			//Quit	
				else
				break;
				}
	}
	else{
	    cout << "Invalid File Name. Restart Program.\n";
	    return 2;
        }
	return 0;
}
}
