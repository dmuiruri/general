// Application similating the dining philosopher algorithm
#include "philosopher.h"
#include "fork.h"
#include <thread>
#include <vector>
using namespace std;


int main(void){

  int numOfPhilosophers = 5, leftfork, rightfork;

  // create vector containers
  vector<thread> threadsVector;
  vector<Philosopher> PhilosophersVector;
  vector<Fork> ForksVector;
  threadsVector.reserve(numOfPhilosophers);	   // ensure mem is not deallocated on runtime
  PhilosophersVector.reserve(numOfPhilosophers);  // plus it gives some performance benefits
  ForksVector.reserve(numOfPhilosophers); // Using individual loops below(as opposed to
					  // processging everything in one loop) also considers
					  // that incase mem is deallocated at runtime,
					  // the sequential processing of the vectors ensures we
					  // get the final created vector.

  // create shared Fork objects
  for(int i=0; i<=numOfPhilosophers; i++){
    ForksVector.push_back(Fork(i));
  }

  // create Philosopher objects
  for(int i=1; i<=numOfPhilosophers; i++){
    leftfork = i-1; 
    if (i == numOfPhilosophers)
      rightfork = 0;
    else
      rightfork = i;
    PhilosophersVector.push_back(Philosopher(i, ForksVector[leftfork], ForksVector[rightfork]));
  }

  for(int i=0; i<numOfPhilosophers; i++)
    threadsVector.push_back(thread(&Philosopher::dinning, PhilosophersVector[i]));
  
  for(auto& thread : threadsVector) thread.join();
}
