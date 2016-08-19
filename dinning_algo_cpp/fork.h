/* A class description for a fork */
#ifndef _fork
#define _fork

#include <mutex>
#include <time.h>
#include <stdio.h>
using namespace std;

class Fork{
 private:
  mutex mtx;
  int id;
  bool inuse;

 public:
  Fork(int indexid=0);
  Fork(const Fork &f);		/* copy constructor: required by philosopher constructor*/
  bool forkinuse();
  void takeToUse(const int i);		/* pass id of philosopher, for tracing purposes */
  void putDownFork(const int i);
  int getForkId();
};
#endif
