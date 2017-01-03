// Testing Eigen matrix "library". The libary contains much more
// advanced inbuilt algorithms for matrix computation than is tested
// here. The Eigen file is added during compile time by using the 'I'
// flag and passing the folder containing the included path in the
// code <Eigen/Dense>. In this test environment the command used was
// g++ -I ./eigen-eigen-f562a193118d/ matrix_eigen.cpp -o matrix_eigen.o

#include <iostream>
#include <Eigen/Dense>
using namespace std;
// using namespace Eigen;

int main(){
  Eigen::MatrixXd a(3,3);	// Dimensions of matrix unknown at compile time of double(type): Matrix[X]d
  a << 1,2,3,4,5,6,7,8, 9;	// note overloaded << operator as assignment operator for Eigen
  cout << a << endl;
  
  // Matrix and Vector Arithmetic
  Eigen::Matrix3d b;		// Define two matrices, predefined 3x3 double(type) matrix: Matrix3d
  Eigen::Matrix3d c;
  b << 1,2,3,4,5,6,7,8,9;	// Fill out the matrices
  c << 10,11,12,13,14,15,16,17,18;
  cout << "=> matrix b \n" << b << endl;
  cout << "=> matrix c \n" << c << endl;

  Eigen::Vector3d d(1,2,3);	// Define two vectors
  Eigen::Vector3d e(4,5,6);
  cout << "=> vector d \n" << d << endl;
  cout << "=> vector e \n" << e << endl;


  cout << endl <<  "b + c \n" << b + c << endl;
  cout << endl <<  "d - e \n" << d - e << endl;

  // Scalar multiplication and division
  cout << endl << "b * 20 \n" << b * 20 << endl;
  cout << endl << "c / 10 \n" << c / 10 << endl;

  //  Matrix tranposition
  Eigen::Matrix3d t = Eigen::Matrix3d::Random(3,3);	// Populate the matrix with random values
  cout << "=> matrix t (random) \n" << t << endl;
  cout << "=> transpose of t (t^T) \n" << t.transpose() << endl;
  t.transposeInPlace();					// streaming the output directly causes spurious results?
  cout << "=> transpose (t^T) in place \n" << t << endl;

  // Matrix/Matix and Matrix/Vector Multiplication
  Eigen::Matrix3d j;
  j << 1, 2, 3,
       4, 5, 6,
       7 ,8 ,9;
  Eigen::Vector3d k(10, 11, 12);	// default notation is 3x1
  Eigen::Vector3d l(13, 14, 15);

  cout << "matrix-by-matrix multiplication \n" << j * j << endl;
  cout << "matrix-by-vector multiplication [m * v] \n" << j * k << endl;
  cout << "vector-by-matrix multiplication [v * m] \n" << k.transpose() * j << endl;
  cout << "vector-to-vector multiplication [v * v] \n" << l.transpose() * k << endl;	// Order of operands seems to matter?


  // Vector operations 'DOT' and 'CROSS' products
  cout << "The dot product [v . v] \n" << k.dot(l) << endl;	// ||a|| ||b|| cos(Ø)
  cout << "The cross product [v x v] \n" << k.cross(l) << endl;	// ||a|| ||b|| sin(Ø)

  // Matrix reduction operations: sum, prod, mean, minCoeff, maxCoeff,
  // trace (sum of diagonal elements)
  Eigen::MatrixXd m = Eigen::MatrixXd::Random(4,4) * 10;
  cout << "Randomly populated 4x4 matrix\n" << m << endl;
  cout << "Reduction operation sum(): " << m.sum() << endl;
  cout << "Reduction operation prod(): " << m.prod() << endl;
  cout << "Reduction operation mean(): " << m.mean() << endl;
  cout << "Reduction operation minCoeff():" << m.minCoeff() << endl;
  cout << "Reduction operation maxCoeff():" << m.maxCoeff() << endl;
  cout << "Reduction operation trace():" << m.trace() << endl;
  cout << "Partial reduction mat.rowwise()" << m.rowwise().sum() << endl;
  cout << "Partial reduction mat.colwise()" << m.colwise().sum() << endl;
  
}
