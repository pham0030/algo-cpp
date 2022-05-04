#include <iostream>

int get_pisano_preiod(long long m){
    long long a = 0, b = 1;
    if (m<2) return 1;
    
    for(int i=0; i<m*m; i++){
        long long c = (a+b) % m;
        a = b;
        b = c;
        if (a == 0 && b == 1){
            return i + 1;
        }
    }
    return 0;
}

long long get_fibonacci_huge_fast(long long n, long long m){
    if (n<=1) return n;
    long long remainder = n % get_pisano_preiod(m);
    long long a = 0;
    long long b = 1;
    long long res = remainder;
    for(int i=0; i<remainder-1; i++){
        res = (a+b) %m;
        a = b;
        b = res;
    }
    return res;
}

int fibonacci_sum_squares(long long n) {
    int Fn = get_fibonacci_huge_fast(n, 10);
    int Fn1 = get_fibonacci_huge_fast(n+1, 10);

    return Fn*Fn1%10;
}

int main() {
    long long n = 0;
    std::cin >> n;
    std::cout << fibonacci_sum_squares(n);
}
