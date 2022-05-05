#include <iostream>
#include <cstring>
#include <vector>
#include <fstream>
#include <sstream>
#include <map>
#include <random>
#include <algorithm>

using namespace std;

const int MAX_ERRORS = 2;
const int EST_GENOME_READ_LENGTH = 1000;
const int READS_SIZE = 1618;
const bool DEBUG=false;

// Function to find the overlap value of string b to string a
int find_overlap(const string& a, const string& b, const int& least_overlap_length){
  int n = a.size();

  // Compare string b to the tail of string a, 
  // Loop from full string a to tail of a with at least overlap least_overlap_length
  for(int i=0; i<1+n-least_overlap_length; ++i){
    int errors = 0;
    for (int j=0;j < n-i && errors<=MAX_ERRORS;++j){
        if (a[i+j] != b[j]){
            errors++;
        }
    }
    if (errors <= MAX_ERRORS){
        return n-i;
    }
  }
  return 0;
}

//get correct char as the most frequent chars 
char get_correct_char(const vector<char> inputs) {
    map<char, int> counts;

    for (auto c: inputs) {
        counts[c]++;
    }
    pair<char, int> most_frequent = *counts.begin();

    for (auto each: counts) {
        if (each.second > most_frequent.second) {
            most_frequent = each;
        }
    }

    return most_frequent.first;
}

string build_genome(vector<string> reads, const int least_overlap_length){
  // Initialize genome strings and record first read
  string genome;
  genome.reserve(EST_GENOME_READ_LENGTH);
  genome += reads.front();
  string first_read = reads.front();
  string current_read= "";

  int i = 0;
  while (reads.size() > 1){
      current_read = move(reads[i]);
      reads.erase(reads.begin() + i);
      int max_overlap = - 1;

      // Tracking all the overlaps length and position of the 
      // corresponding remaining reads for the current read iteration
      vector<int> overlaps; 
      vector<int> positions;
      
      // Naively loop through all the remaining reads and find the read with maximum overlap
      // with the current read, record this maximum overlap 
      // read location record to the genome and use it as current read next round
      int current_reads_size = reads.size();
      for(int j=0; j<current_reads_size; ++j){
          int overlap = find_overlap(current_read, reads[j], least_overlap_length);

          if (overlaps.empty() || overlap>=overlaps.back()){
              // Note that the overlaps is in ascending ordered
              // with the number of overlap
              overlaps.push_back(overlap);
              positions.push_back(j);
              i = j;
          }
      }

      //Cleaning the errors, since the overlaps is ASCENDING then
      /*
      For error free case:
      tail of current genome:                      ....ATCTATGAAGTT
      from bottom, 1st read                                 TGAAGTT....
      2nd read, overlaps[loc-2]                                 AAGTT....  
      3th read, overlaps[loc-3],reads[positions[p-3]]            AGTT....
      4th read, overlaps[loc-4],reads[positions[p-4]]            AGTT....
      ........................................................>[]......
                                                   ....ATCTATGAAGTT
      *suffix------------------------------------------------->A                                                             
                                                               AGTT....
      *prefix1------------------------------------------------>A
                                                               AGTT....
      *prefix2------------------------------------------------>A
                                                              AAGTT....
      *prefix3------------------------------------------------>A
                                                            TGAAGTT....
      *prefix4------------------------------------------------>A

      For ERROR case:
      tail of current genome:                      ....ATCTATGAAGTT
      from bottom, 1st read                                 TGAGGTT....
      2nd read, overlaps[loc-2]                                 AAGTT....  
      3th read, overlaps[loc-3],reads[positions[p-3]]            AGTT....
      4th read, overlaps[loc-4],reads[positions[p-4]]            AGTT....
      ........................................................>[]......
                                                   ....ATCTATGAAGTT
      *suffix------------------------------------------------->A                                                             
                                                               AGTT....
      *prefix1------------------------------------------------>A
                                                               AGTT....
      *prefix2------------------------------------------------>A
                                                              AAGTT....
      *prefix3------------------------------------------------>A
                                                            TGAGGTT....
      *prefix4------------------------------------------------>G
      Here G is ERROR, since A is more common among prefix and suffix  

        //Pointer to the tail(current latest) overlapping portion of current genome 
       //Start with the first of last four reads in the overlaps vector    
       //First char from prefix1 from reads
       //Equivalent second char from prefix2 from reads, this should
       //be the same with the first char if error is free
      //Going down the lists
      */
      int loc = overlaps.size();
        if (overlaps.size() > 3) {
            char *suffix = &genome[genome.size() - overlaps[loc - 4]];
            char *prefix1 = &reads[positions[loc - 4]][0];
            char *prefix2 = &reads[positions[loc - 3]][
                    (overlaps[loc - 3] - overlaps[loc - 4])];
            char *prefix3 = &reads[positions[loc - 2]][
                    (overlaps[loc - 2] - overlaps[loc - 4])];
            char *prefix4 = &reads[positions[loc - 1]][
                    (overlaps[loc - 1] - overlaps[loc - 4])];

            for (int i = 0, n = overlaps[loc - 4]; i < n; ++i,
                    ++suffix, ++prefix1, ++prefix2, ++prefix3, ++prefix4) {
                if (*suffix == *prefix1 && *prefix1 == *prefix2 &&
                    *prefix2 == *prefix3 && *prefix3 == *prefix4) {
                    continue;
                }

                const char c = get_correct_char({*suffix, *prefix1, *prefix2, *prefix3, *prefix4});
                *suffix = *prefix1 = *prefix2 = *prefix3 = *prefix4 = c;
            }
        }
      // Import this read to the current genome, only the substring to load
      genome += reads[i].substr(overlaps.back());

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

  random_device rd;
  mt19937 g(rd());
  shuffle(reads.begin(), reads.end(), g); //Submit few times to shuffle the results
  cout << build_genome(move(reads), 12) << endl;
  return 0;
}
