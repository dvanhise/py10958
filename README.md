## py10958
Solving the 10958 problem asked [in this Numberphile video](https://www.youtube.com/watch?v=-ruC5A9EzzE)

More generally, if I start with the sequence of numbers `1 2 3 4 5 6 7 8 9`, what results can I get by adding operations, mathematical symbols, or concatenating the numbers without changing their order?

For example:
|  |  |
| ----- | - |
| 1 | `1^23456789` |
| 2 | `123+4-56-78+9` |
| 3 | `123-45-6-78+9` |
| 999 | `12^3+4+56-789` |
| 1000 | `1-23*45+678*√9` |
| 90373 | `1+(2^3+4-5!+6*7!-8)*√9` |

py10958 generates mathematical statements following the rules and gathers the best integer results.

`best_results.txt` contains the most recent version of all positive integer results up to 100,000 I've generated running the code so far. 

## Usage
To run all possible sequences the code can generate, use `python main.py run 0`.  My best runtime estimate is about two years on my desktop.

But fear not, results are constantly accumulated and saved.  The search set of expressions is broken into segments which have sub-segments.  The console will inform you what segment and sub-segment it's looking at.  You can pick up where you left off with `python main.py run x y` where `x` and `y` are segment and optional sub-segment respectively. 

To generate a results file from the database with `python main.py results`.  It is called `output.txt`.