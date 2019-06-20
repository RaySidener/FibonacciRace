#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

//#include "Fibo1.cpp"
using namespace std;

//modifies arr so that it contains the
//first n numbers of the Fibonacci sequence
void Fibo1(int n, int* arr){
  arr[0] = 0;
  arr[1] = 1;
  for(int i = 2; i < n; i++){
    arr[i]=arr[i-1]+arr[i-2];
  }
}

//modifies arr so that it contains the first
//n numbers of the Fibonacci sequence, calculated
//using the explicit formula
//I want to parallelize this but I just realized
//that my GPU doesn't support CUDA :(
void Fibo2(int n, int* arr){
  const float rtfive = 2.2360679775;
  arr[0] = 0;
  arr[1] = 1;
  for(int i = 2; i< n; i++){
    arr[i] = int(
      (pow((1+rtfive)/2, i)
    -(pow((1-rtfive)/2,i)))
    /rtfive);
  }
}

//prints the given array
void printArray(int size, int* arr){
  cout<<"Array: ";
  for(int i = 0; i <size; i++){
    cout<< arr[i]<<", ";
  }
}

int main(){
  const int numbrOfElements = 10;
  int a[numbrOfElements];
  int b[numbrOfElements];
  Fibo1(numbrOfElements, a);
  Fibo2(numbrOfElements, b);
  printArray(numbrOfElements, a);
  printArray(numbrOfElements, b);
  return 0;
}
