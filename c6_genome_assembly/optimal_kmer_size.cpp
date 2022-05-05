#include <map>
#include <set>
#include <vector>
#include <iostream>

using namespace std;

const int INITIAL_MERSIZE=100;

map<string, set<string>> build_graph(const vector<string> &reads, const int k){
    map<string, set<string>> graph;
    for(const auto &read: reads){
        for(size_t i=0; i+k < read.size(); ++i){
            graph[read.substr(i, k-1)].emplace(read.substr(i+2, k-1));
            if(i+k+1<read.size()) {
                graph[read.substr(i+2, k-1)];
            }
        }
    }
    return graph;
}


enum struct Result{
    NoCycle,
    OneCycle,
    MultipleCycles
};

Result check_cycle(const map<string, set<string>> graph) {
    // Loop through all vertices to find if the is dead loops or multiple loops or one loops only
    for (auto &vertex : graph){
        if (vertex.second.empty()) return Result::NoCycle;
        if (vertex.second.size() > 1) return Result::MultipleCycles;
    }
    return Result::OneCycle;
}

int search_optimal_kmer_size(const vector<string> reads, int left, int right){
    while (right >=left){
        int mid = left + (right - 1)/2;  //Binary search for optimal kmer values

        Result result = check_cycle(build_graph(reads, mid));
        switch (result) {
            case Result::OneCycle:
                return mid;
            case Result::NoCycle:
                right = mid - 1;
            case Result::MultipleCycles:
                left = mid + 1;
                continue;
        }
    }

    return 0;
}

int main() {
    vector<string> reads;
    string input_string;

    while(cin >> input_string) {
        reads.emplace_back(move(input_string));
    }

    cout << search_optimal_kmer_size(reads, 0, INITIAL_MERSIZE) << endl;
    return 0;
}