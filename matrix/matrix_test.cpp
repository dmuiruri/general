#include "matrix.h"
#include <iostream>
#include <assert.h>
using namespace std;


int main(int argc, char **argv){

  Matrix<double> matrix1(10, 10, 10.0);
  Matrix<double> matrix2(10, 10, 20.0);

  cout << ">> Testing matrix implementation " << endl;

  // Test for addition and overloaded assignment
  Matrix<double> result = matrix1 + matrix2;
  result.print_matrix();

  // Test for subtraction and overloaded assignment
  result = matrix2 - matrix1;
  result.print_matrix();
  
  // Test for Multiplication
  result = matrix1 * matrix2;
  result.print_matrix();

  // Combined Addition and assignment operator (+=)
  result += (matrix1);
  result.print_matrix();

  // TODO: Implement other tests
  
return 0;
}


