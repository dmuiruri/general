/* This is a description of a matrix class. The matrix_vec private
   member is a vector of vectors, i.e it is a set of rows, storing
   columns of Types. */

#ifndef _MATRIX_BASIC_H
#define _MATRIX_BASIC_H

#include <vector>
using namespace std;

template <typename Type=double>
  class Matrix{
 private:
 vector<vector<Type> >matrix_vec;	/* A vector of vectors */
 
 public:
 Matrix();							/* Default constructor */
 Matrix(const int &rows, const int &cols, const Type &initVal);	/* Constructor with parameters */
 Matrix(const Matrix<Type> &_rhsMatrix);			/* Copy constructor */
 
 Matrix<Type>& operator=(const Matrix<Type> &_rhsMatrix);	/* overloading assignment operator */
 virtual ~Matrix();						/* Destructor */
 vector<vector<Type> > getMatrix() const;			/* return full matrix, vect of vects */
 Type& value(const int &row, const int &col);			/* return a select value */
};
#endif
