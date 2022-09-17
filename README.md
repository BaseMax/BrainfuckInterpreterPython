# Brainfuck Interpreter in Python

## Using

```
$ python brainfuck.py
```

## Tokens

| Token | Description |
| ----- | --------------------------- |
| >	| Move the pointer to the right |
| <	| Move the pointer to the left |
| +	| Increment the memory cell at the pointer |
| -	| Decrement the memory cell at the pointer |
| .	| Output the character signified by the cell at the pointer |
| ,	| Input a character and store it in the cell at the pointer |
| [	| Jump past the matching ] if the cell at the pointer is 0 |
| ]	| Jump back to the matching [ if the cell at the pointer is nonzero |
| any | All characters other than ><+-.,[] should be considered comments and ignored |

### ASCII Table

https://en.wikipedia.org/wiki/ASCII

© Copyright 2022, Max Base
