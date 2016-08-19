// Implementation of the philosopher class
#include "philosopher.h"

time_t tracetimer;	// for tracing purposes

Philosopher::Philosopher(const int philId, const Fork &lfork, const Fork &rfork):leftfork(lfork), rightfork(rfork){
  // note Fork constructors listed above
  id = philId;
}

void Philosopher::eating(){
  time(&tracetimer);
  printf("Phil: %d :==> Eating at %s", id, ctime(&tracetimer));
  this_thread::sleep_for(chrono::seconds(3));	// seems to block main thread too ?
  time(&tracetimer);
  printf("Phil: %d :<=== Eating at %s", id, ctime(&tracetimer));
}

void Philosopher::thinking(){
  printf("Phil: %d Thinking\n", id);	// printf is thread safe unlike cout
  this_thread::sleep_for(chrono::seconds(2));
}

void Philosopher::pickingUpForks(){
  // Only get to eat if both forks are available
  printf("Phil: %d Picking up forks\n", id);
  printf("Phil: %d leftfork: %d rightfork %d\n",
	 id, leftfork.getForkId(), rightfork.getForkId());
  leftfork.takeToUse(id);	// should block thread until lock is available
  rightfork.takeToUse(id);	// leftfork must be first available ??
}

void Philosopher::puttingDownForks(){
  printf("Phil: %d Putting down forks(leftfork: %d rightfork: %d)\n", 
	 id, leftfork.getForkId(), rightfork.getForkId());
  rightfork.putDownFork(id);
  leftfork.putDownFork(id);
}

void Philosopher::dinning(){
  printf("Phil: %d Dinning\n", id);
  while(1){
    pickingUpForks();	// calls blocking functions
    eating();
    puttingDownForks();
    thinking();
  }
  // We exit when parent thread is killed
}
