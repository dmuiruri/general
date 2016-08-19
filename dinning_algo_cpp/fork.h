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
  Fork(const Fork &f);		/* copy constructor: for somereason its needed by dinning_app */
  bool forkinuse();
  void takeToUse(const int i);
  void putDownFork(const int i);
  int getForkId();
};
#endif
