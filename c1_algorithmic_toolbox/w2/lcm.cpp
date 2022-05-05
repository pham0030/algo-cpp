#include <iostream>

int gcd(long long a, long long b){
    long long temp_prime ;
    if (a>=b){
        if(b==0) return a;
        else{
            temp_prime = a%b;
            return gcd(b, temp_prime);
        }
    }
    else{
        if(a==0) return b;
        else{
            temp_prime = b%a;
            return gcd(a, temp_prime);
        }
    }
}

long long lcm(long long a, long long b){
    return a*b / gcd(a, b);
}

int main() {
    long a, b;
    std::cin >> a >> b;
    std::cout << lcm(a, b);
    return 0;
}