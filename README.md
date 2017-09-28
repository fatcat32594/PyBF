# PyBF
#### A Brainfuck Interpreter implemented in Python

##### Operations

Brainfuck is a simple language that consists of 8 operations, each represented
by a single character. All other characters are ignored.

Character | Operation
----------|----------
\> | Increment the data pointer by 1
< | Decrement the data pointer by 1
\+ | Increment the data at the data pointer, by 1
\- | Decrement the data at the data pointer, by 1
\. | Output the data at the data pointer, as a character.
, | Read in a single character, then store that at the current location of the data pointer
\[ |	If the data at the data pointer is zero, jump the instruction pointer forward to the character after the matching ']'
\] |	If the data at the data pointer is nonzero, jump the instruction pointer back to the character after the matching '['

##### Implementation Concerns

Brainfuck theoretically utilizes an infinitely long array of bytes as it's data storage. This is impossible due to real limits on memory. Therefore, this implementation uses an expanding python array of ints, each element of which starts as a zero.

Similarly, this interpreter throws an error if the program attempts to move before the data array start (some implementations wrap around).
