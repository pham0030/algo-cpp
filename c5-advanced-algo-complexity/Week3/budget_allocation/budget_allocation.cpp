#include <ios>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <cassert>

using namespace std;

struct ConvertToSat {
    bitset<3> combinations;
    string clauses;


    vector< vector<int> > A;
    vector<int> b;
    
    //Constructor
    ConvertToSat(int n, int m) : A(n, vector<int>(m)), b(n) { }


    void printSAT()
    {
        int cnt = 0;
        for(int i = 0; i < A.size(); ++i) {
            const auto & row = A[i];
            int n = count_if(row.begin(), row.cend(), [](const auto a) { return a != 0; });

            for(int j = 0, s = pow(2, n); j < s; ++j) {
               combinations = j;
               int sum = 0, comb = 0;
               for(const auto x : row) {
                   if(x != 0 && combinations[comb++]) {
                      sum += x;
                   }
               }

               if (sum > b[i]) {
                   bool end_clause = false;
                   for(int k = 0, comb = 0; k < row.size(); ++k) {
                       if(row[k] != 0) {
                          clauses += combinations[comb] ? (to_string(-(k+1)) + ' ') : (to_string(k+1) + ' ');
                          ++comb;
                          end_clause = true;
                       }
                   }
                   if(end_clause) {
                      clauses += "0 \n";
                      ++cnt;
                   }
               }
            }
        }

        if(cnt == 0) {
            cnt++;
            clauses += "1 -1 0\n";
        }
        cout << cnt << " " << (A[0].size()) << endl;
        cout << clauses.c_str();
    }

};

int main() {
    ios::sync_with_stdio(false);

    int n, m;
    cin >> n >> m;
    ConvertToSat converter(n, m);
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        cin >> converter.A[i][j];
      }
    }
    for (int i = 0; i < n; i++) {
      cin >> converter.b[i];
    }

    converter.printSAT();

    return 0;
}
