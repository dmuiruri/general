// Implementation of the Matrix class making use of vector and making
// the matrix object more abstract by designing it as a template
// class.
#include "matrix_basic.h"

template<class Type>
Matrix<Type>::Matrix(){		// default constructor
}

template<class Type>
Matrix<Type>::Matrix(const int &rows, const int &cols, const Type &initVal){
  for(int i=0; i<rows; i++){
    vector<Type> columnVector (cols, initVal);
    matrix_vec.push_back(columnVector);
  }
}

template<class Type>
Matrix<Type>::Matrix(const Matrix<Type> &_rhsMatrix){	// copy constructor
  matrix_vec = _rhsMatrix.getMatrix();
}

template<class Type>
Matrix<Type>& Matrix<Type>::operator=(const Matrix<Type> &_rhsMatrix){
  if(this == &_rhsMatrix)
    return *this;
  matrix_vec = _rhsMatrix.getMatrix();
  return *this;
}

template<class Type>
Matrix<Type>::~Matrix(){ // No dynamic mem to release
}

template<class Type>
vector<vector<Type> >Matrix<Type>::getMatrix() const{
  return matrix_vec;
}

template<class Type>
Type& Matrix<Type>::value(const int &row, const int &col){
  matrix_vec[row][col];
}
