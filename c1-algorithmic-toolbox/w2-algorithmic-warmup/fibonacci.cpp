#include <iostream>

long long calc_fib_fast(int n) {
    if (n <= 1)
        return n;
    else {
        long long fib_array[n+1];
        fib_array[0] = 0;
        fib_array[1] = 1;
        for(int i=2; i< n+1; i++){
            fib_array[i] = fib_array[i-1] + fib_array[i-2];
        }
        return fib_array[n];
    }

}

int main () {
    int n;
    std::cin >> n;
    long long result = calc_fib_fast(n);
    std::cout << result;
    return 0;
}