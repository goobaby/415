//Description: Takes a text file supplied by the user
//             and turns it into a word index, implemented
//             through the use of a BST 

#include <iostream>
#include <fstream>
#include "time.h"
#include <iomanip>
#include <sstream>
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
					tree2.contains(cout);
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
	else if(upperchoice == "c" or upperchoice == "C") {

		myTree.buildTree(input);
		//
		
		//process index for BST
			int line = 1, numWords = 0, distWords = 0, treeHeight = 0;
			stringstream tempWord;
			double BSTtotalTime, BSTfinishTime, BSTstartTime = clock();
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
						///Search For every word
						myTree.find(tempWord);
						//Increment our total number of words inserted
						numWords++;
						//Clear out tempWord so we can use it again
						tempWord.clear();
					}
					
				}
				line++;
			}
			BSTfinishTime = clock();
			BSTtotalTime = (double) (BSTfinishTime - BSTtotalTime)/CLOCKS_PER_SEC;
			//Calculations

			cout << "Total time taken by BST: " << BSTtotalTime << endl;
			input.close();




			//2-3 Time



			ifstream inputTwo(argv[1]);
			if(inputTwo.is_open())
			{
				tree2.buildTree(inputTwo);
				
				int line = 1, numWords = 0, distWords = 0, treeHeight = 0;
				stringstream tempWord;
				double twoThreetotalTime, twoThreefinishTime, twoThreestartTime = clock();
				while (!inputTwo.eof()) {
					string tempLine, tempWord;

					//Read a whole line of text from the file
					getline(inputTwo, tempLine);
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
							///Search For every word
							tree2.find(tempWord);
							//Increment our total number of words inserted
							numWords++;
							//Clear out tempWord so we can use it again
							tempWord.clear();
						}
						
					}
					line++;
				}
				twoThreefinishTime = clock();
				twoThreetotalTime = (double) (twoThreefinishTime - twoThreetotalTime)/CLOCKS_PER_SEC;
				//Calculations

				cout << "Total time taken by 2-3 Tree: " << twoThreetotalTime << endl;
				inputTwo.close();
			}



		}
	else{
	    cout << "Invalid File Name. Restart Program.\n";
	    return 2;
        }
	return 0;
}
}
