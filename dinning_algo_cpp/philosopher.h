/* This is a description for the philosopher class */
#ifndef _philosopher
#define _philosopher

#include "fork.h"
#include <time.h>
#include <string>
#include <chrono>
#include <thread>
#include <stdio.h>
using namespace std;


class Philosopher{
 private:
  int id;
  Fork leftfork, rightfork;	/* Note that this is a composition
				   relationship and therefore the
				   Philosopher constructor should be
				   designed correctly */

 public:
  Philosopher(const int philId, const Fork &lfork, const Fork &rfork);
  void eating();
  void thinking();
  void pickingUpForks();
  void puttingDownForks();
  void dinning();
/*   void startDinningThread(); */
};
#endif
