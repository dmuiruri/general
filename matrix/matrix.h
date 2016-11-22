/* This is a description of the matrix class API */
#ifndef _MATRIX_H
#define _MATRIX_H

#include <vector>
using namespace std;

template <typename T> 
class Matrix{
  /* The internal implementation of the matrix in this design is
     considered as a vector of vectors, making the structure assume a
     two dimensional logical structure. The matrix can also be
     implemented as a linear structure i.e as one vector. In the
     linear structure we just need to know the number of rows(R) and
     columns(C) to step through to the relevant element address where
     the adrress of an element is computed as follows: 

     address=1 + k * (R + 1) where k = 0, 1...(q-1) and q=min(C, R)

  */
 private:
  vector<vector<T> > _matrix;	/* A vector of vectors */
  unsigned rows;		/* unsigned to ensure +ve values */
  unsigned cols;
  
 public:
  Matrix(unsigned _rows, unsigned _cols, const T& initVal);
  Matrix(const Matrix<T>& otherMatrix);
  virtual ~Matrix();

  Matrix<T>& operator=(const Matrix<T>& otherMatrix);		/* assignment */

  /* Matrix mathematical operations */
  Matrix<T> operator+(const Matrix<T>& otherMatrix);		/* Addition */
  Matrix<T> operator-(const Matrix<T>& otherMatrix);		/* Subtraction */
  Matrix<T> operator*(const Matrix<T>& otherMatrix);		/* Multiplication */
  Matrix<T>& operator+=(const Matrix<T>& otherMatrix);		/* Addition and assignment */
  Matrix<T>& operator-=(const Matrix<T>& otherMatrix);		/* Substraction and assignment */
  Matrix<T>& operator*=(const Matrix<T>& otherMatrix);		/* Multiplicationa and assignment */ 
  Matrix<T> transpose();					/* Transpose */

  /* Basic scalar operations */
  Matrix<T> operator+(const T& scalar);
  Matrix<T> operator-(const T& scalar);
  Matrix<T> operator*(const T& scalar);
  Matrix<T> operator/(const T& scalar);

  /* Vector operations */
  vector<T> operator*(const vector<T>& otherVector);		/* Multiply two vectors */
  vector<T> diag_vec();

  /* Acccess the individual elements */
  T& operator()(const unsigned& row, const unsigned& col);
  const T& operator()(const unsigned& row, const unsigned& col)const;

  /* Access row and column sizes */
  unsigned get_rows()const;
  unsigned get_cols()const;
};
#include "matrix.cpp"		/* since its a template class, we must include */

#endif				/* end the _MATRIX_H definition */
