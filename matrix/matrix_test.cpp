#include "matrix.h"
#include <iostream>
#include <assert.h>
using namespace std;

// To test the matrix implementation, a set of bundled test functions
// are implemented.

void test_binary_operators(){
  // This tests matrix addition implementation and also tests the
  // functionality of the overloaded assignment operator.
  cout << ">> Test binary operators : + - *" << endl;
  Matrix<double> matrix1(10, 10, 10.0), matrix2(10, 10, 20.0), result(10, 10, 0.0);

  cout << ">> Addition ";
  result = matrix1 + matrix2;		  // Addition
  result.print_matrix();

  cout << ">> Subtraction ";
  result = result - matrix1;		  // Subtraction
  result.print_matrix();

  cout << ">> Multiplication ";
  result = matrix1 * matrix2;		  // Multiplication
  result.print_matrix();
   
  cout << endl;
}

void test_assignment_operators(){
  cout << ">> Testing assignment operators: +=, -=, *= " << endl;
  Matrix<double> matrix1(10, 10, 10.0), matrix2(10, 10, 20.0), result(10, 10, 0.0);

  result += matrix1;			// Addition-assignment
  result.print_matrix();

  result -= matrix1;			// Subtraction-assignment
  result.print_matrix();

  matrix1 *= matrix2;			// multiplication-assignment
  matrix1.print_matrix();

  cout << endl;
}

// Testing scalar operations
void test_scalar_operations(){
 Matrix<double> matrix1(10, 10, 10);
 double i = 3;

 Matrix<double> result = matrix1 + i;	 // Scalar Addition
 result.print_matrix();

 result = matrix1 - i;			// Scalar subtraction
 result.print_matrix();
 
 result = matrix1 * i;			// Scalar multiplication
 result.print_matrix();
 
 result = matrix1 / 2.0;		// Scalar division
 result.print_matrix();
 
 cout << endl;
}

// Testing matrix and vector multiplication
void test_vector_operations(){
  cout << ">> Vector operations test " << endl;
  vector<double> aVector(10, 2.0);
  Matrix<double> matrix(5, 10, 2.0);
  
  vector<double> res = matrix * aVector;	// Vector multiplication
  for(int i=0; i< res.size(); i++){
    cout << res.at(i) << ' ';
  }
  cout << endl;
}

// Testing a matrix transpose
void test_transpose_diagonal(){
  cout <<">> Transpose test";
  Matrix<double> matrix(4, 5, 0.0);

  for(int i=0; i<4; i++){
    for(int j=0; j<5; j++){
      matrix(i, j) = i+1*j+1;
    }
  }

  matrix.print_matrix();
  Matrix<double> result = matrix.transpose();	// Matrix transposition
  result.print_matrix();

  cout << "diagonal of transposed matrix" << endl;
  vector<double> res_diag =matrix.diag_vec();
  for(int i=0; i<res_diag.size(); i++){
    cout << res_diag.at(i) << ' ' ;
  }
  cout << endl;
}

int main(int argc, char **argv){

  // Binary operators
  test_binary_operators();
  
  // Assignment operators
  test_assignment_operators();

  // Scalar operations
  test_scalar_operations();

  // Vector operations
  test_vector_operations();

  // Transponse
  test_transpose_diagonal();

return 0;
}
