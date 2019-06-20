Ray Sidener, 6.20.19

This project is currently on hold.

This involves two methods which both populate arrays of size n with the first n elements of the Fibonacci sequence. One function, Fibo1()
does this sequentially, the easy way, directly from the definition of the Fibonacci sequence. The other, Fibo2(), uses the explicit formula
for the Fibonacci sequence.

As implemented currently (and for the forseeable future), these functions simply run and print. However, eventually the exciting part will
be implemented:
    Fibo2() is implemented using CUDA. The main() method sets up a timer and runs both Fibo1() and Fibo2(), printing their respective times.
    Which is faster? My prediction is that for very small values of n (like 3 or so), Fibo1() will be slightly faster because of the setup
    time associated with CUDA. As n gets large, of course Fibo2() will be much faster.
    
I can't implement this portion yet because my graphics card doesn't support CUDA :( At some point I might come back to this, either with a 
different machine or some software other than CUDA.
