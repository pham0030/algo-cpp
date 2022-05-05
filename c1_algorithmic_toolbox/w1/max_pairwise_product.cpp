#include <iostream>

long long MaxPairwiseProduct(int * numbers, int n){
  int max_index1 = -1;
  for (int i=0; i<n; ++i){
    if((max_index1==-1) || (numbers[i] > numbers[max_index1]))
      max_index1 = i;
  }

  int max_index2 = -1;
  for (int j=0; j<n; ++j){
    if((j!=max_index1) && ((max_index2==-1) || (numbers[j] > numbers[max_index2])))
      max_index2 = j;
  }
  return ((long long) (numbers[max_index1])) * numbers[max_index2];
}

int main(){
  int n;
  std::cin>>n;
  int numbers[n];
  for (int i=0; i<n; i++){
    std::cin >> numbers[i];
  }
  long long result = MaxPairwiseProduct(numbers, n);
  std::cout << result << std::endl;
  return 0;
}
