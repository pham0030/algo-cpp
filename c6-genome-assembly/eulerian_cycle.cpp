#include <iostream>
#include <vector>
#include <cassert>
#include <stack>
#include <algorithm>

using namespace std;

// If number of in_path_records is not equal to number of out_path_records at any vertex, the eulerian is
// in_path_records valid
bool check_eulerian_validity(const vector<int> &in_path_records, const vector<int> &out_path_records){
    assert(in_path_records.size()==out_path_records.size());
    for(size_t i=0; i<in_path_records.size(); ++i){
        if(in_path_records[i] != out_path_records[i])
            return false;
    }
    return true;
}

vector<int> find_eulerian_graph(vector<vector<int>> graph){
    stack<int> vertices;
    vector<int> path;
    // Start at 0 vertex
    vertices.push(0);  //Caching vertices
    int current_vertex=0;
    while(!vertices.empty()){
        current_vertex = vertices.top(); // Start at 0 vertex or the next inline vertex
        if(!graph[current_vertex].empty()){  //Get all the paths from the current vertex if it is not empty
            vertices.push(graph[current_vertex].back());  //By pushing the vertex to the caching vertices
            graph[current_vertex].pop_back();  //Remove vertex after add to the caching vertices
            continue;
        }
        path.push_back(current_vertex);
        vertices.pop();  //remove an element from the top of the stack
    }
    reverse(path.begin(), path.end());
    path.pop_back();
    return path;
}

int main(){

    int number_vertices, number_edges;
    cin >> number_vertices >> number_edges;
    
    vector<vector<int>> graph(number_vertices);
    vector<int> in_path_records(number_vertices), out_path_records(number_vertices);

    for (int i = 0; i < number_edges; ++i)
    {
        int from, to;
        cin >> from >> to;
        graph[--from].push_back(--to);
        ++in_path_records[to];
        ++out_path_records[from];
    }

    if (!check_eulerian_validity(in_path_records, out_path_records)){
        cout << 0 << endl;
    } else{
        vector<int> eulerian_cycle = find_eulerian_graph(move(graph));
        cout << 1 << endl;
        for(int v: eulerian_cycle){
            cout << v + 1 << ' ';
        }
        cout << endl;
    }
    return 0;
}