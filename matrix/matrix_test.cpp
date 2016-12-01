#include "matrix.h"
#include <iostream>
#include <assert.h>
using namespace std;

// Test Functions
void test_binary_operators(){
  // This tests matrix addition implementation and also tests the
  // functionality of the overloaded assignment operator.
  cout << ">> Test binary operators : + - *" << endl;
  Matrix<double> matrix1(10, 10, 10.0), matrix2(10, 10, 20.0), result(10, 10, 0.0);

  // Addition
  cout << ">> Addition ";
  result = matrix1 + matrix2;
  result.print_matrix();

  // Subtraction
  cout << ">> Subtraction ";
  result = result - matrix1;
  result.print_matrix();

  // Multiplication
  cout << ">> Multiplication ";
  result = matrix1 * matrix2;
  result.print_matrix();
   
  cout << endl;
}

void assignment_operators(){
  cout << ">> Testing assignment operators: +=, -=, *= " << endl;
  Matrix<double> matrix1(10, 10, 10.0), matrix2(10, 10, 20.0), result(10, 10, 0.0);
  result += matrix1;
  result.print_matrix();

  result -= matrix1;
  result.print_matrix();

  matrix1 *= matrix2;
  matrix1.print_matrix();

  cout << endl;
}

void test_transpose(){
  // Implements a matrix transpose test
  cout <<">> Transpose test";
  Matrix<double> matrix(4, 5, 0.0);
  for(int i=0; i<4; i++){
    for(int j=0; j<5; j++){
      matrix(i, j) = i+1*j+1;
    }
  }
  matrix.print_matrix();
  Matrix<double> result = matrix.transpose();
  result.print_matrix();
  cout << endl;
}

void scalar_operations(){
 Matrix<double> matrix1(10, 10, 10);
 int i = 3;

 // Scalar Addition
 Matrix<double> result = matrix1 + i;
 result.print_matrix();

 // Scalar subtraction
 result = matrix1 - i;
 result.print_matrix();

 // Scalar multiplication
 result = matrix1 * i;
 result.print_matrix();

 // Scalar division
 result = matrix1 / 2.0;
 result.print_matrix();

 cout << endl;
}

int main(int argc, char **argv){

  // Binary operators
  test_binary_operators();

  // Assignment operators
  assignment_operators();

  // Scalar operations
  scalar_operations();

  // Transponse
  test_transpose();

  // TODO: Implement other tests
  
return 0;
}
