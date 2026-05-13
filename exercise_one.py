"""
Section 3.6 (Chapter 3) made us understand that 'else' in an if...elif...else statement is Optional given that the if...elif satements 
already cover all possible conditions. this is the case in fig 4.1. The explanation in section 3.6 ges further to say 
"When an if…elif statement without an else tests a value that does not make any of its conditions True, 
the program does not execute any of the statement's suites. The next statement in sequence after the if…elif statement executes." 
This means that in the case of fig 4.1, without the else statement, no error is raised if none of the conditions is true. 
However, given that all possible die faces were accounted for in the if...elif statement, one condition will always be true.
"""