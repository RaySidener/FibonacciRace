Ray Sidener, 9.26.20

# What is this?
This project includes two methods which both populate arrays of size n with the first n elements of the Fibonacci sequence. One function, Fibo1()
does this sequentially, the easy way, directly from the definition of the Fibonacci sequence. The other, Fibo2(), uses the explicit formula
for the Fibonacci sequence.

## Python multiprocessing
  In this version, Fibo2() is implemented using Python multiprocessing. The main() method will set up a timer and runs both Fibo1() and Fibo2(), printing their respective times.
### Which is faster?
  This isn't a great example of parallelization, and I'm working on better implementations that might better use multiprocessing. The sequential function Fibo1() is much, much faster than the parallelized version Fibo2(). This is because of overhead costs associated with creating multiple processes, and because there is so little computation involved with finding the next value in the sequential version.

## C++ and CUDA
The C++ version of this project is currently on hold. As implemented currently, these functions simply run and print values of the Fibonacci sequence, without any concurrency.
In the future I hope to implement this using C++ and CUDA. Unfortunately I can't yet because my graphics card doesn't support CUDA :pensive:

### Which is faster?
  My prediction is that for very small values of n (like 3 or so), Fibo1() will be slightly faster because of the setup
    time associated with multiprocessing. As n gets large, of course Fibo2() should eventually be faster. Because GPU processing with CUDA allows for many, many processes to run concurrently, this should allow for significant performance improvements.
