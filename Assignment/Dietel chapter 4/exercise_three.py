"""
The problem is that the function is missing a return statement. 
Section 4.2 states that "When there's no return statement in a function, 
it implicitly returns the value None after executing the last statement in the function's block." 
This means thatcube(2) gives back None instead of 8, and the print statement ends up displaying: 
The cube of 2 is None.
"""