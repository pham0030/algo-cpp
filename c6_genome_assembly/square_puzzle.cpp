#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
const bool DEBUG=false;

struct Square{
    string up;
    string left;
    string down;
    string right;
    int id;
};

bool operator < (const Square &lhs, const Square &rhs) {return lhs.id < rhs.id;}

class SquarePuzzle{
    Square left_up, left_down, right_up, right_down;
    vector<Square> up, left, down, right, middle;
    const string black="black";

    public:
    void insert(Square square){
        if(square.up == black && square.left == black)
            left_up = move(square);
        else if(square.left == black && square.down == black)
            left_down = move(square);
        else if(square.down == black && square.right == black)
            right_down = move(square);
        else if(square.right == black && square.up == black)
            right_up = move(square);
        else if(square.up == black)
            up.emplace_back(move(square));
        else if(square.left == black)
            left.emplace_back(move(square));
        else if(square.down == black)
            down.emplace_back(move(square));
        else if(square.right == black)
            right.emplace_back(move(square));
        else middle.emplace_back(move(square));
    }

    bool check(){
        for(int i = 0; i < up.size(); ++i)
            if(up[i].down != middle[i].up) return false;
        for(int i = 0; i < left.size(); ++i)
            if(left[i].right != middle[i * left.size()].left) return false;
        for(int i = 1; i <= down.size(); ++i)
            if(down[down.size()-i].up != middle[middle.size()-i].down) return false;
        for(int i = 0; i < right.size(); ++i)
            if(right[i].left != middle[i * right.size() + (right.size()-1)].right) return false;
        return true;
    }
    void solve()
    {   if(up.size()>1){
        while(left_up.right != up[0].left or up[0].right != up[1].left or up.back().right != right_up.left)
            next_permutation(up.begin(), up.end());

        while(left_down.right != down[0].left or down[0].right != down[1].left or down.back().right != right_down.left)
            next_permutation(down.begin(), down.end());

        while(left_up.down != left[0].up or left[0].down != left[1].up or left.back().down != left_down.up)
            next_permutation(left.begin(), left.end());

        while(right_up.down != right[0].up or right[0].down != right[1].up or right.back().down != right_down.up)
            next_permutation(right.begin(), right.end());

        while(not check())
            next_permutation(middle.begin(), middle.end());
        }
    }

    void print_top(){
        cout << '(' << left_up.up << ',' << left_up.left << ',' << left_up.down << ',' << left_up.right << ");";
        for(auto & square : up)
            cout << '(' << square.up << ',' << square.left << ',' << square.down << ',' << square.right << ");";
        cout << '(' << right_up.up << ',' << right_up.left << ',' << right_up.down << ',' << right_up.right << ")" << endl;
    }

    void print_middle(){
        for(int i = 0, j = 0; i < left.size(); ++i){
            cout << '(' << left[i].up << ',' << left[i].left << ',' << left[i].down << ',' << left[i].right << ");";
            for(int k = 0; k < up.size(); ++k, ++j)
                cout << '(' << middle[j].up << ',' << middle[j].left << ',' << middle[j].down << ',' << middle[j].right << ");";
            cout << "(" << right[i].up << ',' << right[i].left << ',' << right[i].down << ',' << right[i].right << ")" << endl;
        }
    }

    void print_bottom(){
        cout << '(' << left_down.up << ',' << left_down.left << ',' << left_down.down << ',' << left_down.right << ");";
        for(auto & square : down)
            cout << '(' << square.up << ',' << square.left << ',' << square.down << ',' << square.right << ");";
        cout << '(' << right_down.up << ',' << right_down.left << ',' << right_down.down << ',' << right_down.right << ")" << endl;
    }

    void print(){
        print_top();
        print_middle();
        print_bottom();
    }

};

int main () {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    int id = 0;
    SquarePuzzle puzzle;
    string up, left, down, right, tmp;

    if(!DEBUG){
        while (getline(cin, up, ',')){
            up = up.substr(1);
            getline(cin, left, ',');
            getline(cin, down, ',');
            getline(cin, right, ')');
            right = right.substr(0, right.size());
            getline(cin, tmp, '\n');
            puzzle.insert(Square{move(up), move(left), move(down), move(right), id++});
        }
    }
    else{
        up="yellow";left="black";down="black";right="blue";
        puzzle.insert(Square{move(up), move(left), move(down), move(right), id++});

        up="blue";left="blue";down="black";right="yellow";
        puzzle.insert(Square{move(up), move(left), move(down), move(right), id++});

        up="orange";left="yellow";down="black";right="black";
        puzzle.insert(Square{move(up), move(left), move(down), move(right), id++});

        up="red";left="black";down="yellow";right="green";
        puzzle.insert(Square{move(up), move(left), move(down), move(right), id++});

        up="orange";left="green";down="blue";right="blue";
        puzzle.insert(Square{move(up), move(left), move(down), move(right), id++});

        up="green";left="blue";down="orange";right="black";
        puzzle.insert(Square{move(up), move(left), move(down), move(right), id++});

        up="black";left="black";down="red";right="red";
        puzzle.insert(Square{move(up), move(left), move(down), move(right), id++});

        up="black";left="red";down="orange";right="purple";
        puzzle.insert(Square{move(up), move(left), move(down), move(right), id++});

        up="black";left="purple";down="green";right="black";
        puzzle.insert(Square{move(up), move(left), move(down), move(right), id++});
    }



    puzzle.solve();
    puzzle.print();

    return 0;
}
