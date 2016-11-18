#ifndef _MATRIX_CPP
#define _MATRIX_CPP

#include "matrix.h"

// Implementation of the matix template class
template<typename T>
Matrix<T>::Matrix(unsigned _rows, unsigned _cols, const T& initVal){
  _matrix.resize(_rows);
  for(unsigned i=0; i<_matrix.size(); i++){
    _matrix[i].resize(_cols, initVal);	// mat[i] is a vector itself
  }
  rows = _rows;
  cols = _cols;
}

template<typename T>
Matrix<T>::Matrix(const Matrix<T>& otherMatrix){
  _matrix = otherMatrix;
  rows = otherMatrix.get_rows();	
  cols = otherMatrix.get_cols();
}

template<typename T>
Matrix<T>::~Matrix(){
  // No dynamic memory to delete
}

template <typename T>
Matrix<T> Matrix<T>::operator+(const Matrix<T>& otherMatrix){
  Matrix<T> _mat(rows, cols, 0.0);	// new matrix
  for(unsigned i=0; i<cols; i++){
    for(unsigned j=0; j<rows; j++){
      _mat(j,i) = this->_matrix[j][i] + otherMatrix(j,i);
    }
  }
  return _mat;
}

template<typename T>
Matrix<T> Matrix<T>::operator-(const Matrix<T>& otherMatrix){
  Matrix<T> _mat(rows, cols, 0.0);
  for(int i=0; i<rows; i++){
    for(int j=0; j<cols; j++){
      _mat(i,j) = _matrix[i][j] - otherMatrix(i, j);
    }
  }
  return _mat;
}

template<typename T>
Matrix<T> Matrix<T>::operator*(const Matrix<T>& otherMatrix){
  int rows = otherMatrix.get_rows();
  int cols = otherMatrix.get_cols();
  Matrix<T> _mat(rows, cols, 0.0);

  for(int i=0; i<rows; i++){
    for(int j=0; j<cols; j++){
      for(int k=0; k<rows; k++){
	_mat(i, j) += _matrix[i][j] * otherMatrix(k, j);
      }
    }
  }
  return _mat;
}

template<typename T>
Matrix<T>& Matrix<T>::operator=(const Matrix<T>& otherMatrix){
  if (this == &otherMatrix)		// Don't copy this matrix to itself
    return *this;

  int new_rows = otherMatrix.get_rows();
  int new_cols = otherMatrix.get_cols();

  _matrix.resize(new_rows);		// resize the matrix
  for(int i=0; i<_matrix.size(); i++){
    _matrix[i].resize(new_cols);
  }
  
  for(int i=0; i<new_rows; i++){	// Copy the contents of other matrix
    for(int j=0; j<new_cols; j++){
      _matrix[i][j] = otherMatrix(i, j);
    }
  }
  rows = new_rows;
  cols = new_cols;
  
  return *this;
}

template<typename T>
Matrix<T>& Matrix<T>::operator+=(const Matrix<T>& otherMatrix){

  int rows = otherMatrix.get_rows();
  int cols = otherMatrix.get_cols();

  for(int i=0; i<rows; i++){
    for(int j=0; j<cols; j++){
      this->_matrix[i][j] = _matrix[i][j] + otherMatrix(i, j);
    }
  }
  return *this;
}

template<typename T>
Matrix<T>& Matrix<T>::operator-=(const Matrix<T>& otherMatrix){
  int rows = otherMatrix.get_rows();
  int cols = otherMatrix.get_cols();

  for(int i=0; i<rows; i++){
    for(int j=0; j<cols; j++){
      this->_matrix[i][j] = _matrix[i][j]-otherMatrix(i, j);
    }
  }
  return *this;
}

template<typename T>
Matrix<T>& Matrix<T>::operator*=(const Matrix<T>& otherMatrix){
  Matrix<T> result = (*this) * otherMatrix;	// Since we have implemented * operator
  (*this) = result;
  return *this;
}

template<typename T>
Matrix<T> Matrix<T>::transpose(){
  int rows = _matrix.get_rows();
  int cols = _matrix.get_cols();
  Matrix<T> temp(cols, rows, 0.0);

  for(int i=0; i<rows; i++){
    for(int j=0; j<cols; j++){
      temp[j][i] =this-> _matrix[i][j];
    }
  }
  return temp;
}

// Scalar operations
template<typename T>
Matrix<T> Matrix<T>::operator+(const T& scalar){
  Matrix<T> result(rows, cols, 0.0);
  
  for(int i=0; i<rows; i++){
    for(int j=0; j<cols; j++){
      result[i][j] = scalar + this-> _matrix(i, j);
    }
  }
  return result;
}

template<typename T>
Matrix<T> Matrix<T>::operator-(const T& scalar){
  Matrix<T> result(rows, cols, 0.0);

  for(int i=0; i<rows; i++){
    for(int j=0; j<cols; j++){
      result[i][j] = this->_matrix[i][j] + scalar;
    }
  }
  return result;
}

template<typename T>
Matrix<T> Matrix<T>::operator*(const T& scalar){
  Matrix<T> result(rows, cols, 0.0);
  for(int i=0; i<rows; i++){
    for(int j=0; j<cols; j++){
      result[i][j] = this->_matrix[i][j] + scalar;
    }
  }
  return result;
}

template<typename T>
Matrix<T> Matrix<T>::operator/(const T& scalar){
  Matrix<T> result(rows, cols, 0.0);
  for(int i=0; i<rows; i++){
    for(int j=0; j<cols; j++){
      result[i][j] = this->_matrix[i][j] / scalar;
    }
  }
  return result;
}

// Matrix and vector operations
template<typename T>
vector<T> Matrix<T>::operator*(const vector<T>& aVector){
  vector<T> result(aVector.size(), 0.0);
  for(int i=0; i<rows; i++){
    for(int j=0; j<cols; j++){
      result[i] += this->_matrix[i][j] * aVector[j];
    }
  }
  return result;
}

template<typename T>
vector<T> Matrix<T>::diag_vec(){
  /* No need to iterate through all elements just move row to row
     picking only they diagonal element this speeds up the computation
     especially in light of large matrices. */
  vector<T> resVector;
  for(int i=0; i<rows; i++){
	resVector[i] = _matrix[i][i];	
  }
  return resVector;
}

// Access the individual elements
template<typename T>
T& Matrix<T>::operator()(const unsigned& row, const unsigned& col){
  return this->_matrix[row][col];
}

template<typename T>
const T& Matrix<T>::operator()(const unsigned& row, const unsigned& col) const{
  return this->_matrix[row][col];
}
 
// Access row and cols sizes of the matrix 
template<typename T>
unsigned Matrix<T>::get_rows() const{
  return this->rows;
}

template<typename T>
unsigned Matrix<T>::get_cols() const{
  return this->cols;
}

#endif
