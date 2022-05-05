#include <iostream>
#include <cstring>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;
const int EST_GENOME_READ_LENGTH = 1000;
const int READS_SIZE = 1618;
const bool DEBUG=false;

// Function to find the overlap value of string b to string a
int find_overlap(const string& a, const string& b, const int& least_overlap_length){
  int n = a.size();
  // Compare string b to the tail of string a, 
  // Loop from full string a to tail of a with at least overlap least_overlap_length
  for(int i=0; i<1+n-least_overlap_length; i++){
    if(strncmp(b.c_str(), a.c_str()+i, n-i)==0)
        return n-i; // If equal return the value of overlap
  }
  return 0;
}

string build_genome(vector<string> reads, const int least_overlap_length){
  // Initialize genome strings and record first read
  string genome;
  genome.reserve(EST_GENOME_READ_LENGTH);
  genome += reads.front();
  string first_read = reads.front();
  string current_read= "";
  
  int i = 0;
  while (reads.size() > 1) {
    //Import the specific read from the previous round to current read also clear
    // it from the reads as it was recorded to genome in the last rounds
    current_read = move(reads[i]);
    reads.erase(reads.begin() + i);
    
    int max_overlap = -1;
    // Naively loop through all the remaining reads and find the read with maximum overlap
    // with the current read, record this maximum overlap 
    // read location record to the genome and use it as current read next round
    int m = reads.size();
    for (int j=0; j<m; ++j){
      int overlap = find_overlap(current_read, reads[j], least_overlap_length);
      if (overlap > max_overlap){
        max_overlap = overlap;
        i=j;
      }
    }
    // Import this read to the current genome, only the substring to load
    genome += reads[i].substr(max_overlap);
  }

  // Delete redundancy as the genome is circular
  genome.erase(0, find_overlap(reads[0], first_read, least_overlap_length));
  return genome;
}

int main(){
  // ios_base::sync_with_stdio(0);
  // cin.tie(0);
  // cout.tie(0);
  string s;
  vector<string> reads;
  reads.reserve(READS_SIZE);
  if(!DEBUG){
    while (cin >> s) {
        if (reads.back() != s) {
            reads.emplace_back(move(s));
        }
    }
  } else{
    string line;
    ifstream myfile ("phiX174_reads.txt");
    if (myfile.is_open()){
      while ( getline (myfile,line)){
        if (reads.back() != line) 
          reads.emplace_back(move(line));
      }
      myfile.close();
    }
    else cout << "Unable to open file"; 
  }

  cout << build_genome(move(reads), 12) << endl;
  return 0;
}
