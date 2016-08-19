// An implementation of the fork class
#include "fork.h"
using namespace std;

time_t timer;

Fork::Fork(int indexid){
  id = indexid;
  inuse = false;
}

Fork::Fork(const Fork &f){
  id = f.id;
  inuse = f.inuse;
}

bool Fork::forkinuse(){
  return inuse;
}

void Fork::takeToUse(const int i){
  mtx.lock();
  time(&timer);
  printf("Phil: %d ==> Taking fork: %d into use at:%s",i, id, ctime(&timer));
  inuse = true;
  time(&timer);
  printf("Phil: %d <=== Taking fork: %d into use at:%s",i,id, ctime(&timer));
}

void Fork::putDownFork(const int i){
  time(&timer);
  printf("Phil: %d ==> Putting down fork %d at %s",i, id, ctime(&timer));
  inuse = false;
  printf("Phil: %d <=== Putting down fork %d at %s",i, id, ctime(&timer));
  mtx.unlock();
}

int Fork::getForkId(){
  return id;
}
