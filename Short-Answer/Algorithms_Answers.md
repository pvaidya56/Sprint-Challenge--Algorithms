#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - grows at the same rate everytime


b) O(logn) - the outer loop has a runtime of O(n) but the 	inner loop multiplies j by 2 each time so it cuts the time 	in half for which j can be less than n.


c) O(n) - the bunnies decrease until they hit 0, the 	number of bunnies depends on how many times the recursion 	will happen.

## Exercise II

1. Drop the egg from the middle floor, so if there are 100 floors, start from the 50th.
2. If it breaks, find the next midpoint and drop the egg from there
3. If the egg doesn't break, do the same thing but go above
4. Keep repeating until the number of floors can't be divided anymore. if the egg breaks when # of floors cannot be divided anymore then the floor is directly under. If it doesn't break then the answer is the floor you are on. 
5. Runtime complexity is O(logn)

