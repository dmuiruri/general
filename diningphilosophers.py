#!/usr/bin/env python

"""
This file contains an implementation of a non-blocking solution to the
dining philosophers problem -a concurrent algorithm design
illustrating synchronization.

The dining philosopher's problem: Five philosophers sit at a round
table with bowls of spaghetti. Forks are placed between each pair of
adjacent philosophers. Each philosopher must alternately think and
eat. However, a philosopher can only eat when he has both left and
right forks. Each fork can held by only one philosopher
exclusively. Once finished eating, the fork must be made available to
others. A Philosopher can take forks are they become available BUT can
only start eating when both forks are available.

Round table logic

        -------------------------
Forks   | 0 | 1 | 2 | 3 | 4 | 0 |
        -------------------------
Philospher  1   2   3   4   5
    
Each Philosopher has a fork to the left and to the right

TODO: Make the algorithm more generic such that we can create an
arbitrary number of Philosophers.
"""

__author__ = 'Dennis Muiruri'
__copyright__ = 'Copyright (c) 02/2015 Dennis Muiruri'

import os, time
import _thread as thread        # _thread allows us to kill threads
                                # through killing the main process
    
class Philosopher:
    def __init__(self, name, leftfork, rightfork):
        print('Creating instance', name)
        self.myname     = name
        self.leftFork   = leftfork
        self.rightFork  = rightfork

    def eating(self):
        """
        Only eat when you have forks available
        """
        print(self.myname,':==> Eating', time.asctime())
        time.sleep(3)
        print(self.myname,':<== Eating', time.asctime())

    def thinking(self):
        """
        When not eating, engage in some thinking.
        """
        print(self.myname, 'Thinking...', time.asctime())
        time.sleep(2)

    def pickUpForks(self):      # Would be best if function is atomic
        print(self.myname, 'Picking up forks',time.asctime())
        print(self.myname, ': leftforkinuse:%s, rightforkinuse:%s' %
              (self.leftFork.inuse, self.rightFork.inuse))
        if self.leftFork.mymutex.acquire() and self.rightFork.mymutex.acquire():
            print(self.myname,':Forks mutex acquired')
            self.leftFork.takeToUse(self.myname)
            self.rightFork.takeToUse(self.myname)

    def putDownForks(self):     # consider making function atomic? no need
        print(self.myname, 'Putting Down forks', time.asctime())
        self.rightFork.putDownFork(self.myname)
        self.leftFork.putDownFork(self.myname)
        self.leftFork.mymutex.release()
        self.rightFork.mymutex.release()
 
    def dinning(self):
        """
        We simulate picking up forks, eating then thinking
        """
        print(self.myname,': => Dining...', time.asctime())
        while True:
            self.pickUpForks()
            self.eating()
            self.putDownForks()
            self.thinking()

class Fork:
    def __init__(self, forkname):
        print('Creating fork:', forkname)
        self.myforkname = forkname
        self.mymutex    = thread.allocate_lock()
        self.inuse      = False
        self.mypid      = os.getpid()

    def takeToUse(self, name):
        print(name,':',self.myforkname,': Taking fork into use', time.asctime())
        self.inuse = True

    def putDownFork(self, name):
        print(name, ':', self.myforkname,': Putting down the fork', time.asctime())
        self.inuse = False

# Test code: We need to have 5 Philisophers and they need to be
# assigned forks that they could use
        
if __name__ == '__main__':
    # Create Forks
    Fork0 = Fork('Fork0') 
    Fork1 = Fork('Fork1')
    Fork2 = Fork('Fork2')
    Fork3 = Fork('Fork3')
    Fork4 = Fork('Fork4')
    
    # Create Philosophers and assign forks
    Phil1 = Philosopher('Phil1', Fork0, Fork1)
    Phil2 = Philosopher('Phil2', Fork1, Fork2)
    Phil3 = Philosopher('Phil3', Fork2, Fork3)
    Phil4 = Philosopher('Phil4', Fork3, Fork4)
    Phil5 = Philosopher('Phil5', Fork4, Fork0)

    # Start to eat
    thread.start_new_thread(Phil1.dinning, ())
    thread.start_new_thread(Phil2.dinning, ())
    thread.start_new_thread(Phil3.dinning, ())
    thread.start_new_thread(Phil4.dinning, ())
    thread.start_new_thread(Phil5.dinning, ())

    time.sleep(25)       # Give spawned threads a chance to run
    

