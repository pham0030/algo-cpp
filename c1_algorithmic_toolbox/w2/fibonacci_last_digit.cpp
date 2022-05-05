#include <iostream>

int get_fibonacci_last_digit_less_mem(int n){
    if (n <=1) return n;
    else{
        long long previous = 0;
        long long current = 1;
        long long temp = 0;
        for(int i; i < n-1; ++i){
            temp = previous;
            previous = current;
            current = (temp+current) % 10;
        }
        return current;
    }
}

int main() {
    int n;
    std::cin >> n;
    int result;
    result = get_fibonacci_last_digit_less_mem(n);
    std::cout << result;
    return 0;
}