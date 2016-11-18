/* This is a description of the matrix class API */
#ifndef _MATRIX_H
#define _MATRIX_H

#include <vector>
using namespace std;

template <typename T> 
class Matrix{
 private:
  vector<vector<T> > _matrix;	/* A vector of vectors */
  unsigned rows;		/* unsigned to ensure +ve values */
  unsigned cols;
  
 public:
  Matrix(unsigned _rows, unsigned _cols, const T& initVal);
  Matrix(const Matrix<T>& otherMatrix);
  virtual ~Matrix();

  /* Matrix mathematical operations */
  Matrix<T> operator+(const Matrix<T>& otherMatrix);		/* Addition */
  Matrix<T> operator-(const Matrix<T>& otherMatrix);		/* Subtraction */
  Matrix<T> operator*(const Matrix<T>& otherMatrix);		/* Multiplication */
  Matrix<T>& operator=(const Matrix<T>& otherMatrix);		/* assignment */
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
