#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <random>

using namespace std;

// Function to get rid of non alphabet charaters
string cleanStr(string str){
    for(int i=0; i<str.length(); i++){
        if(!isalpha(str[i])){
            str.erase(i, 1);
            i--;
        }
    }
    return str;
}

int main () {
    // Configuration for reads
    const int OVERLAP_MIN = 15;
    const int OVERLAP_MAX = 75;
    const int READ_LENGTH = 100;
    const int NUMBER_READS = 1000;
    random_device rd;
    mt19937 rng(rd());
    uniform_int_distribution<int> uni(OVERLAP_MIN , OVERLAP_MAX);

    string phiX174_genome;
    string phiX174_genomes;

    // Read and clean phiX174 data
    ifstream inFile("phiX174_notclean.txt");
    if (inFile.is_open()){
        stringstream strStream;
        strStream << inFile.rdbuf();
        phiX174_genome= cleanStr(strStream.str());
        inFile.close();
    }
    else cout << "Unable to open file";
    // Write the cleaned phiX174 genome to file
    ofstream phiX174_cleaned_outfile("phiX174_cleaned.txt");
    if (phiX174_cleaned_outfile.is_open()){
        phiX174_cleaned_outfile << phiX174_genome << endl;
        phiX174_cleaned_outfile.close();
    }
    else cout << "Unable to write file to phiX174_cleaned.txt";

    // Duplicate the genome and breaking it to pieces (read)
    for (int i=0; i<30; i++){
        phiX174_genomes += phiX174_genome;
    }
    ofstream outFile("phiX174_reads.txt");
    if (outFile.is_open()){
        for (int i=0; i<NUMBER_READS; i++){
            int overlap_size = uni(rng);
            outFile << phiX174_genomes.substr(READ_LENGTH*(i+1) - overlap_size, READ_LENGTH) << endl;
        }
        outFile.close();
    }
    else cout << "Unable to write file to phiX174_reads.txt";

    return 0;
}