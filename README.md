BinarySearchMonitor
===================

Simple command line monitor to check the actions happened in your binary search algorithm

##About how to use this monitor

1. There are 3 files in this repo:
  * `binarysearch.py`: contains 3 frequently used binary search algorithms
  * `monitor.py`: mainly used for recording the runtime data
  * `client.py`: same as the main file, the basic interface to command line shell

2. You could just typein:

  ```
  python client.py [number bound] [lower bound] [upper bound]
  ```
  
  * `number bound`: number of elements in the list which will be bisearched
  * `lower bound`: smallest number in the list
  * `upper bound`: largest number in the list
  * I create the list randomly, using `random.randint(lower_bound, upper_bound)`.
  
  For example:
  ```
  python client.py 10 1 100
  ```
  
  will creates:
  ```
  List->[2, 2, 5, 8, 33, 41, 66, 68, 84, 87]
  ```
  
##How to read output?

Basically the output for command:
```
python client.py 10 1 100
```
will be like this:
```
List->[2, 2, 5, 8, 33, 41, 66, 68, 84, 87]
Val ->66
Monitor initialized ...
Testing 'regular' binary search ...
Inserted #(low,high)=(    0,    9) ...
Inserted #(low,high)=(    5,    9) ...
Inserted #(low,high)=(    5,    6) ...
Inserted #(low,high)=(    6,    6) ...
->Record List:
[ 2 {l} , 2 , 5 , 8 , 33 *mid* , 41 , 66 , 68 , 84 , 87 (h) ]
[ 2 , 2 , 5 , 8 , 33 , 41 {l} , 66 , 68 *mid* , 84 , 87 (h) ]
[ 2 , 2 , 5 , 8 , 33 , 41 {l} *mid* , 66 (h) , 68 , 84 , 87 ]
[ 2 , 2 , 5 , 8 , 33 , 41 , 66 (h) {l} *mid* , 68 , 84 , 87 ]
#index=  6
find=   66 : real=   66
Testing 'lowerbound' binary search ...
Inserted #(low,high)=(    0,    9) ...
Inserted #(low,high)=(    5,    9) ...
Inserted #(low,high)=(    5,    6) ...
Inserted #(low,high)=(    6,    6) ...
->Record List:
[ 2 {l} , 2 , 5 , 8 , 33 *mid* , 41 , 66 , 68 , 84 , 87 (h) ]
[ 2 , 2 , 5 , 8 , 33 , 41 {l} , 66 , 68 *mid* , 84 , 87 (h) ]
[ 2 , 2 , 5 , 8 , 33 , 41 {l} *mid* , 66 (h) , 68 , 84 , 87 ]
[ 2 , 2 , 5 , 8 , 33 , 41 , 66 (h) {l} *mid* , 68 , 84 , 87 ]
#index=  6
find=   66 : real=   66
Testing 'upperbound' binary search ...
Inserted #(low,high)=(    0,    9) ...
Inserted #(low,high)=(    5,    9) ...
Inserted #(low,high)=(    5,    6) ...
Inserted #(low,high)=(    6,    6) ...
->Record List:
[ 2 {l} , 2 , 5 , 8 , 33 *mid* , 41 , 66 , 68 , 84 , 87 (h) ]
[ 2 , 2 , 5 , 8 , 33 , 41 {l} , 66 , 68 *mid* , 84 , 87 (h) ]
[ 2 , 2 , 5 , 8 , 33 , 41 {l} *mid* , 66 (h) , 68 , 84 , 87 ]
[ 2 , 2 , 5 , 8 , 33 , 41 , 66 (h) {l} *mid* , 68 , 84 , 87 ]
#index=  6
find=   66 : real=   66
```

Let me explain this patch by patch:

1. **Initialization**:
  ```
  List->[2, 2, 5, 8, 33, 41, 66, 68, 84, 87]
  Val ->66
  ```
  * First line tells you the testing dataset:
    * The `List` will be generated randomly
  * `Val` is our target, also this one will be generated randomly

2. **Running**:
 ```
 Testing 'regular' binary search ...
 Inserted #(low,high)=(    0,    9) ...
 Inserted #(low,high)=(    5,    9) ...
 Inserted #(low,high)=(    5,    6) ...
 Inserted #(low,high)=(    6,    6) ...
 ```
 * First line indicates the type of binary search we are using, there are 3 of them:
   * regular: immediately return when meets the target
   * lowerbound: assigns `mid - 1` to `h`, and exits only if not satisfies `l <= h`
   * upperbound: assigns `mid + 1` to `l`, and exits only if not satisfies `l <= h`
 * Following lines will show you the whole procedure, these are useless, we will show you more visual results.

3. **Analysis**:
  ```
  ->Record List:
  [ 2 {l} , 2 , 5 , 8 , 33 *mid* , 41 , 66 , 68 , 84 , 87 (h) ]
  [ 2 , 2 , 5 , 8 , 33 , 41 {l} , 66 , 68 *mid* , 84 , 87 (h) ]
  [ 2 , 2 , 5 , 8 , 33 , 41 {l} *mid* , 66 (h) , 68 , 84 , 87 ]
  [ 2 , 2 , 5 , 8 , 33 , 41 , 66 (h) {l} *mid* , 68 , 84 , 87 ]
  #index=  6
  find=   66 : real=   66
  ```
  * All the lists outputed are formatted like this, in the current status:
    * if the element's index is equal to the `l` value, and mark of `{l}` will be appended.
    * if the element's index is equal to the `h` value, and mark of `(h)` will be appended.
    * if the element's index is equal to the `mid` value, and mark of `*mid*` will be appended.
  * The last 2 lines contain the result

4. **HOWTO: Monitor.py**
  
You may want to define your binary search algorithm, you could use the module `monitor`

1. There is a class called `Monitor` in that file, so you could declare an instance first:
  
  ```
  _monitor = monitor.Monitor(Datalist)
  ```
2. `insert` method will add a record to the `record` list inside the class instance.
3. `show_record` will show you the runtime record, formattted.


