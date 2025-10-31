# Synced Notion Notes

L9

 Print All Factors of a Given Number



better

```
from typing import List

def factors(num: int) -> List[int]:
    factors = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            factors.append(i)
    factors.append(num)
    return factors
```



optimal 

```
from typing import List
from math import sqrt


def factors(num: int) -> List[int]:
    factors = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            if num // i != i:
                factors.append(num // i)
    factors.sort()  # Do this only if you want in sorted order
    return factors
```







L10





L11

Q:  freq of m in n  

using hashing  → using list





using Dict → even work if 1st constraint is also  not given



Q:  freq of m in n   for string







UL - LL - 1   ( when both exclusive )

UL - LL - 1   ( when both inclusive )

UL - LL         ( when any one inclusive  & other exclusive )

define 

```
int max =  Integer.MIN_VALUE;
```



```
char ch = 'd';
int index = ch - 'a'; // index = 3
```



Java

int[] arr = {10, 20, 30, 40, 50};
int N = arr.length;
int i = 0; // Start at index 0

for (int step = 0; step < 7; step++) {
    System.out.println(arr[i]);
    i = (i - 1 + N) % N; // Move backward and wrap around
}

### Dry Run Table:

index get into 0 after reaching end

```
(i + 1) % n      //cycles forward.
(i - 1 + n) % n   //cycles backward.
```









```
        int arr[] = new int[3];
        arr[0] = 4;
        System.out.println(arr[0]);    // 4
        int brr[] = arr;               // --> both point to same 
        brr[0] = 8;
        System.out.println(arr[0]);    //8
```



## 1. Overview of Java Collections Framework

The Java Collections Framework provides a set of classes and interfaces for storing and manipulating data efficiently. It includes:

- Interfaces: List, Set, Map, Queue, Deque
- Implementations: ArrayList, LinkedList, HashSet, TreeSet, HashMap, TreeMap, PriorityQueue, etc.
## 2. List

### What is a List?

- A List is an ordered collection that allows duplicate elements.
- Common implementations:
- ArrayList: Resizable-array implementation.
- LinkedList: Doubly-linked list implementation.
### How to Initialize a List?

```
// ArrayList Initialization
List<Integer> arrayList = new ArrayList<>();
arrayList.add(1);
arrayList.add(2);

// LinkedList Initialization
List<Integer> linkedList = new LinkedList<>();
linkedList.add(3);
linkedList.add(4);

```

### Common Functions & Methods (with complexity):

### How to Use Common Methods?

```
arrayList.add(5);                    // add element
int x = arrayList.get(1);            // get element
arrayList.set(2, 100);               // update element
arrayList.remove(0);                 // remove by index
boolean hasVal = arrayList.contains(100); // check contains
int idx = arrayList.indexOf(100);    // index of element
arrayList.clear();                   // clear all

```

### Time Complexity:

### Space Complexity:

- ArrayList: O(n) for storage.
- LinkedList: O(n) for nodes + O(n) pointers.
### Use Cases:

- Use ArrayList for fast random access.
- Use LinkedList for frequent insertions/deletions.
## 3. Set

### What is a Set?

- A Set is an unordered collection that does not allow duplicate elements.
- Common implementations:
- HashSet: Backed by a HashMap.
- TreeSet: Sorted set backed by a balanced binary tree.
### How to Initialize a Set?

```
// HashSet Initialization
Set<Integer> hashSet = new HashSet<>();
hashSet.add(5);
hashSet.add(6);

// TreeSet Initialization
Set<Integer> treeSet = new TreeSet<>();
treeSet.add(7);
treeSet.add(8);

```

### Common Functions & Methods (with complexity):

### How to Use Common Methods?

```
hashSet.add(10);                // add element
hashSet.remove(5);              // remove element
boolean exists = hashSet.contains(6); // check contains
treeSet.first();                // first element in sorted order
treeSet.last();                 // last element in sorted order

```

### Time Complexity:

### Space Complexity:

- HashSet: O(n) for storage.
- TreeSet: O(n) for nodes.
### Use Cases:

- Use HashSet for fast lookups.
- Use TreeSet for sorted sets.
## 4. Map

### What is a Map?

- A Map stores key-value pairs.
- Common implementations:
- HashMap: Unordered key-value store.
- TreeMap: Sorted key-value store.
### How to Initialize a Map?

```
// HashMap Initialization
Map<String, Integer> hashMap = new HashMap<>();
hashMap.put("key1", 10);
hashMap.put("key2", 20);

// TreeMap Initialization
Map<String, Integer> treeMap = new TreeMap<>();
treeMap.put("key3", 30);
treeMap.put("key4", 40);

```

### Common Functions & Methods (with complexity):

### How to Use Common Methods?

```
hashMap.put("a", 1);                    // add entry
int value = hashMap.get("key1");        // get value
hashMap.remove("key2");                 // remove entry
boolean hasKey = hashMap.containsKey("a"); // check if key exists
for (String k : hashMap.keySet()) {     // iterate keys
    System.out.println(k + " " + hashMap.get(k));
}

```

### Time Complexity:

### Space Complexity:

- HashMap: O(n) for storage.
- TreeMap: O(n) for nodes.
### Use Cases:

- Use HashMap for fast lookups.
- Use TreeMap for sorted key-value pairs.
## 5. Queue

### What is a Queue?

- A Queue is a collection designed for FIFO (First-In-First-Out) order.
- Common implementations:
- LinkedList: Implements Queue interface.
- PriorityQueue: A queue where elements are ordered by priority.
### How to Initialize a Queue?

```
// LinkedList Queue Initialization
Queue<Integer> linkedListQueue = new LinkedList<>();
linkedListQueue.add(50);
linkedListQueue.add(60);

// PriorityQueue Initialization
Queue<Integer> priorityQueue = new PriorityQueue<>();
priorityQueue.add(70);
priorityQueue.add(80);

```

### Common Functions & Methods (with complexity):

### How to Use Common Methods?

```
queue.add(100);
queue.offer(200);
int head = queue.poll();        // retrieves and removes head or null
queue.peek();                   // retrieves but does not remove head

```

### Time Complexity:

### Space Complexity:

- LinkedList Queue: O(n) for storage.
- PriorityQueue: O(n) for heap.
### Use Cases:

- Use PriorityQueue for ordering elements based on priority.
## 6. Deque

### What is a Deque?

- A Deque is a double-ended queue that allows inserting and removing elements from both ends.
- Common implementations:
- ArrayDeque: Efficient resizable-array implementation.
### How to Initialize a Deque?

```
// ArrayDeque Initialization
Deque<Integer> deque = new ArrayDeque<>();
deque.addFirst(90);
deque.addLast(100);

```

### Common Functions & Methods (with complexity):

### How to Use Common Methods?

```
deque.addFirst(1);         // push to front
deque.addLast(2);          // push to end
deque.removeFirst();       // pop from front
deque.removeLast();        // pop from end

```

### Time Complexity:

### Space Complexity:

- ArrayDeque: O(n) for storage.
### Use Cases:

- Use Deque for stack and queue operations in a single structure.
## 7. Stack

### What is a Stack?

- A Stack is a collection designed for LIFO (Last-In-First-Out) order.
```
1. List Interface (e.g., ArrayList, LinkedList) // Commonly Used
add(E e);                    // Adds element to the list
add(int index, E element);   // Adds element at a specific index
get(int index);              // Returns element at the specified index
set(int index, E element);   // Replaces element at the specified index
remove(int index);           // Removes element at a specific index
remove(Object o);            // Removes the first occurrence of the specified element
contains(Object o);          // Checks if the list contains the specified element
indexOf(Object o);           // Returns the index of the first occurrence of the specified element
lastIndexOf(Object o);       // Returns the index of the last occurrence of the specified element
size();                      // Returns the number of elements in the list
isEmpty();                   // Checks if the list is empty
subList(int fromIndex, int toIndex); // Returns a view of the portion of this list
toArray();                   // Converts the list to an array
sort(Comparator<? super T> c); // Sorts the list

```

###  Arrays Class (for Array Manipulation)

```

Arrays.sort(T[] a);                   // Sorts the array
Arrays.binarySearch(T[] a, T key);    // Searches for a key in the array
Arrays.copyOf(T[] original, int newLength); // Copies array to a new array with new length
Arrays.fill(T[] a, T val);            // Fills the array with the specified value
Arrays.equals(T[] a, T[] b);          // Compares two arrays
Arrays.toString(T[] a);               // Returns a string representation of the array
```

### . Utility Methods (Collections Class)

```
Collections.sort(List<T> list);        // Sorts the list in ascending order
Collections.reverse(List<T> list);    // Reverses the order of elements
Collections.shuffle(List<?> list);    // Randomly shuffles the list
Collections.max(Collection<T> coll); // Returns the maximum element
Collections.min(Collection<T> coll); // Returns the minimum element
Collections.frequency(Collection<?> coll, Object o); // Counts occurrences of an element
Collections.binarySearch(List<? extends Comparable<? super T>> list, T key); // Searches using binary search
Collections.swap(List<?> list, int i, int j); // Swaps elements at two positions
```

### ✅ 1D Array → Elements in Set

```
java
CopyEdit
int[] arr = {1, 2, 3, 2, 1};

// Using a loop
Set<Integer> set = new HashSet<>();
for (int num : arr) {
    set.add(num);
}
```

### ✅ 2D Array → Store Each Sub-array as an Element (Set of arrays)

You can do this only if you treat sub-arrays as objects (e.g., int[][] arr → Set of int[]):

```
java
CopyEdit
int[][] arr = {
    {1, 2},
    {3, 4},
    {1, 2}
};

Set<List<Integer>> set = new HashSet<>();
for (int[] subArray : arr) {
    set.add(Arrays.asList(subArray[0], subArray[1]));
}
```

###  ✅List → Set

```
java
CopyEdit
List<String> list = Arrays.asList("a", "b", "a");

Set<String> set = new HashSet<>(list);
```



### ✅ 2D array → Map

For example, if you have:

```
java
CopyEdit
String[][] array = {
    {"a", "1"},
    {"b", "2"},
    {"c", "3"}
};
```

You can convert it into a Map<String, String> like this:

```
java
CopyEdit
Map<String, String> map = new HashMap<>();
for (String[] pair : array) {
    map.put(pair[0], pair[1]);
}
```

### ✅   1D array (index → value) → Map<Integer, Integer>

```
java
CopyEdit
int[] arr = {10, 20, 30};

Map<Integer, Integer> map = new HashMap<>();
for (int i = 0; i < arr.length; i++) {
    map.put(i, arr[i]); // key = index, value = element
}
```

## ✅  List → Map

### Example: List of Strings → Map (Index → Value)

```
java
CopyEdit
List<String> list = Arrays.asList("a", "b", "c");

Map<Integer, String> map = new HashMap<>();
for (int i = 0; i < list.size(); i++) {
    map.put(i, list.get(i));
}
```

## 🔹 1. Array Basics

```
java
CopyEdit
// Declaration
int[] arr = new int[5];          // Default values = 0
int[] arr2 = {1, 2, 3, 4, 5};    // Initialized

// Access elements
int first = arr2[0];

// Length
int n = arr2.length;
```

## 🔹 2. Array Input & Output

```
java
CopyEdit
Scanner sc = new Scanner(System.in);
int n = sc.nextInt();
int[] arr = new int[n];

for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

for (int num : arr) System.out.print(num + " ");
```

## 🔹 3. Sorting Arrays

```
java
CopyEdit
Arrays.sort(arr);  // Ascending

// Descending
Integer[] arr = {4, 1, 3};
Arrays.sort(arr, Collections.reverseOrder());
```

## 🔹 4. Binary Search (Sorted Only)

```
java
CopyEdit
int idx = Arrays.binarySearch(arr, key);
```

## 🔹 5. Find Max / Min in Array

```
java
CopyEdit
int max = Arrays.stream(arr).max().getAsInt();
int min = Arrays.stream(arr).min().getAsInt();
```

## 🔹 6. Reverse an Array

```
java
CopyEdit
for (int i = 0; i < arr.length / 2; i++) {
    int temp = arr[i];
    arr[i] = arr[arr.length - i - 1];
    arr[arr.length - i - 1] = temp;
}
```

```

    public static void main(String[] args) {
        int arr[] = {1, 3, 4, 5, 5};
        int start = 0;
        int end = arr.length - 1;

        while (start < end) {
            // Swap elements
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;

            // Move pointers
            start++;
            end--;
        }

        System.out.println(Arrays.toString(arr)); // Output: [5, 5, 4, 3, 1]
    }

```

## 🔹 7. Prefix Sum Array

```
java
CopyEdit
int[] prefix = new int[n];
prefix[0] = arr[0];
for (int i = 1; i < n; i++) {
    prefix[i] = prefix[i - 1] + arr[i];
}
```

## 🔹 8. Frequency Count with HashMap

```
java
CopyEdit
Map<Integer, Integer> freq = new HashMap<>();
for (int num : arr) {
    freq.put(num, freq.getOrDefault(num, 0) + 1);
}
```

## 🔹 9. Convert Array to List

```
java
CopyEdit
String[] arr = {"a", "b", "c"};
List<String> list = Arrays.asList(arr); // Fixed-size
List<String> modifiable = new ArrayList<>(list);
```

## 🔹 10. Convert List to Array

```
java
CopyEdit
List<String> list = new ArrayList<>();
list.add("a");
String[] arr = list.toArray(new String[0]);
```

## 🔹 11. Remove Duplicates

```
java
CopyEdit
Set<Integer> set = new HashSet<>();
for (int num : arr) set.add(num);
```

# 🟩 Java ArrayList Essentials

## 🔹 1. Declaration

```
java
CopyEdit
List<Integer> list = new ArrayList<>();
```

## 🔹 2. Basic Operations

```
java
CopyEdit
list.add(10);
list.get(0);
list.set(1, 20);
list.remove(0);
list.contains(10);
list.isEmpty();
```

## 🔹 3. Looping through List

```
java
CopyEdit
for (int num : list) System.out.println(num);

for (int i = 0; i < list.size(); i++) {
    System.out.println(list.get(i));
}
```

## 🔹 4. Sorting

```
java
CopyEdit
Collections.sort(list);                         // Ascending
Collections.sort(list, Collections.reverseOrder()); // Descending
```

## 🔹 5. Convert ArrayList to Array

```
java
CopyEdit
Integer[] array = list.toArray(new Integer[0]);
```

## 🔹 6. SubList

```
java
CopyEdit
List<Integer> sub = list.subList(1, 4); // index 1 to 3
```

## 🔹 7. Remove All Occurrences

```
java
CopyEdit
list.removeIf(x -> x == 3);
```

## 🔹 8. Frequency Count in List

```
java
CopyEdit
int freq = Collections.frequency(list, 3);
```

# 💡 Common DSA Patterns with Arrays

### ✅ 1D Array → Elements in Set

```

int[] arr = {1, 2, 3, 2, 1};

// Using a loop
Set<Integer> set = new HashSet<>();
for (int num : arr) {
    set.add(num);
}
```

### ✅ 2D Array → Store Each Sub-array as an Element (Set of arrays)

You can do this only if you treat sub-arrays as objects (e.g., int[][] arr → Set of int[]):

```

int[][] arr = {
    {1, 2},
    {3, 4},
    {1, 2}
};

Set<List<Integer>> set = new HashSet<>();
for (int[] subArray : arr) {
    set.add(Arrays.asList(subArray[0], subArray[1]));
}
```

###  ✅List → Set

```

List<String> list = Arrays.asList("a", "b", "a");

Set<String> set = new HashSet<>(list);
```



### ✅ 2D array → Map

For example, if you have:

```
java
CopyEdit
String[][] array = {
    {"a", "1"},
    {"b", "2"},
    {"c", "3"}
};
```

You can convert it into a Map<String, String> like this:

```
java
CopyEdit
Map<String, String> map = new HashMap<>();
for (String[] pair : array) {
    map.put(pair[0], pair[1]);
}
```

### ✅   1D array (index → value) → Map<Integer, Integer>

```
java
CopyEdit
int[] arr = {10, 20, 30};

Map<Integer, Integer> map = new HashMap<>();
for (int i = 0; i < arr.length; i++) {
    map.put(i, arr[i]); // key = index, value = element
}
```

## ✅  List → Map

### Example: List of Strings → Map (Index → Value)

```
java
CopyEdit
List<String> list = Arrays.asList("a", "b", "c");

Map<Integer, String> map = new HashMap<>();
for (int i = 0; i < list.size(); i++) {
    map.put(i, list.get(i));
}
```

### 1. Set Interface (e.g., HashSet, TreeSet, LinkedHashSet)

```
java
CopyEdit
add(E e);                    // Adds element to the set
remove(Object o);            // Removes the specified element
contains(Object o);          // Checks if the set contains the specified element
size();                      // Returns the number of elements in the set
isEmpty();                   // Checks if the set is empty
iterator();                  // Returns an iterator for the set
clear();                     // Removes all elements from the set
toArray();                   // Converts the set to an array


```

### 2. Map Interface (e.g., HashMap, TreeMap, LinkedHashMap)

```
java
CopyEdit
put(K key, V value);         // Inserts OR UPDATE a key-value pair
putIfAbsent(K key, V value); // Inserts a key-value pair only if the key is not already mapped
get(Object key);             // Returns the value associated with the key
getOrDefault(Object key, V defaultValue); // Returns the value or a default value if the key is not found
containsKey(Object key);     // Checks if the map contains the specified key
containsValue(Object value); // Checks if the map contains the specified value
remove(Object key);          // Removes the mapping for the specified key
replace(K key, V value);     // Replaces the value for a key if it exists
keySet();                    // Returns a set of all keys
values();                    // Returns a collection of all values
entrySet();                  // Returns a set of key-value pairs
size();                      // Returns the number of key-value mappings
isEmpty();                   // Checks if the map is empty

```

```
Find Key By Value 

for (Map.Entry<String, Integer> entry : myMap.entrySet()) {
    if (entry.getValue().equals(2)) {
        System.out.println(entry.getKey());
        break;
    }
}
```

### 💡 Bonus: getKey()

Similarly, entry.getKey() gets the key of that entry.

```
java
CopyEdit
Map.Entry<String, Integer> entry = Map.entry("banana", 7);
System.out.println(entry.getKey());   // banana
System.out.println(entry.getValue()); // 7


```

## 🔶 Array: Common DSA Pattern Types

Once you're confident with the basics, move to the following array problem-solving patterns:

### 1. Two Pointers

- Use when array is sorted or you're checking pairs. O(n²) ⇒ O(n)
- if unsorted  > first sort it > O(n²) ⇒ O( n logn )
- 🔍 Problems:
- finding duplicates / palindrome / pair related -  sub , difference of any pair
- reverse of any particular section
- merge two sorted 
- Pair with target sum
- Remove duplicates
- Reverse array
- Sort colors (Dutch national flag)
- 🧠 Pattern: Left and right pointer, move inward based on condition.
- 🔧 Code Template:
```
int left = 0, right = arr.length - 1;
while (left < right) {
    int sum = arr[left] + arr[right];
    if (sum == target) break;
    else if (sum < target) left++;
    else right--;
}
```

### 2. Sliding Window

- O(n²) ⇒ O(n)
- Use when you're dealing with subarrays, windowed calculations.
- 🔍 Problems:  > fixed size window / dynamic size window
- to find maximum , minimum or any target of {subarray , substring , subsequence}
- ✅longest subarray / substring 
-  finding a part of any subarray, substring
- Maximum sum subarray of size k
- Longest substring with at most K distinct characters
- Minimum size subarray sum
- 🧠 Pattern: Expand window → check condition → shrink window.
- 🔧 Code Template:
```
int windowSum = 0, maxSum = 0;
for (int i = 0; i < k; i++) windowSum += arr[i];
maxSum = windowSum;
for (int i = k; i < arr.length; i++) {
    windowSum += arr[i] - arr[i - k];
    maxSum = Math.max(maxSum, windowSum);
}

```

### 3. Prefix Sum

- Use for range sums, difference arrays, cumulative data.
- 🔍 Problems:
- Range sum queries
- Subarray sum equals K
- Even count subarrays
- 🧠 Pattern: Build a prefix sum array, use it for quick lookup.
- 🔧 Code Template:
```
int[] prefix = new int[arr.length + 1];
for (int i = 0; i < arr.length; i++) {
    prefix[i + 1] = prefix[i] + arr[i];
}
// range sum from l to r = prefix[r+1] - prefix[l]

```

### 4. Hashing / HashMap / Frequency Map

- Use for counting, quick lookup, removing duplicates.
- 🔍 Problems:
- Two sum
- Majority element
- Longest consecutive sequence
- 🧠 Pattern: Use dictionary to track frequency/index/count.
- 🔧 Code Template:
```
Map<Integer, Integer> map = new HashMap<>();
for (int num : arr) {
    map.put(num, map.getOrDefault(num, 0) + 1);
}

```

### 5. Binary Search on Answer

- Use when problem asks for minimum or maximum value that satisfies a condition.
- 🔍 Problems:
- Capacity to ship packages within D days
- Minimum number of days to make m bouquets
- 🧠 Pattern: Search over possible answers rather than indices.
- 🔧 Code Template:
```
int low = minValue, high = maxValue;
while (low < high) {
    int mid = low + (high - low) / 2;
    if (isValid(mid)) high = mid;
    else low = mid + 1;
}
return low;

```

### 5(A) . Standard Binary Search

- Sorted arrays / Monotonic conditions
- Variants:
- First/last occurrence
- Lower/upper bound
- Search in rotated sorted array
- 🔍 Problems:
- Binary search on answers
- Peak element
- Search in infinite array
```
int l = 0, r = arr.length - 1;
while (l <= r) {
    int mid = l + (r - l) / 2;
    if (arr[mid] == target) return mid;
    else if (arr[mid] < target) l = mid + 1;
    else r = mid - 1;
}
```



### 6. Kadane’s Algorithm

- Use for maximum subarray sum problems.
- 🧠 Pattern: Keep track of current sum and max sum.
- 🔧 Code Template:
```
int max = arr[0], curr = arr[0];
for (int i = 1; i < arr.length; i++) {
    curr = Math.max(arr[i], curr + arr[i]);
    max = Math.max(max, curr);
}

```

### 7. Greedy

- Use when locally optimal choices lead to global optimal.
- 🔍 Problems:
- Jump Game
- Partition labels
- Candy problem
- 🧠 Pattern: Iteratively take best choice.
- 🔧 Example Snippet (Jump Game):
```
int reach = 0;
for (int i = 0; i <= reach; i++) {
    reach = Math.max(reach, i + nums[i]);
    if (reach >= nums.length - 1) return true;
}
return false;

```

### 8. Monotonic Stack/Queue (Advanced)

- Use for next greater element, range minimum/maximum.
- 🔍 Problems:
- Trapping Rain Water
- Largest Rectangle in Histogram
- 🧠 Pattern: Maintain increasing/decreasing stack.
- 🔧 Code Template:
```
Stack<Integer> stack = new Stack<>();
for (int i = 0; i < arr.length; i++) {
    while (!stack.isEmpty() && arr[stack.peek()] < arr[i]) {
        stack.pop();
    }
    stack.push(i);
}

```

### 9. Backtracking / Recursion

- Use when you need to explore all combinations/permutations.
- 🔍 Problems:
- Subsets
- Permutations
- 🧠 Pattern: Recursive calls with different choices.
- 🔧 Code Template:
```
void backtrack(List<List<Integer>> res, List<Integer> temp, int[] nums, boolean[] used) {
    if (temp.size() == nums.length) {
        res.add(new ArrayList<>(temp));
        return;
    }
    for (int i = 0; i < nums.length; i++) {
        if (used[i]) continue;
        used[i] = true;
        temp.add(nums[i]);
        backtrack(res, temp, nums, used);
        used[i] = false;
        temp.remove(temp.size() - 1);
    }
}

```

Let me know if you’d like additional code examples or practice problems for each!

- Understand and apply:
- Prefix Sum
- Sliding Window
- Two Pointers
- Master:
- Hash Maps
- Kadane’s Algorithm
- Binary Search on Answer
- Greedy & Backtracking
- Explore advanced:
- Monotonic Stack
- Bit Manipulation
- Recursion + DP




## 1. Constant Window  

standard code

## 2. Longest subarray /  substring with <condt>

```
//Brute force for max of subarray of size < k
// by generating all subarrays

//O(N*N)

 max_len =0
 
for(int i=0 to n-1 ){
sum = 0
	 for ( j= i to n-1) {
				 sum = sum + arr[j];
				 if (sum <= k) max_len = MAX(max_len m, j-i+1 );
				 else if (sum > k) break;
				 }
				 }
	 
```



if we need to find subarray than use while loop and time complexity O(2N)

```
//optimised by using sliding window

/*
time = O(2N) 
space = O(1)
*/

l = 0
r = 0 
max_len = 0
sum = 0
while( n < r){
	sum = sum + arr[r];
 
		 if ( sum > k ) {
				 sum = sum - arr[l];
				 l = l + 1 ; }
 
 
		if( sum <= k ) {
			 max_len = MAX(max_len , r - l + 1);
				r = r +1 } 
		 }
```



if it asking , MAX Length , then while loop can be replaced by if ,  TC = O(N)

```
//optimised by using sliding window

/*
time = O(N) 
space = O(1)
*/

l = 0
r = 0 
max_len = 0
sum = 0

if( n < r){
		sum = sum + arr[r];
 
		 if ( sum > k ) {
			 sum = sum - arr[l];
				 l = l + 1 ; }
 
 
		if( sum <= k ) {
			 max_len = MAX(max_len , r - l + 1);
				r = r +1 }
		 }
```

## 3. No. of subarrays /  substring with <condt>



## 4. Minimum  subarrays /  substring with <condt>



## ✅Two Pointers 



T1 ) yes/no

T2) tell the index



using hashmap  -

optimal for telling index

```
TC : O(N)
SC : O(N)
```

```
class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer, Integer> hm = new HashMap<>();

        for (int i =0;i<nums.length;i++){

            int complement = target- nums[i];
            if(hm.containsKey(complement)){
                return new int [] {hm.get(complement), i};

            }
            hm.put(nums[i], i);
        }
        return new int [] {-1,-1};
    }
}
```





2 pointer —> always work on sorted array

optimal for telling yes / no

TC : O(NlogN)
SC : O(1)

but first sort the array

```
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int N = nums.length;
        int[][] arr = new int[N][2];
        for (int i=0; i<N; i++) {
            arr[i] = new int[] {nums[i], i};
        }
        Arrays.sort(arr, (a1, a2) -> a1[0]-a2[0]);
        int left = 0;
        int right = N-1;

        while (left < right) {  // not <= since numbers must have distinct indices
            int sum = arr[left][0] + arr[right][0];
            if (sum == target) {
                return new int[] {arr[left][1], arr[right][1]};
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }

        return new int[] {};    // will never execute since solution is guaranteed to exist
    }
}
```



sorted array

```
public int[] twoSum(int[] nums, int target) {
	int l = 0, r = nums.length - 1;
	
	while (nums[l] + nums[r] != target) {
		if (nums[l] + nums[r] < target) l++;
		else r--;
	}

	return new int[] {l+1, r+1};
}
```

```
Time Complexity: O(n)
Space Complexity: O(1)
```

https://leetcode.com/problems/3sum/solutions/3736346/java-easiest-solution-ever/

brute force 
🔴 Time Complexity: O(n^3)

```
import java.util.*;

public class ThreeSumBruteForce {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> result = new HashSet<>();
        int n = nums.length;

        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        List<Integer> triplet = Arrays.asList(nums[i], nums[j], nums[k]);
                        Collections.sort(triplet); // To avoid permutation duplicates
                        result.add(triplet);
                    }
                }
            }
        }
        return new ArrayList<>(result);
    }
}

```



Two-Pointer (Sorted) ✅ optimised

```
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // Sort the array to make it easier to avoid duplicates and use two pointers
        Arrays.sort(nums); // O(n log n)
        
        // This will store the final list of triplets that sum to zero
        List<List<Integer>> result = new ArrayList<>();
        
        int tar = 0;  // Target sum for the triplet is zero

        // Iterate through each number, treating it as the first number in the triplet
        for (int i = 0; i < nums.length - 2; i++) {
            // Skip duplicate elements to avoid duplicate triplets
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int li = i + 1;             // Left pointer starts just after i
            int ri = nums.length - 1;   // Right pointer starts at the end of the array
            int ntar = tar - nums[i];   // New target sum for left + right is -nums[i]

            // Use two pointers to find pairs that sum up to ntar
            while (li < ri) {
                int sum = nums[li] + nums[ri];
                if (sum == ntar) {
                    // If sum of left and right equals target, add the triplet
                    result.add(Arrays.asList(nums[i], nums[li], nums[ri]));

                    // Skip duplicates on the left pointer
                    while (li < ri && nums[li] == nums[li + 1]) li++;

                    // Skip duplicates on the right pointer
                    while (li < ri && nums[ri] == nums[ri - 1]) ri--;

                    // Move both pointers inward after finding a valid triplet
                    li++;
                    ri--;
                } 
                else if (sum < ntar) {
                    // If sum is smaller than target, move left pointer to increase sum
                    li++;
                } 
                else {
                    // If sum is larger than target, move right pointer to decrease sum
                    ri--;
                }
            }
        }

        // Return all found triplets
        return result;
    }
}

```

### Summary of Approaches:



## ✅sliding window 

### ⬇️fixed size

```
class Solution {
    public double findMaxAverage(int[] nums, int k) {
     
      int li = 0 ; 
      int ri = k-1 ;
      double max_avg = Double.NEGATIVE_INFINITY;

      if(nums.length ==1) {
        return nums[0];}

      while(ri <= nums.length-1 ){
       double sum = 0;

        for(int i= li ; i<= ri ; i++){
             sum = sum + nums[i] ; //  accumulate sum first
            }
            double avg = sum/ k;

        if(avg > max_avg ){
            max_avg = avg;
        }

        li++;
        ri++;
      }
      return max_avg;  
    }
}
```


Constant fixed size sliding window 

- O(n) — Only one pass through the array.
- Space: O(1)
```
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double sum = 0;

        // Compute initial window sum
        for (int i = 0; i < k; i++) {
            sum += nums[i];
        }

        double maxSum = sum;

        // Slide the window
        for (int i = k; i < nums.length; i++) {
            sum = sum - nums[i - k] + nums[i]; // Remove leftmost, add rightmost
            maxSum = Math.max(maxSum, sum);
        }

        return maxSum / k; // Return the maximum average
    }
}
```



### ⬇️Dynamic size

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

###  Sliding Window with HashSet

- SC =O(K) 
- TC =O(n)
```
class Solution {
    public int lengthOfLongestSubstring(String s) {
      int n = s.length();
        HashSet<Character> seen = new HashSet<>();
        int maxLength = 0;
        int left = 0;

        for (int right = 0; right < n; right++) {
            // Shrink window until duplicate is removed
            while (seen.contains(s.charAt(right))) {
                seen.remove(s.charAt(left));
                left++;
            }

            // Add current character and update maxLength
            seen.add(s.charAt(right));
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
}
}
```

### Other approach→ 
Sliding Window with HashMap

- SC =O(K) 
- TC =O(n).
```
class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map =new HashMap<>();
int maxlen = 0 ;
int start  = 0 ; 

 for(int i= 0 ; i< s.length() ; i++ ){
    if(map.containsKey(s.charAt(i)) && map.get(s.charAt(i))>= start){
        start = map.get(s.charAt(i)) + 1;
    }
       map.put(s.charAt(i) ,i);
       maxlen = Math.max(maxlen , i - start +1);
 }
     return maxlen;
}
}


```



🔴 QUERY SUM OF ELEMENTS IN A SUBARRAY



https://www.youtube.com/watch?v=yuws7YK0Yng



```
public class PrefixSum {

    public static int[] calculatePrefixSum(int[] arr) {
        int[] prefixSum = new int[arr.length];
        prefixSum[0] = arr[0];

        for (int i = 1; i < arr.length; i++) {
            prefixSum[i] = prefixSum[i - 1] + arr[i];
        }

        return prefixSum;
    }
}
```

```
public class PrefixSumInPlace {

    public static void calculatePrefixSumInPlace(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            arr[i] = arr[i - 1] + arr[i];
        }
    }  
```



https://leetcode.com/problems/range-sum-query-immutable/description/

```
class NumArray {
private int [] prefixSum;

    public NumArray(int[] nums) {
       for(int i = 1 ; i < nums.length ; i++){
        nums[i] += nums[i-1];
       }
        this.prefixSum = nums;
    }
    
    public int sumRange(int left, int right) {
        if(left == 0) return prefixSum[right];
        return prefixSum[right] - prefixSum[left - 1];
    }
}
```

https://leetcode.com/problems/subarray-sum-equals-k/



```
class Solution {
    public int subarraySum(int[] nums, int k) {
        int count =0;
       for(int i = 1 ; i< nums.length ; i++){
        if(nums[i]==k)count++;
        nums[i]+= nums[i-1];
       }

       for(int j = nums.length-1 ; j >= 0; j--){
        if(nums[j]==k)count++;
            for(int i = 1 ; i< j ; i++){
                if((nums[j] - nums[i-1]) == k) count++;
            }
       }
       return count;
    }
}
```



### Optimized using HashMap and Prefix Sum

- Time complexity: O(n) 
- Space complexity: O(n)
```
class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;          // Total number of subarrays that sum to k
        int prefixSum = 0;      // Running prefix sum
        
        // Map to store frequency of prefix sums
        // Key: prefix sum, Value: frequency of that sum
        HashMap<Integer, Integer> prefixSumFreq = new HashMap<>();
        
        prefixSumFreq.put(0, 1); // Base case: empty subarray has sum 0

        for (int num : nums) {
            prefixSum += num; // Update running prefix sum

            // Check if there exists a prefixSum that if removed would result in sum k
            // That is: prefixSum - oldPrefix = k → oldPrefix = prefixSum - k
            if (prefixSumFreq.containsKey(prefixSum - k)) {
                count += prefixSumFreq.get(prefixSum - k); // Add the number of such occurrences
            }

            // Update the frequency of the current prefix sum
            prefixSumFreq.put(prefixSum, prefixSumFreq.getOrDefault(prefixSum, 0) + 1);
        }

        return count; // Total subarrays with sum equal to k
    }
}

```

https://leetcode.com/problems/contiguous-array/description/



Brute force  TC = O(N^2)  TLE

```
class Solution {
    public int findMaxLength(int[] nums) {
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            int zeros = 0, ones = 0;
            for (int j = i; j < nums.length; j++) {
                if (nums[j] == 0) {
                    zeros++;
                } else {
                    ones++;
                }
                if (zeros == ones) {
                    count = Math.max(count, j - i + 1);
                }
            }
        }
        return count;
    }
}
```



Optimized using HashMap,   TC = O(N)

https://www.youtube.com/watch?v=1WugaISSWx8

```
class Solution {
    public int findMaxLength(int[] nums) {
        HashMap <Integer, Integer> SumIndex =  new HashMap<>();
        int sum =0 ;
        int ans = 0;

        SumIndex.put(0,-1); //initially sum 0 at index -1

        for(int i = 0 ; i < nums.length ; i++){
            if(nums[i] == 0) sum += -1;
            else if(nums[i] == 1) sum += 1;

            if(SumIndex.containsKey(sum)){
                int idx = SumIndex.get(sum);
                int len = i - idx;
                if(len > ans) ans = len;
            }

            else SumIndex.put(sum,i);
        }
        return ans;
    }
}
```

https://leetcode.com/problems/continuous-subarray-sum/description/

https://www.youtube.com/watch?v=iQGK-ttaU50

TC =O(N)
SC =O(min(n, k))

```
class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        
        HashMap<Integer, Integer> map = new HashMap<>();
        int prefixSum = 0;
        map.put(0,-1);

        for(int i = 0 ; i < nums.length ; i++){
            prefixSum += nums[i];
            if(map.containsKey(prefixSum % k))
            {
                 //edge case for 
                if(i - map.get(prefixSum % k) >1)  //if nums = [0] & k = 1
                 return true;
            }
            
            else map.put((prefixSum % k) , i);
        }
    return false;
    }
}
```





The space complexity of the given solution is O(min(n, k)), where:

- n is the length of the input array nums
- k is the modulus base
### 🔍 Here's why:

- The HashMap<Integer, Integer> map stores at most one entry per distinct prefixSum % k.
- The number of possible values of prefixSum % k is at most k (from 0 to k-1), so in the worst case, the map holds up to k entries.
- But if k > n, then the number of entries is bounded by n.
### 



https://leetcode.com/problems/maximum-subarray/submissions/1659112629/

###  maximum Sum Subarray  

TC =O(N)

```
public class KadaneAlgorithm {
    public int maxSubArray(int[] nums) {
        int currentSum = nums[0]; // Start with the first element
        int maxSum = nums[0];     // Initialize maxSum with the first element

        // Traverse the array from the second element
        for (int i = 1; i < nums.length; i++) {
            // If currentSum is negative, reset to current element
            currentSum = Math.max(nums[i], currentSum + nums[i]);
            // Update maxSum if currentSum is greater
            maxSum = Math.max(maxSum, currentSum);
        }
        return maxSum;
    }    
}
```




### max product subarray 

TC =O(N)

SC = O(1)

```
class Solution {
    public int maxProduct(int[] nums) {
        int currentMax = nums[0];
         int currentMin = nums[0];
        int maxProd =nums[0];

        for(int i = 1 ; i< nums.length; i++){

            int temp = currentMax;
            currentMax = Math.max(nums[i], Math.max(currentMin*nums[i] , currentMax*nums[i]));
            currentMin = Math.min(nums[i], Math.min(temp*nums[i] , currentMin*nums[i]));
            maxProd =  Math.max(currentMax ,maxProd);
        }
        return maxProd ;
    }
}
```













### ✅Linked List

### ⭐Dummy pointer Strategy

Visualization of this solution:

Case 1 (Have Intersection & Same Len):

```
       a
A:     a1 → a2 → a3
                   ↘
                     c1 → c2 → c3 → null
                   ↗
B:     b1 → b2 → b3
       b
```

```
            a
A:     a1 → a2 → a3
                   ↘
                     c1 → c2 → c3 → null
                   ↗
B:     b1 → b2 → b3
            b
```

```
                 a
A:     a1 → a2 → a3
                   ↘
                     c1 → c2 → c3 → null
                   ↗
B:     b1 → b2 → b3
                 b
```

```
A:     a1 → a2 → a3
                   ↘ a
                     c1 → c2 → c3 → null
                   ↗ b
B:     b1 → b2 → b3
```

Since a == b is true, end loop while(a != b), return the intersection node a = c1.

Case 2 (Have Intersection & Different Len):

```
            a
A:          a1 → a2
                   ↘
                     c1 → c2 → c3 → null
                   ↗
B:     b1 → b2 → b3
       b
```

```
                 a
A:          a1 → a2
                   ↘
                     c1 → c2 → c3 → null
                   ↗
B:     b1 → b2 → b3
            b
```

```
A:          a1 → a2
                   ↘ a
                     c1 → c2 → c3 → null
                   ↗
B:     b1 → b2 → b3
                 b
```

```
A:          a1 → a2
                   ↘      a
                     c1 → c2 → c3 → null
                   ↗ b
B:     b1 → b2 → b3
```

```
A:          a1 → a2
                   ↘           a
                     c1 → c2 → c3 → null
                   ↗      b
B:     b1 → b2 → b3
```

```
A:          a1 → a2
                   ↘                a = null, then a = b1
                     c1 → c2 → c3 → null
                   ↗           b
B:     b1 → b2 → b3
```

```
A:          a1 → a2
                   ↘
                     c1 → c2 → c3 → null
                   ↗                b = null, then b = a1
B:     b1 → b2 → b3
       a
```

```
            b
A:          a1 → a2
                   ↘
                     c1 → c2 → c3 → null
                   ↗
B:     b1 → b2 → b3
            a
```

```
                 b
A:          a1 → a2
                   ↘
                     c1 → c2 → c3 → null
                   ↗
B:     b1 → b2 → b3
                 a
```

```
A:          a1 → a2
                   ↘ b
                     c1 → c2 → c3 → null
                   ↗ a
B:     b1 → b2 → b3
```

Since a == b is true, end loop while(a != b), return the intersection node a = c1.

Case 3 (Have No Intersection & Same Len):

```
       a
A:     a1 → a2 → a3 → null
B:     b1 → b2 → b3 → null
       b
```

```
            a
A:     a1 → a2 → a3 → null
B:     b1 → b2 → b3 → null
            b
```

```
                 a
A:     a1 → a2 → a3 → null
B:     b1 → b2 → b3 → null
                 b
```

```
                      a = null
A:     a1 → a2 → a3 → null
B:     b1 → b2 → b3 → null
                      b = null
```

Since a == b is true (both refer to null), end loop while(a != b), return a = null.

Case 4 (Have No Intersection & Different Len):

```
       a
A:     a1 → a2 → a3 → a4 → null
B:     b1 → b2 → b3 → null
       b
```

```
            a
A:     a1 → a2 → a3 → a4 → null
B:     b1 → b2 → b3 → null
            b
```

```
                 a
A:     a1 → a2 → a3 → a4 → null
B:     b1 → b2 → b3 → null
                 b
```

```
                      a
A:     a1 → a2 → a3 → a4 → null
B:     b1 → b2 → b3 → null
                      b = null, then b = a1
```

```
       b                   a = null, then a = b1
A:     a1 → a2 → a3 → a4 → null
B:     b1 → b2 → b3 → null
```

```
            b
A:     a1 → a2 → a3 → a4 → null
B:     b1 → b2 → b3 → null
       a
```

```
                 b
A:     a1 → a2 → a3 → a4 → null
B:     b1 → b2 → b3 → null
            a
```

```
                      b
A:     a1 → a2 → a3 → a4 → null
B:     b1 → b2 → b3 → null
                 a
```

                           b = null
A:     a1 → a2 → a3 → a4 → null
B:     b1 → b2 → b3 → null
                      a = null



https://leetcode.com/problems/intersection-of-two-linked-lists/solutions/49785/java-solution-without-knowing-the-difference-in-len/comments/165648/

```
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if(headA == null | headB ==null) return null;
        ListNode a = headA;
        ListNode b = headB;

        while (a!=b){
            if(a == null) a = headB;
            else a = a.next;
        // same meaning what written above
            b = b == null? headA : b.next;
        }
        return a; // or b
    }
}
```

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

```
//Using Left and right pointer 
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode rp= head ,lp = head;
        if(rp.next == null && n ==1){
            return null;
        }

        int count = 0;
        while(rp != null){
            //starting lp when rp reaches end . 
            //so lp will reach to the node prev to the node that has to be remove
            if(count>n) lp= lp.next;
            rp = rp.next;
            count++;
        }
        //linkedlist has N node and n = N 
        //=> removing head
         if(n == count) return head. next;

         //lp reaches to node prev to the node that has to be remove
        lp.next = lp.next.next;
        return head;
    }
   
}
```

You are not creating a copy of the node, you're creating another reference to the same object in memory.

Both lp and head now point to the same node in the linked list.

You're mutating the object that both lp and head refer to. So the change is visible in head too, because they point to the same underlying object.



https://leetcode.com/problems/swap-nodes-in-pairs/description/

https://www.youtube.com/watch?v=M9lsf_ySE9s

- Time
O(n)

- Space 
O(1)

```
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {

        //creating dummy node before head 
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode point = dummy;

        //ensuring nodes we are swapping are not null
        while (point.next != null && point.next.next != null){
        
        //idenetifying nodes to swap
        ListNode swap1 = point.next;
        ListNode swap2 = point.next.next;

        //actual swap
        swap1.next = swap2.next;
        swap2.next = swap1;

        point.next = swap2;
        point = swap1;   
        }
        
        return dummy.next;
    }
}
```



https://leetcode.com/problems/rotate-list/description/

- Time complexity:
O(n)  ==O(2n)

We traverse the list twice: once to find the length and once to find the new tail. 

- Space complexity:
O(1)

```

class Solution {
    public ListNode rotateRight(ListNode head, int k) {

if (head == null || head.next == null || k == 0) return head;

        //Finding length of the list
        ListNode temp = head;
        int len = 1;
        while(temp.next != null){
            len++;
            temp = temp.next;
        }

        
       //Computing rotations
        k = k % len;
        if(k == 0) return head;

       // Making the list circular
        temp.next = head;

        //Finding new tail (length - k steps ahead)
         temp = temp.next; //at head
        for(int i = 0 ; i< len - k -1 ; i++){
            temp = temp.next;   
        }

        //: New head is after new tail
        head = temp.next;
        temp.next = null;

        return head;
    }
}
```

https://leetcode.com/problems/add-two-numbers/description/

O(N)  TIme

constant space

```
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
         while(l1 != null || l2 != null || carry != 0){
            int val1 = (l1 != null)? l1.val : 0;
            int val2 = (l2 != null)? l2.val : 0;
            
            int sum = val1 + val2 + carry;
            carry = (sum) / 10;

            // ⭐ to connect and update dummy.next
            curr.next = new ListNode(sum % 10);
            curr = curr.next;

            if(l1 != null) l1 = l1.next;
            if(l2 != null) l2 =l2.next;
         }
         return dummy.next;
    }
}
```







### ✅ Fast and Slow Pointer

https://leetcode.com/problems/linked-list-cycle/description/

O(N) ⇒ TC

O(1) ⇒ SC

```
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
  public boolean hasCycle(ListNode head) {
    ListNode slow = head;
    ListNode fast = head;

    while (fast != null && fast.next != null) {
      slow = slow.next;
      fast = fast.next.next;
      if (slow == fast)
        return true;
    }

    return false;
  }
}
```

getNext(n)  TC == O(log n)
 ..
 TC and SC = O(1)

```
class Solution {
    public boolean isHappy(int n) {
        int slow = n;
        int fast = getNext(n);
        while(fast != 1 && slow != fast){
            slow =getNext(slow);
            fast = getNext(getNext(fast));
            if (fast != 1 && slow == fast)  return false;
        } 
     return true;
    }

     public int getNext(int n){
            int sum = 0;
            while (n>0){
                int digit = n % 10;
                sum += digit * digit;
                n = n/10;
            }
        return sum;
        }
}
```

https://leetcode.com/problems/linked-list-cycle-ii/description/

- Time Complexity :- BigO(N)
- Space Complexity :- BigO(1)
```
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                while (slow != head) {
                    slow = slow.next;
                    head = head.next;
                }
                return slow;
            }
        }
        return null;
    }
}
```

Since fast is 2x faster than slow pointer, we have the equation

2(x_1 + x_2) = x_1 + x_2 + x_3 + x_2



Therefore x_1 = x_3, which means (# of steps of head to cycle start) == (# of steps where fast and slow meet to cycle start).

finding duplicates with constant space , without modifying array


```
class Solution {
    public int findDuplicate(int[] nums) {

        int slow = nums[0];
        int fast = nums[0];
        //do while is must .. socho !!!!!!!!!!
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        
        if (slow == fast) {
            fast = nums[0];
            while (slow != fast) {
                slow = nums[slow];
                fast = nums[fast];
            }
        }
        return slow;
    }
}
```

### 🧠 Pigeonhole Principle:

In our case, that means:

- At least one value appears more than once → it creates a cycle when modeled as pointers


### ✅ In - Place Reversal in LL

O(N) time    O(1) space

```
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        

      while (curr != null){
     ListNode next = curr.next;
      curr.next = prev;
      prev = curr;
      curr = next;
      }
    return prev;
    }
}
```



https://leetcode.com/problems/reverse-nodes-in-k-group/

```
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        // Step 1: Check if we have k nodes to reverse
        ListNode node = head;
        int count = 0;
        while (node != null && count < k) {
            node = node.next;
            count++;
        }

        // If fewer than k nodes, return head as is
        if (count < k) {
            return head;
        }

        // Step 2: Reverse k nodes
        ListNode prev = null, curr = head, next = null;
        int i = 0;
        while (i < k) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
            i++;
        }

        // Step 3: Recurse on the rest
        head.next = reverseKGroup(curr, k);

        // prev is the new head of the reversed group
        return prev;
    }
}

```



curr = null ( node just after prev)





## 📚LINKED LIST PATTERNS 

### 1. 🔁 Fast & Slow Pointer

Use Case: Middle element, Cycle detection, Palindrome check

### 🚀 Find Middle of LinkedList

```
ListNode slow = head, fast = head;
while (fast != null && fast.next != null) {
    slow = slow.next;
    fast = fast.next.next;
}
return slow; // Middle node
```

### 🔄 Detect Cycle

```
public boolean hasCycle(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) return true;
    }
    return false;
}
```

### 2. 🔄 In-Place Reversal (Reverse Linked List)

✅ Reverse Entire Linked List

```
public ListNode reverseList(ListNode head) {
    ListNode prev = null;
    while (head != null) {
        ListNode next = head.next;
        head.next = prev;
        prev = head;
        head = next;
    }
    return prev;
```

✅5. Reverse in K-Groups

```
public ListNode reverseKGroup(ListNode head, int k) {
    ListNode curr = head;
    int count = 0;
    while (curr != null && count < k) {
        curr = curr.next;
        count++;
    }
    if (count == k) {
        curr = reverseKGroup(curr, k);
        while (count-- > 0) {
            ListNode tmp = head.next;
            head.next = curr;
            curr = head;
            head = tmp;
        }
        head = curr;
    }
    return head;
}
```

### 3. 🧩 Merge Two Sorted Lists

```

public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    ListNode dummy = new ListNode(0);
    ListNode tail = dummy;
    while (l1 != null && l2 != null) {
        if (l1.val < l2.val) {
            tail.next = l1;
            l1 = l1.next;
        } else {
            tail.next = l2;
            l2 = l2.next;
        }
        tail = tail.next;
    }
    tail.next = (l1 != null) ? l1 : l2;
    return dummy.next;
}
```

### 4. 🔁 Detect & Remove Loop

```
public void removeLoop(ListNode head) {
    ListNode slow = head, fast = head;
    boolean hasLoop = false;

    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) {
            hasLoop = true;
            break;
        }
    }

    if (hasLoop) {
        slow = head;
        while (slow.next != fast.next) {
            slow = slow.next;
            fast = fast.next;
        }
        fast.next = null; // Remove loop
    }

```

### 5. 🔁 Palindrome Linked List (Using Reverse Half)

```
public boolean isPalindrome(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }

    // Reverse second half
    ListNode prev = null;
    while (slow != null) {
        ListNode next = slow.next;
        slow.next = prev;
        prev = slow;
        slow = next;
    }

    // Compare both halves
    ListNode left = head, right = prev;
    while (right != null) {
        if (left.val != right.val) return false;
        left = left.next;
        right = right.next;
    }
    return true;
}
```

## 📋 4. COMMON LINKED LIST QUESTIONS ON LEETCODE

## 🔖 5. LinkedList Template Snippets

### Create and Print

```

LinkedList<Integer> list = new LinkedList<>();
list.add(10);
list.addFirst(5);
list.addLast(15);
System.out.println(list); // [5, 10, 15]
```

### Traverse Custom LinkedList

```
void printList(ListNode head) {
    while (head != null) {
        System.out.print(head.val + " ");
        head = head.next;
    }
}
```

## 🔄 6. CIRCULAR LINKED LIST CHECK

```
public boolean isCircular(ListNode head) {
    if (head == null) return true;
    ListNode node = head.next;
    while (node != null && node != head) {
        node = node.next;
    }
    return (node == head);
}
```

## ✅ 7. Remove N-th Node from End

```

public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    ListNode first = dummy, second = dummy;
    for (int i = 0; i <= n; i++) first = first.next;
    while (first != null) {
        first = first.next;
        second = second.next;
    }
    second.next = second.next.next;
    return dummy.next;
}
```



```
### 🔸 Adding Elements

- `add(E e)` — append to end
- `add(int index, E e)`
- `addFirst(E e)`
- `addLast(E e)`
- `offer(E e)` — add to tail
- `offerFirst(E e)`
- `offerLast(E e)`

### 🔸 Removing Elements

- `remove()` — remove first
- `remove(int index)`
- `remove(Object o)`
- `removeFirst()`, `removeLast()`
- `poll()`, `pollFirst()`, `pollLast()`
- `pop()` — stack-style
- `removeFirstOccurrence(Object o)`
- `removeLastOccurrence(Object o)`

### 🔸 Access Elements

- `get(int index)`
- `getFirst()`, `getLast()`
- `peek()`, `peekFirst()`, `peekLast()`

### 🔸 Utility

- `contains(Object o)`
- `indexOf(Object o)`
- `lastIndexOf(Object o)`
- `size()`, `clear()`, `clone()`
- `toArray()`, `toArray(T[] a)`
- `toString()`
- `descendingIterator()`
- `spliterator()`
```



```
// ====================== 🔵 Insertion ======================

// Insert at the beginning or end
ll.addFirst(e);                         // Deque: insert at head
ll.addLast(e);                          // Deque: insert at tail

// Add to end or at a specific index
ll.add(e);                              // List: add at end
ll.add(index, e);                       // List: add at specified index

// Offer at front or back (returns true/false)
ll.offerFirst(e);                       // Deque: offer at head
ll.offerLast(e);                        // Deque: offer at tail

// Queue-style and stack-style insertion
ll.offer(e);                            // Queue/Deque: offer at end
ll.push(e);                             // Stack (Deque): push at head

// Insert an entire collection
ll.addAll(collection);                 // List: add all at end
ll.addAll(index, collection);          // List: insert all at specific index

// ====================== 🔴 Deletion ======================

// Remove and return head or tail (throws if empty)
ll.removeFirst();                       // Deque: remove head
ll.removeLast();                        // Deque: remove tail

// Safe remove head/tail, returns null if empty
ll.pollFirst();                         // Deque: poll head
ll.pollLast();                          // Deque: poll tail

// Remove head element
ll.remove();                            // Queue: remove head (throws)
ll.poll();                              // Queue: poll head (null-safe)

// Stack-style pop and clear all
ll.pop();                               // Deque: remove head (LIFO)
ll.clear();                             // Collection: remove all elements

// Remove by index or object
ll.remove(index);                       // List: remove at index
ll.remove(obj);                         // List: remove by value

// Remove first or last occurrence of object
ll.removeFirstOccurrence(obj);          // Deque: remove first match
ll.removeLastOccurrence(obj);           // Deque: remove last match

// ====================== 🟢 Access / Retrieve ======================

// Get head or tail (throws if empty)
ll.getFirst();                          // Deque: get head
ll.getLast();                           // Deque: get tail

// Peek head or tail (null-safe)
ll.peekFirst();                         // Deque: peek head
ll.peekLast();                          // Deque: peek tail

// Get or set value by index
ll.get(index);                          // List: access at index
ll.set(index, e);                       // List: update at index

// Peek head element (null-safe or exception)
ll.peek();                              // Queue: peek head (null-safe)
ll.element();                           // Queue: get head (throws if empty)

// ====================== 🟠 Search / Info ======================

// Search and presence
ll.contains(obj);                       // Collection: check existence
ll.indexOf(obj);                        // List: first index of element

// Last index and size
ll.lastIndexOf(obj);                    // List: last index of element
ll.size();                              // Collection: total element count

// Convert to array
Object[] arr1 = ll.toArray();           // Collection: Object[]
String[] arr2 = ll.toArray(new String[0]); // Collection: typed array

// Object utilities
LinkedList<T> copy = (LinkedList<T>) ll.clone(); // Shallow copy
String repr = ll.toString();           // List contents as string

// Iterators
Spliterator<T> sp = ll.spliterator();   // Stream-style iterator
ListIterator<T> li = ll.listIterator(index); // Indexed bi-directional iterator
Iterator<T> rev = ll.descendingIterator();    // Reverse-order iterator (Deque)

```



```
// ====================== 🟩 1. Common LinkedList Utility Methods ======================

Collections.sort(ll);                          // Sorts list in ascending order
Collections.reverse(ll);                       // Reverses list order
Collections.shuffle(ll);                       // Randomly shuffles elements
Collections.swap(ll, 0, 1);                    // Swaps elements at index 0 and 1
int max = Collections.max(ll);                 // Returns the maximum element
int min = Collections.min(ll);                 // Returns the minimum element
int freq = Collections.frequency(ll, "a");     // Counts frequency of "a" in the list
Collections.replaceAll(ll, "a", "b");          // Replaces all "a" with "b"
List<Integer> unmod = Collections.unmodifiableList(ll);  // Creates a read-only view


// ====================== 🟨 2. Conversion Utilities ======================

List<Integer> ll = new LinkedList<>(Arrays.asList(arr));   // Convert Array to LinkedList
Integer[] arr = ll.toArray(new Integer[0]);            // Convert LinkedList to Array
Set<Integer> set = new HashSet<>(ll);   // Convert LinkedList to Set (removes duplicates)


// ====================== 🟥 3. Other Useful Utility Ideas ======================

LinkedList<T> copy = new LinkedList<>(original);    // Deep copy of LinkedList
Iterator<T> it = ll.descendingIterator();           // Reverse iterator from tail to head
ll.sort((a, b) -> b - a);                          // Custom sort: descending order

Map<T, Long> freqMap = ll.stream()
.collect(Collectors.groupingBy(e -> e, Collectors.counting()));
// Frequency map of elements


Interface	Description
List	 // Indexed, ordered access (get/set)
Deque //	Double-ended queue (stack/queue both)
Queue	//FIFO-based operations
Collection	//Root interface for most collections
Object	//Inherited from base class (toString, clone)
```

### 📌 1. Core Java Stack and Queue Classes

### ✅ Stack

```
java
CopyEdit
Stack<Integer> stack = new Stack<>();
stack.push(1);         // insert
int val = stack.pop(); // remove and return top
int peek = stack.peek(); // view top
boolean empty = stack.isEmpty();


```

### ✅ Queue (via LinkedList)

```
java
CopyEdit
Queue<Integer> queue = new LinkedList<>();
queue.offer(1);        // insert
int val = queue.poll(); // remove and return front
int peek = queue.peek(); // view front
boolean empty = queue.isEmpty();


```

### 🧱 2. Boilerplate Templates

### 🔁 Iterate over a Stack

```
java
CopyEdit
for (int val : stack) {
    // use val
}


```

### 🔁 Iterate over a Queue

```
java
CopyEdit
while (!queue.isEmpty()) {
    int current = queue.poll();
}


```

### 🧩 3. Stack Patterns

### ✅ Valid Parentheses / Balanced Brackets

```
java
CopyEdit
Stack<Character> stack = new Stack<>();
for (char c : s.toCharArray()) {
    if (c == '(' || c == '{' || c == '[') {
        stack.push(c);
    } else {
        if (stack.isEmpty()) return false;
        char top = stack.pop();
        if (!isMatching(top, c)) return false;
    }
}
return stack.isEmpty();


```

### ✅ Monotonic Stack

Used in: Next Greater Element, Largest Rectangle in Histogram

```
java
CopyEdit
Stack<Integer> stack = new Stack<>();
for (int i = 0; i < nums.length; i++) {
    while (!stack.isEmpty() && nums[stack.peek()] < nums[i]) {
        int prevIndex = stack.pop();
        // nums[prevIndex] has next greater element nums[i]
    }
    stack.push(i);
}


```

### 🧩 4. Queue Patterns

### ✅ BFS (Level Order Traversal)

```
java
CopyEdit
Queue<TreeNode> queue = new LinkedList<>();
queue.offer(root);
while (!queue.isEmpty()) {
    int size = queue.size();
    for (int i = 0; i < size; i++) {
        TreeNode node = queue.poll();
        if (node.left != null) queue.offer(node.left);
        if (node.right != null) queue.offer(node.right);
    }
}


```

### ✅ Sliding Window Maximum (Deque)

```

Deque<Integer> deque = new ArrayDeque<>();
for (int i = 0; i < nums.length; i++) {
    if (!deque.isEmpty() && deque.peekFirst() < i - k + 1)
        deque.pollFirst(); // remove out of window
    while (!deque.isEmpty() && nums[deque.peekLast()] < nums[i])
        deque.pollLast(); // remove smaller elements
    deque.offerLast(i);
    if (i >= k - 1) result[i - k + 1] = nums[deque.peekFirst()];
}


```

### 🛠️ 5. Custom Stack/Queue 

## 📦 Stack Using Array

```
java
CopyEdit
class MyStack {
    int[] arr;
    int top = -1;

    public MyStack(int size) {
        arr = new int[size];
    }

    public void push(int x) {
        arr[++top] = x;
    }

    public int pop() {
        return arr[top--];
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public int peek() {
        return arr[top];
    }
}


```

🕒 Time: O(1) for push, pop, peek

## 📦 Queue Using Array (Linear)

```
java
CopyEdit
class MyQueue {
    int[] arr;
    int front = 0, rear = 0, size = 0, capacity;

    public MyQueue(int k) {
        capacity = k;
        arr = new int[k];
    }

    public boolean enqueue(int x) {
        if (size == capacity) return false;
        arr[rear++] = x;
        size++;
        return true;
    }

    public int dequeue() {
        if (size == 0) return -1;
        int val = arr[front++];
        size--;
        return val;
    }

    public int peek() {
        return size == 0 ? -1 : arr[front];
    }

    public boolean isEmpty() {
        return size == 0;
    }
}


```

🕒 Time: O(1) for all ops (with caveats on shifting if not circular)

## 🔄 Queue Using Array (Circular Queue)

```
java
CopyEdit
class Queue {
    int[] arr;
    int front, rear, size, capacity;

    Queue(int k) {
        arr = new int[k];
        front = 0;
        rear = 0;
        size = 0;
        capacity = k;
    }

    boolean push(int x) {
        if (size == capacity) return false;
        arr[rear] = x;
        rear = (rear + 1) % capacity;
        size++;
        return true;
    }

    int pop() {
        if (size == 0) return -1;
        int val = arr[front];
        front = (front + 1) % capacity;
        size--;
        return val;
    }

    int peek() {
        if (size == 0) return -1;
        return arr[front];
    }

    boolean isEmpty() {
        return size == 0;
    }

    boolean isFull() {
        return size == capacity;
    }
}


```

🧠 % capacity wraps the pointer to simulate circular behavior

🕒 Time: O(1) for all ops

## 🪜 Stack Using Linked List

```
java
CopyEdit
class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
    }
}

class Stack {
    Node head;

    Stack() {
        head = null;
    }

    void push(int x) {
        Node temp = new Node(x);
        temp.next = head;
        head = temp;
    }

    int pop() {
        if (head == null) return -1;
        int val = head.data;
        head = head.next;
        return val;
    }

    int top() {
        if (head == null) return -1;
        return head.data;
    }

    boolean isEmpty() {
        return head == null;
    }
}


```

🕒 Time: O(1) for all ops

## 🪜 Queue Using Linked List

```
java
CopyEdit
class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
    }
}

class Queue {
    Node front, rear;

    Queue() {
        front = rear = null;
    }

    void push(int x) {
        Node temp = new Node(x);
        if (rear == null) {
            front = rear = temp;
            return;
        }
        rear.next = temp;
        rear = temp;
    }

    int pop() {
        if (front == null) return -1;
        int val = front.data;
        front = front.next;
        if (front == null) rear = null;
        return val;
    }

    int peek() {
        if (front == null) return -1;
        return front.data;
    }

    boolean isEmpty() {
        return front == null;
    }
}


```

🕒 Time: O(1) for all ops

## 🔁 Stack Using Two Queues (Push Costly)

```
java
CopyEdit
class MyStack {
    Queue<Integer> q1 = new LinkedList<>();
    Queue<Integer> q2 = new LinkedList<>();

    void push(int x) {
        q2.add(x);
        while (!q1.isEmpty()) q2.add(q1.remove());
        Queue<Integer> tmp = q1;
        q1 = q2;
        q2 = tmp;
    }

    int pop() { return q1.isEmpty() ? -1 : q1.remove(); }
    int top() { return q1.isEmpty() ? -1 : q1.peek(); }
    boolean isEmpty() { return q1.isEmpty(); }
}


```

🕒 push: O(n), pop/top: O(1)

## 🔁 Stack Using Two Queues (Pop Costly)

```
java
CopyEdit
class MyStack {
    Queue<Integer> q1 = new LinkedList<>();
    Queue<Integer> q2 = new LinkedList<>();

    void push(int x) {
        q1.add(x);
    }

    int pop() {
        if (q1.isEmpty()) return -1;
        while (q1.size() > 1) q2.add(q1.remove());
        int res = q1.remove();
        q1 = q2;
        q2 = new LinkedList<>();
        return res;
    }

    int top() {
        if (q1.isEmpty()) return -1;
        while (q1.size() > 1) q2.add(q1.remove());
        int res = q1.remove();
        q2.add(res);
        q1 = q2;
        q2 = new LinkedList<>();
        return res;
    }

    boolean isEmpty() {
        return q1.isEmpty();
    }
}


```

🕒 push: O(1), pop/top: O(n)

## 🧲 Stack Using Single Queue (Striver Optimized)

```
java
CopyEdit
class MyStack {
    Queue<Integer> q = new LinkedList<>();

    void push(int x) {
        q.add(x);
        int sz = q.size();
        for (int i = 0; i < sz - 1; i++) {
            q.add(q.remove());
        }
    }

    int pop() {
        return q.isEmpty() ? -1 : q.remove();
    }

    int top() {
        return q.isEmpty() ? -1 : q.peek();
    }

    boolean isEmpty() {
        return q.isEmpty();
    }
}


```

🕒 push: O(n), pop/top: O(1)

## 🔁 Queue Using Two Stacks (Push Efficient)

```
java
CopyEdit
class Queue {
    Stack<Integer> input = new Stack<>();
    Stack<Integer> output = new Stack<>();

    void push(int x) {
        input.push(x);
    }

    int pop() {
        if (output.isEmpty()) {
            while (!input.isEmpty()) output.push(input.pop());
        }
        return output.isEmpty() ? -1 : output.pop();
    }

    int peek() {
        if (output.isEmpty()) {
            while (!input.isEmpty()) output.push(input.pop());
        }
        return output.isEmpty() ? -1 : output.peek();
    }

    boolean isEmpty() {
        return input.isEmpty() && output.isEmpty();
    }
}


```

🕒 push: O(1), pop/peek: Amortized O(1)

## 🔁 Queue Using Two Stacks (Pop Efficient)

```
java
CopyEdit
class Queue {
    Stack<Integer> s1 = new Stack<>();
    Stack<Integer> s2 = new Stack<>();

    void push(int x) {
        while (!s1.isEmpty()) s2.push(s1.pop());
        s1.push(x);
        while (!s2.isEmpty()) s1.push(s2.pop());
    }

    int pop() {
        return s1.isEmpty() ? -1 : s1.pop();
    }

    int peek() {
        return s1.isEmpty() ? -1 : s1.peek();
    }

    boolean isEmpty() {
        return s1.isEmpty();
    }
}


```

🕒 push: O(n), pop/peek: O(1)

## 🌀 Queue Using Single Stack (Recursive)

```
java
CopyEdit
class Queue {
    Stack<Integer> st = new Stack<>();

    void push(int x) {
        st.push(x);
    }

    int pop() {
        if (st.isEmpty()) return -1;
        int x = st.pop();
        if (st.isEmpty()) return x;
        int res = pop();
        st.push(x);
        return res;
    }

    int peek() {
        if (st.isEmpty()) return -1;
        int x = st.pop();
        if (st.isEmpty()) {
            st.push(x);
            return x;
        }
        int res = peek();
        st.push(x);
        return res;
    }

    boolean isEmpty() {
        return st.isEmpty();
    }
}


```

🕒 push: O(1), pop/peek: O(n) via recursion

## ✅ Stack

https://leetcode.com/problems/valid-parentheses/description/

- Time  / Space : O(n)
```
class Solution {
    public boolean isValid(String s) {
        // Stack to keep track of opening brackets
        Stack<Character> st = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            // If it's an opening bracket, push to stack
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            }
            // If it's a closing bracket
            else if (c == ')' || c == '}' || c == ']') {
                // If stack is empty, there's no matching opening bracket
                if (st.isEmpty()) return false;
                // Pop the top element and check if it matches the closing bracket
                char top = st.pop();
                if (
                    (c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')
                ) return false; // Mismatched bracket
            }
        }
        // If stack is empty, all brackets matched; otherwise, some were unmatched
        return st.isEmpty();
    }
}
```

https://leetcode.com/problems/min-stack/

```
class MinStack {
    class Pair{
        int x, y;
        // Constructor
        Pair(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
    // Declaration
    Stack<Pair> stk;
    public MinStack() {
        stk = new Stack<>(); // Initialization
    }
    
    public void push(int val) {
        int min;
        if(stk.isEmpty()){
            min = val;
        }
        else {
            min = Math.min(val, stk.peek().y);
        }
        stk.push(new Pair(val, min));
    }
    
    public void pop() {
        stk.pop();
    }
    
    public int top() {
        return stk.peek().x;
    }
    
    public int getMin() {
        return stk.peek().y;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
```

https://www.youtube.com/watch?v=rU5p0MRm5zU

```

//Using string as a stack
//T.C : O(n) - We visit each character only once (Note that an element once popped from result is never put back)
//S.C : O(1)
public class Solution {
    public String removeDuplicateLetters(String s) {
        int n = s.length();
        StringBuilder result = new StringBuilder();
        
        boolean[] taken = new boolean[26];
        int[] lastIndex = new int[26];
        Arrays.fill(lastIndex, -1);
        
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            lastIndex[ch - 'a'] = i;
        }
        
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            int idx = ch - 'a';
            
            if (taken[idx]) continue;
            
            while (result.length() > 0 && ch < result.charAt(result.length() - 1) && lastIndex[result.charAt(result.length() - 1) - 'a'] > i) {
                taken[result.charAt(result.length() - 1) - 'a'] = false;
                result.deleteCharAt(result.length() - 1);
            }
            
            result.append(ch);
            taken[idx] = true;
        }
        
        return result.toString();
    }
}


//Approach-2 (Using stack)
//T.C : O(n) - We visit each character only once (Note that an element once popped from result is never put back)
//S.C : O(n) stack
public class Solution {
    public String removeDuplicateLetters(String s) {
        int n = s.length();
        Stack<Character> st = new Stack<>();
        
        boolean[] taken = new boolean[26];
        int[] lastIndex = new int[26];
        
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            lastIndex[ch - 'a'] = i;
        }
        
        for (int i = 0; i < n; i++) {
            int idx = s.charAt(i) - 'a';
            
            if (taken[idx]) continue;
            
            while (!st.isEmpty() && s.charAt(i) < st.peek() && lastIndex[st.peek() - 'a'] > i) {
                taken[st.pop() - 'a'] = false;
            }
            
            st.push(s.charAt(i));
            taken[idx] = true;
        }
        
        StringBuilder result = new StringBuilder();
        while (!st.isEmpty()) {
            result.append(st.pop());
        }
        
        return result.reverse().toString();
    }
}
```

https://leetcode.com/problems/longest-valid-parentheses/solutions/6830763/easy-to-understand-simple-solution-using-stack/

- Time complexity: O(n)
- Space complexity: O(n)
```
class Solution {
    public int longestValidParentheses(String s) {
        int max =  0;
        Stack <Integer> st = new Stack <>();

        st.push(-1);
        for(int i= 0 ; i < s.length() ; i++){

            if(s.charAt(i) == '(') st.push(i);

            else{
                st.pop(); 

                if(st.isEmpty()) st.push(i);
                else max = Math.max(max, i - st.peek());

            }
        }
        return max;
    }
}
```





## ✅ Monotonic Stack

 → Next Greater / Smaller

 → Previous Greater / Smaller  

 → Array related , Time O(n²)  → O(n)

 → Better To Store indices of Array

### Monotonic Increasing

increasing matlab jab tak stack ka peek bada ho  tab tak pop



### Monotonic Decreasing

decreasing matlab jab tak stack ka peek chota ho  tab tak pop

## NGE 

https://www.youtube.com/watch?v=DtJVwbbicjQ

https://www.youtube.com/watch?v=1_Bbq5qOraY

3. Initialization:
- Creating the result array and filling it with -1: O(n)
3. Main Loop:
- The outer for-loop iterates through all n elements: O(n)
3. Inner While Loop:
- Every element is pushed exactly once: O(n) operations
- Every element is popped at most once: O(n) operations
- Total operations: 2×O(n) = O(n)
- The while loop might seem nested, but it's amortized O(1) per iteration of the main loop



- Direction: Left to right
- Comparison: Current > Stack top
- Stack: Decreasing monotonic stack
```
 // dry run --  2 1 5 6 2 3
  public int[] nextGreaterElement(int[] nums) {
        int n = nums.length;
        int[] result = new int[n]; // Output array
        Arrays.fill(result, -1); // Default to -1 if no greater element exists
        Stack<Integer> stack = new Stack<>(); // Stack stores indices

        // Iterate through the array
        for (int i = 0; i < n; i++) {
            // While stack is not empty and current element is greater than stack top
            while (!stack.isEmpty() && nums[i] > nums[stack.peek()]) {
                int index = stack.pop(); // Pop the top element
                result[index] = nums[i]; // The current element is the Next Greater Element
            }
            stack.push(i); // Push the current index onto the stack
        }
        return result;
    }
```

 

```
 public int[] previousGreaterElement(int[] nums) {
    int n = nums.length;
    int[] result = new int[n];
    Arrays.fill(result, -1);
    Stack<Integer> stack = new Stack<>();

    // Iterate from right to left ❌ NO! Still iterate from left to right
    for (int i = 0; i < n; i++) {
        // While current element is greater or equal to stack top
        while (!stack.isEmpty() && nums[i] >= nums[stack.peek()]) {
            stack.pop(); // Pop elements smaller than current
        }
        
        //🔴 If stack is not empty, the top has the previous greater element
        if (!stack.isEmpty()) {
            result[i] = nums[stack.peek()];
        }
        
        stack.push(i);
    }
    return result;
}
```

```
public int[] nextLesserElement(int[] nums) {
    int n = nums.length;
    int[] result = new int[n];
    Arrays.fill(result, -1);
    Stack<Integer> stack = new Stack<>();

    // Still iterate from left to right
    for (int i = 0; i < n; i++) {
        // Changed comparison: current < stack top
        while (!stack.isEmpty() && nums[i] < nums[stack.peek()]) {
            int index = stack.pop();
            result[index] = nums[i]; // Current element is the Next Lesser Element
        }
        stack.push(i);
    }
    return result;
}
```

```
public int[] previousLesserElement(int[] nums) {
    int n = nums.length;
    int[] result = new int[n];
    Arrays.fill(result, -1);
    Stack<Integer> stack = new Stack<>();

    // Still iterate from left to right
    for (int i = 0; i < n; i++) {
        // Pop all elements that are greater than or equal to current
        while (!stack.isEmpty() && nums[i] <= nums[stack.peek()]) {
            stack.pop();
        }
        
        // If stack is not empty, top has the Previous Lesser Element
        if (!stack.isEmpty()) {
            result[i] = nums[stack.peek()];
        }
        
        stack.push(i);
    }
    return result;
}
```



## Summary 

- For "next" problems (NGE, NLE): Update result for popped indices
- For "previous" problems (PGE, PLE): Update result for current index
https://leetcode.com/problems/daily-temperatures/description/

time  = O(n)

space = O(n) 

```
 public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] result = new int[n]; // Result array initialized with 0s
        Stack<Integer> stack = new Stack<>(); // Monotonic decreasing stack (stores indices)

        // Iterate through the temperature array
        for (int i = 0; i < n; i++) {
            // While stack is not empty AND the current temperature is warmer than the temperature at stack top
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                int prevIndex = stack.pop(); // Pop the previous day's index
                result[prevIndex] = i - prevIndex; // ⭐🔴 Calculate the wait time
            }
            
            stack.push(i); // Push current index onto the stack
        }

        return result; // Return the computed results
    }   
```

https://leetcode.com/problems/largest-rectangle-in-histogram/description/


bit slow — > ⏲️ Time = O(5N)

                     Space  = O(4N) =2 * O(2N)

Optimized 
⭐⭐TC = O(n) + O(n)      while loop + pushing in stack
SC = O(n)

```
class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack <Integer> st = new Stack <>();
        int maxArea = Integer.MIN_VALUE;
        int n = heights.length;
        for(int i = 0  ; i <= n ; i++ ){
            //nse , pse so increasing stack
            while ( !st.isEmpty() && ( i == n || heights[st.peek()] > heights[i])){
                int height = st.pop();
                int nse = i;
                int pse = st.isEmpty() ? -1 : st.peek();
                maxArea = Math.max(heights[height] * ( nse - pse -1), maxArea);
            }
            st.push(i);
        }
        return maxArea;
    }
}
```

If it reaches end,  no nse



## ✅ Queue

https://leetcode.com/problems/number-of-recent-calls/solutions/6892673/simplest-solution-using-java/

📌using Queue , Design

- Time :   O(1)                   Space :   O(1)
```
class RecentCounter {
    private Queue<Integer> queue;

    public RecentCounter() {
        queue = new LinkedList<>();
    }
    
    public int ping(int t) {
        queue.add(t);

        while(queue.peek() < (t-3000)) {
            queue.remove();
        }

        return queue.size();
    }
}
```



📌using Sliding Window

- Time : O(1) amortized
 it’s only O(N) total for N calls (so O(1) per call, amortized)

- Space : O(N)  — after N
 it’s only O(N) total for N calls (so O(1) per call, amortized)

```
class RecentCounter {
    List<Integer> list;
    int i;
    int j;

    public RecentCounter() {
        list = new ArrayList();
        i = 0;
        j = -1;
    }

    public int ping(int t) {
        list.add(t);
        j++;
        while (i < j && list.get(j) - 3000 > list.get(i)) {
            i++;
        }
        return j - i + 1;
    }
}
```

### Approach 1 w/o Queue

- Time: O(n Log n)     
{ sorting → (n Log n)    , while  —> for each i (of total n )require ( log n) to fill array }

- Space: O( n )  
auxi i.e. including result

```
class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        int i = 0; //deck
        int j = 0; //result
        int n = deck.length;
    
        int[] result = new int [n];
        boolean skip = false;
        Arrays.sort(deck);

        while(i<n){

            if ( result[j] == 0){ //kahli hai

                if(skip == false){
                    result[j] = deck[i];
                    i++;
                }

                skip = !skip;  //alternate skip
            }

            j = (j+1) % n;  
        }

    return result;
    }
}
```

🔹 Arrays:

- deck (input)
- result (same size as deck)
🔹 Indices:

- i — index in deck
- j — index in result
 Steps:

4. Sort the deck in ascending order.
4. Initialize result array as empty (all zeros or placeholders).
4. Alternate Filling:  place element from deck to result as 
4. while( j < n )
skip true / falseswitch on each pass > 

fill result if  false

(j + 1) % N

—- -example ——-

deck = [17,13,11,2,3,5,7]

deck = [2,3,5,7,11,13,17]   sorted

Fill result alternately, cycling 

[2, _, 3, _, 5, _, 7]

Then fill remaining blanks:

[2, _ , 3, 11 , 5 , _ , 7] 

[2, 13 , 3, 11 , 5 , _ , 7] 

[2, 13 , 3, 11 , 5 , 17 , 7]  

- till j   reaches end  ⇒ place deck elements into even position and leave odd position of result as blank (alternate filling)
-  index get reset to 0 as we are not doing  j ++ .. instead we are doing  ( j + 1 ) % n
- (leaving first)   putting remaining item of deck into the blank spaces such in alternate fashion 
eg:  leave the first blank then put into next blank and we are cycling the index 



- Time: O(n Log n)     sorting → (n Log n)  
- Space: O( n )            queue of size N
```
class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        Queue <Integer> queue = new LinkedList<>(); // contains index of deck
        Arrays.sort(deck); // nlogn
        int n =deck.length;
        int [] result = new int [n];
        for(int i = 0 ; i < n ; i++ ){
            queue.add(i); //pushing index of deck
        }

        for(int i = 0 ; i < n ; i++ ){
           int idx = queue.remove();
           result[idx] = deck[i];  //putting a elemt in result 
            //and then elemt after it send back to last of queue
           if(!queue.isEmpty()) queue.add(queue.remove());
        }
        return result;
    }
}
```



## ✅ Monotonic Queue

🔴youtube 

📌📌  Used with Sliding Window



1st Sliding window

2nd Montonic que + slid windw

monoto que + prefix sum

monoto que + dp

## Sliding Window Minimum / Maximum

of size K ——> first element of window deque.getFirst()will return Minimum / Maximum

Using Monotonic Increasing Deque

Time ⇒  O(2N) —> visiting two times , push & pop

```
class SlidingWindowMinimum {
    // Returns an array of minimums for each window of size k
    static int[] slidingWindowMin(int arr[], int k) {
        int n = arr.length;
        Deque<Integer> deque = new LinkedList<>();
        int[] result = new int[n - k + 1];
        int idx = 0;

        for (int i = 0; i < n; i++) {
            // Remove indices out of the current window
            while (!deque.isEmpty() && deque.getFirst() <= i - k) {
                deque.removeFirst();
            }
            // Remove from back while arr[deque.getLast()] > arr[i]
            while (!deque.isEmpty() && arr[deque.getLast()] > arr[i]) {
                deque.removeLast();
            }
            deque.addLast(i); // Store index

            // Add the minimum for this window to result
            if (i >= k - 1) {
                result[idx++] = arr[deque.getFirst()];
            }
        }
        return result;
    }
}
```

⭐Increasing Monotonic queue

```
class MonotonicIncreasingQueue {
    static Deque<Integer> increasing_monotonic_queue(int arr[]) {
        int n = arr.length;
        Deque<Integer> deque = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            // Remove from back while arr[deque.getLast()] > arr[i]
            while (!deque.isEmpty() && arr[deque.getLast()] > arr[i]) {
                deque.removeLast();
            }
            deque.addLast(i); // Store index
        }
        return deque;
    }
}
```



⭐Decreasing Monotonic queue

```
class MonotonicDecreasingQueue {
    // Stores indices, not values
    static Deque<Integer> decreasingMonotonicQueue(int[] arr) {
        int n = arr.length;
        Deque<Integer> deque = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            // Remove from back while arr[deque.getLast()] < arr[i]
            while (!deque.isEmpty() && arr[deque.getLast()] < arr[i]) {
                deque.removeLast();
            }
            deque.addLast(i);
        }
        return deque;
    }
}
```





h = height of tree  

n =  no of nodes

h= log n   


 where 'n' is the number of nodes in tree s and 'm' is the number of nodes in tree t
    • time = O(m*n)    • space = O(n) 

maximum depth of the call stack is limited by the height of s

```
public class Solution {
    public boolean isSubtree(TreeNode s, TreeNode t) {
        if (s == null) return false;
        if (isSame(s, t)) return true;
        return isSubtree(s.left, t) || isSubtree(s.right, t);
    }
    
    private boolean isSame(TreeNode s, TreeNode t) {
        if (s == null && t == null) return true;
        if (s == null || t == null) return false;
        
        if (s.val != t.val) return false;
        
        return isSame(s.left, t.left) && isSame(s.right, t.right);
    }
}
```

## Level order

- Time: O(N)
- Space: O(N)
```
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();

        if (root == null) return result;
        queue.add(root); // <-- Add this line

        while (!queue.isEmpty()) {
            int n = queue.size();
            ArrayList<Integer> level = new ArrayList<>();

            for (int i = 0; i < n; i++) {
                TreeNode curr = queue.poll();
                level.add(curr.val);
                if (curr.left != null) queue.add(curr.left);
                if (curr.right != null) queue.add(curr.right);
            }
            result.add(level);
        }
        return result;
    }
}

/*
//Start with the root node in a queue.
While the queue isn’t empty:
Count how many nodes are at this level (queue size).
For each node at this level:
Take it out, save its value.
Add its children (if any) to the queue.
Save this level’s values to the result.
Repeat until all levels are processed.  */
```






### Approach 1 

- Time: O(N) — each node visited once.
- Space: O(N) — for the queue and result list.
```
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            int n = q.size(); // number of nodes at current level
            for (int i = 0; i < n; i++) {
                TreeNode curr = q.poll();
                // if this is the rightmost node at this level
                if (i == n - 1) result.add(curr.val);
                if (curr.left != null) q.add(curr.left);
                if (curr.right != null) q.add(curr.right);
            }
        }
        return result;
    }
}
```

- If tree is empty, return empty list.
- Start with root node in queue.
- While queue is not empty:
- Count how many nodes are on this level.
- Go through each node on this level:
- Save the value of the last node (rightmost) of this level.
- Add left and right children (if any) to queue.
- Return the list of rightmost values.


### Approach 2

```
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        q.add(null); // Level separator

        TreeNode last = null;

        while (!q.isEmpty()) {
            TreeNode curr = q.poll();

            if (curr == null) {
                if (last != null) {
                    result.add(last.val); // Add the rightmost node of this level
                }
                if (!q.isEmpty()) {
                    q.add(null); // More levels to process
                }
                last = null;
            } else {
                last = curr; // Update last as we go through the level
                if (curr.left != null) q.add(curr.left);
                if (curr.right != null) q.add(curr.right);
            }
        }
        return result;
    }
}
```

Best Approach —> In question it is asked to solve using constant space


- Space: O(1)    Time: O(N)
```
class Solution {
    public Node connect(Node root) {
        Node parent = root;

        while (parent != null) {
            Node child = null, childHead = null;
            Node curr = parent;

            while (curr != null) {
                // Handle left child
                if (curr.left != null) {
                    if (childHead == null) {
                        // First child found at this level
                        childHead = curr.left;
                    } else {
                        // Link previous child to this one
                        child.next = curr.left;
                    }
                    child = curr.left; // Move child pointer forward
                }
                // Handle right child
                if (curr.right != null) {
                    if (childHead == null) {
                        childHead = curr.right;
                    } else {
                        child.next = curr.right;
                    }
                    child = curr.right;
                }
                curr = curr.next; // Move to next node in current level
            }
            parent = childHead; // Go to next level
        }
        return root;
    }
}


/* dry run
    1
   / \
  2   3
 / \
4   5

 */
```



- Time: O(N)
- Space: O(N) 
```
class Solution {
    public Node connect(Node root) {
        if (root == null) return root;
                
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        
        while(!q.isEmpty()){
            int n = q.size();

            for(int i = 0 ; i < n ; i++){

                Node curr = q.poll();
                // if this is the rightmost node at this level
                if (i == n - 1) curr.next = null;
                else curr.next = q.peek();


                if (curr.left != null) q.add(curr.left);
                if (curr.right != null) q.add(curr.right);
            }
        }
        return root;
    }
}
```








## Pre order

https://leetcode.com/problems/binary-tree-preorder-traversal/description/

- Time: O(n)  ,         n = no of node
- Space: O(h) ,       h = height of tree
```
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {

        List<Integer> result = new ArrayList<>();
        preorder(root, result);
        return result;
    }

    private void preorder(TreeNode node, List<Integer> result  ){
        if(node == null) return;

        result.add(node.val);
        preorder(node.left, result);
        preorder(node.right, result);
    }
}
```

https://leetcode.com/problems/symmetric-tree/description/



- Time: O(n)           n = no of node
- Space
- O(h) = O(log n) ,       (balanced tree)     h = height of tree         h recursive call
- O(n)                               skewed tree 
```
        return (left.val == right.val) 
        && check(left.left, right.right)
        && check(left.right, right.left);
```

```
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null)
            return true;
        
        return check(root.left, root.right);

    }

    private boolean check(TreeNode left, TreeNode right){

        if(left == null && right == null) return true;
        if(left == null || right == null) return false;

        return (left.val == right.val) 
        && check(left.left, right.right)
        && check(left.right, right.left);
    }
}
```

time = O(n) 

```
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
       return makeBST(nums, 0 , nums.length -1);
    }

    private TreeNode makeBST(int [] nums, int low, int high){
        if(low > high) return null;

        int mid = (low + high) / 2;
        TreeNode node = new TreeNode(nums[mid]);

        node.left = makeBST(nums, low, mid-1);
        node.right = makeBST(nums, mid+1, high);

        return node;
    }
}
```



Approach 2  : time = O(n) 

when we done traversing a particular path, we need to  remove that running sum from hash map

```
class Solution {
    public int pathSum(TreeNode root, int targetSum) {
    HashMap<Long, Integer> map = new HashMap<>();
    map.put(0L,1);
    return pathSum2(root, 0L, targetSum, map);

    }

    private int pathSum2(TreeNode root, long runningSum, int targetSum, HashMap<Long, Integer> map ){
        if(root == null) return 0;

        runningSum += root.val;
        int count = map.getOrDefault(runningSum - targetSum, 0);
        map.put(runningSum , map.getOrDefault(runningSum,0) + 1);

        count += pathSum2(root.left, runningSum, targetSum, map);
        count += pathSum2(root.right, runningSum, targetSum, map);

        map.put(runningSum, map.get(runningSum) -1);

        return count;
    }

}
```



Approach 1  : time = O( n^2)

```
class Solution {
    public int pathSum(TreeNode root, int targetSum) {

        if (root == null) return 0;
        
        return
        pathSum( root.left,  targetSum) + 
        pathSum( root.right,  targetSum) +
        Sumfnx(root,targetSum);

    }

    private int Sumfnx(TreeNode root, long targetSum){
        if(root == null) return 0;

        int count = 0 ; 
        if(root.val == targetSum) count++;

        long newTarget = targetSum - root.val;

        count += Sumfnx(root.left, newTarget);
        count += Sumfnx(root.right, newTarget);

        return count;
    }

}
```

```
import java.util.HashMap;

class Solution {

        // Recursive helper fnx
    private TreeNode helper(int[] preorder, int[] preidx, int left, int right, HashMap<Integer, Integer> inMap){
    
		// base case :: no nodes in this subtree
        if(left > right) return null; 
        
        // Create the root node with the current preorder value
        TreeNode root = new TreeNode();
        root.val = preorder[preidx[0]];
        preidx[0]++;
        
		// Find index of root value in inorder
        int inorderIdx = inMap.get(root.val);  
        
        // Recursively build the left and right subtrees
        root.left =  helper(preorder, preidx, left, inorderIdx - 1, inMap); 
        root.right = helper(preorder, preidx, inorderIdx + 1, right, inMap); 

        return root;
    }


    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // Map value to index for quick inorder lookup
        HashMap<Integer, Integer> inMap = new HashMap<>();
        for(int i = 0; i < inorder.length; i++){
            inMap.put(inorder[i], i);
        }

		// mutable preorder index reference, it act as pass by reference
        int[] preidx = new int[]{0}; 
        
        //build tree
        return helper(preorder, preidx, 0, preorder.length - 1, inMap);
    }
}
```







https://www.youtube.com/watch?v=-DzowlcaUmE

## Level order⭐⭐

⇒ if pointer on null and you’re removing it..

 ⇒ just put again the null pointer in queue at the time when you are removing it



## Count of Node O(N)

## Sum of Node O(N)



## height of Node O(N)



## Diameter of Tree  → two case

###                        Approach - 1  O( N^2) 



###          Approach - 2 O(N)

height and diam calc simultaneously







## ✅ 1. Are Trees and Graphs the Same?

No, but a tree is a special type of graph.

✅ So, every tree is a graph, but not every graph is a tree.

## ✅ 2. Are Inorder, Preorder, Postorder Traversals for Graphs Too?

No, these are only for trees (mainly binary trees).

## ✅ 3. DFS and BFS (Depth-First Search and Breadth-First Search)

These are graph traversal algorithms, but also work on trees.

## ✅ 4. Summary Table

## ✅ So... Are These the Same?

## ✅ Summary (The Analogy You’re Asking For):



## ✅ 5. What You Need to Learn: Tree & Graph Roadmap

### 🌳 Trees

- Types:
- Binary Tree
- Binary Search Tree (BST)
- AVL Tree, Red-Black Tree
- Segment Tree, Fenwick Tree
- Trie (Prefix Tree)
- N-ary Tree
- Traversals:
- Inorder, Preorder, Postorder
- Level-order (BFS)
- Problems:
- Lowest Common Ancestor
- Diameter of Tree
- Tree to Linked List
- Path Sum
- Balanced Tree checks
### 📊 Graphs

- Types:
- Directed / Undirected
- Weighted / Unweighted
- Cyclic / Acyclic
- DAG (Directed Acyclic Graph)
- Representations:
- Adjacency List / Matrix
- Traversal:
- DFS (iterative/recursive)
- BFS
- Algorithms:
- Dijkstra’s (shortest path)
- Bellman-Ford
- Floyd-Warshall
- Topological Sort
- Union-Find (Disjoint Set)
- Kruskal’s, Prim’s (Minimum Spanning Tree)
- Problems:
- Detect Cycle
- Connected Components
- Bipartite Graph Check
- Strongly Connected Components (Tarjan’s)




A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than on

## ✅ 1. Binary Tree (Generic Structure)

```
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}


```

### ✅ Use Case:

- Any general tree-based question: DFS, BFS, traversal, diameter, LCA
## ✅ 2. Binary Search Tree (BST)

```
class BST {
    TreeNode root;

    void insert(int val) {
        root = insert(root, val);
    }

    private TreeNode insert(TreeNode node, int val) {
        if (node == null) return new TreeNode(val);
        if (val < node.val) node.left = insert(node.left, val);
        else node.right = insert(node.right, val);
        return node;
    }

    boolean search(int val) {
        return search(root, val);
    }

    private boolean search(TreeNode node, int val) {
        if (node == null) return false;
        if (val == node.val) return true;
        return val < node.val ? search(node.left, val) : search(node.right, val);
    }
}


```

### ⏱ Time:

- Insert/Search/Delete: O(log n) average, O(n) worst (unbalanced)
## ✅ 3. AVL Tree (Self-balancing BST)

```
class AVLNode {
    int val, height;
    AVLNode left, right;
    AVLNode(int val) { this.val = val; height = 1; }
}

class AVLTree {
    AVLNode root;

    int height(AVLNode n) {
        return n == null ? 0 : n.height;
    }

    int getBalance(AVLNode n) {
        return n == null ? 0 : height(n.left) - height(n.right);
    }

    AVLNode rotateRight(AVLNode y) {
        AVLNode x = y.left;
        AVLNode T = x.right;
        x.right = y;
        y.left = T;
        y.height = 1 + Math.max(height(y.left), height(y.right));
        x.height = 1 + Math.max(height(x.left), height(x.right));
        return x;
    }

    AVLNode rotateLeft(AVLNode x) {
        AVLNode y = x.right;
        AVLNode T = y.left;
        y.left = x;
        x.right = T;
        x.height = 1 + Math.max(height(x.left), height(x.right));
        y.height = 1 + Math.max(height(y.left), height(y.right));
        return y;
    }

    AVLNode insert(AVLNode node, int val) {
        if (node == null) return new AVLNode(val);
        if (val < node.val) node.left = insert(node.left, val);
        else if (val > node.val) node.right = insert(node.right, val);
        else return node;

        node.height = 1 + Math.max(height(node.left), height(node.right));
        int balance = getBalance(node);

        // 4 Rotations
        if (balance > 1 && val < node.left.val) return rotateRight(node);
        if (balance < -1 && val > node.right.val) return rotateLeft(node);
        if (balance > 1 && val > node.left.val) {
            node.left = rotateLeft(node.left);
            return rotateRight(node);
        }
        if (balance < -1 && val < node.right.val) {
            node.right = rotateRight(node.right);
            return rotateLeft(node);
        }

        return node;
    }
}


```

### ⏱ Time:

- Insert/Search/Delete: O(log n) guaranteed
## ✅ 4. Red-Black Tree

📌 Use TreeMap / TreeSet in Java — internally implemented as Red-Black Tree.

```
TreeMap<Integer, String> map = new TreeMap<>();
TreeSet<Integer> set = new TreeSet<>();


```

- All operations: O(log n)
- Maintains a sorted order
## ✅ 5. Segment Tree (for Range Queries)

```
class SegmentTree {
    int[] tree, arr;
    int n;

    SegmentTree(int[] input) {
        arr = input;
        n = input.length;
        tree = new int[4 * n];
        build(0, 0, n - 1);
    }

    void build(int node, int start, int end) {
        if (start == end) tree[node] = arr[start];
        else {
            int mid = (start + end) / 2;
            build(2 * node + 1, start, mid);
            build(2 * node + 2, mid + 1, end);
            tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
        }
    }

    int query(int l, int r) {
        return query(0, 0, n - 1, l, r);
    }

    int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return 0;
        if (l <= start && end <= r) return tree[node];
        int mid = (start + end) / 2;
        return query(2 * node + 1, start, mid, l, r)
             + query(2 * node + 2, mid + 1, end, l, r);
    }
}


```

### ⏱ Time:

- Build: O(n), Query: O(log n), Update: O(log n)
## ✅ 6. Fenwick Tree (Binary Indexed Tree)

```
class FenwickTree {
    int[] bit;
    int n;

    FenwickTree(int size) {
        n = size;
        bit = new int[n + 1];
    }

    void update(int i, int val) {
        for (; i <= n; i += i & -i)
            bit[i] += val;
    }

    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i)
            sum += bit[i];
        return sum;
    }
}


```

### ⏱ Time:

- Update/Query: O(log n)
## ✅ 7. Trie (Prefix Tree)

```
class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isWord = false;
}

class Trie {
    TrieNode root = new TrieNode();

    void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if (node.children[c - 'a'] == null)
                node.children[c - 'a'] = new TrieNode();
            node = node.children[c - 'a'];
        }
        node.isWord = true;
    }

    boolean search(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if (node.children[c - 'a'] == null) return false;
            node = node.children[c - 'a'];
        }
        return node.isWord;
    }

    boolean startsWith(String prefix) {
        TrieNode node = root;
        for (char c : prefix.toCharArray()) {
            if (node.children[c - 'a'] == null) return false;
            node = node.children[c - 'a'];
        }
        return true;
    }
}


```

### ⏱ Time:

- Insert/Search: O(L), L = length of word
## ✅ 8. N-ary Tree

```

class NaryNode {
    int val;
    List<NaryNode> children;

    NaryNode(int val) {
        this.val = val;
        children = new ArrayList<>();
    }
}
```

### Use Case:

- LeetCode N-ary tree traversal (e.g., postorder)


# Trees: Comprehensive Notes for Interview Preparation (Java-Specific)

## 1. Introduction to Trees

### What is a Tree?

- A tree is a hierarchical data structure consisting of nodes connected by edges.
- Properties:
- Root: The topmost node.
- Parent and Child: Nodes connected directly.
- Leaf: A node without children.
- Height: The longest path from the root to a leaf.
- Depth: The level of a node from the root.
- Subtree: Any node and its descendants.
### Types of Trees:

- Binary Tree: Each node has at most two children.
- Binary Search Tree (BST): A binary tree where left child < root < right child.
- Balanced Trees:
- AVL Tree: Balances height after every insertion or deletion.
- Red-Black Tree: Ensures balance using color coding.
- Segment Tree: Used for range queries.
- Fenwick Tree: Used for prefix sums.


### Applications:

- Expression Trees (parsing mathematical expressions)
- Search and optimization problems
- File systems and hierarchical data representation
## 2. Tree Traversals

### Types of Traversals:

3. Preorder Traversal: Root → Left → Right.
```
void preorderTraversal(TreeNode root) {
    if (root != null) {
        System.out.print(root.val + " ");
        preorderTraversal(root.left);
        preorderTraversal(root.right);
    }
}

```

3. Inorder Traversal: Left → Root → Right.
```
void inorderTraversal(TreeNode root) {
    if (root != null) {
        inorderTraversal(root.left);
        System.out.print(root.val + " ");
        inorderTraversal(root.right);
    }
}

```

3. Postorder Traversal: Left → Right → Root.
```
void postorderTraversal(TreeNode root) {
    if (root != null) {
        postorderTraversal(root.left);
        postorderTraversal(root.right);
        System.out.print(root.val + " ");
    }
}

```

3. Level Order Traversal (BFS): Traverse level by level.
```
void levelOrderTraversal(TreeNode root) {
    if (root == null) return;
    Queue<TreeNode> queue = new LinkedList<>();
    queue.add(root);

    while (!queue.isEmpty()) {
        TreeNode node = queue.poll();
        System.out.print(node.val + " ");
        if (node.left != null) queue.add(node.left);
        if (node.right != null) queue.add(node.right);
    }
}

```

### Common Patterns:

- Recursive vs Iterative approaches.
- Using stacks for DFS and queues for BFS.
## 3. Advanced Tree Concepts

### Binary Search Trees (BST):

- Insertion:
```
TreeNode insert(TreeNode root, int val) {
    if (root == null) {
        return new TreeNode(val);
    }
    if (val < root.val) {
        root.left = insert(root.left, val);
    } else {
        root.right = insert(root.right, val);
    }
    return root;
}

```

- Deletion:
```
TreeNode delete(TreeNode root, int key) {
    if (root == null) return null;

    if (key < root.val) {
        root.left = delete(root.left, key);
    } else if (key > root.val) {
        root.right = delete(root.right, key);
    } else {
        // Node with only one child or no child
        if (root.left == null) return root.right;
        if (root.right == null) return root.left;

        // Node with two children: Get the inorder successor
        TreeNode successor = getMinValueNode(root.right);
        root.val = successor.val;
        root.right = delete(root.right, successor.val);
    }
    return root;
}

TreeNode getMinValueNode(TreeNode node) {
    while (node.left != null) {
        node = node.left;
    }
    return node;
}

```

### Balanced Trees:

- AVL Tree: Rotation operations (left and right) to maintain balance.
- Red-Black Tree: Balancing using coloring rules.
### Segment Trees:

- Range queries like sum, minimum, or maximum in intervals.
- Efficient updates.
### Fenwick Tree (Binary Indexed Tree):

- Prefix sum computation.
- Space-efficient representation.
## 4. Interview Patterns and Techniques

### Cheat Sheet for Trees:

- Traversal templates (Preorder, Inorder, Postorder, Level Order).
- Common operations (Insert, Delete, Search).
- Recognizing tree-related problems:
- Check for BST validity.
- Finding Lowest Common Ancestor (LCA).
- Diameter of a tree.
- Maximum path sum.
### Common Problems:

- Leetcode: Serialize and Deserialize Binary Tree, Binary Tree Zigzag Level Order Traversal, Validate BST.
### Optimization Techniques:

- Use memoization for repeated calculations.
- Avoid recursion depth limits by using iterative methods.
## 5. Tips and Tricks

- Pattern Recognition:
- If recursion is involved, think of tree traversal.
- Use stack/queue for iterative solutions.
- Debugging Recursive Solutions:
- Print intermediate values.
- Use visual aids like tree diagrams.
- Space Optimization:
- Tail recursion optimization.
- Efficient data structures for traversal.
## 6. Practice Problems



# Graphs: Comprehensive Notes for Interview Preparation (Java-Specific)

## 1. Introduction to Graphs

### What is a Graph?

- A graph is a collection of nodes (called vertices) and edges connecting pairs of vertices.
- Properties:
- Vertices (Nodes): Fundamental units of the graph.
- Edges: Connections between vertices.
- Directed vs Undirected Graphs:
- Directed: Edges have direction (A → B).
- Undirected: Edges have no direction (A ↔ B).
- Weighted Graphs: Edges have weights associated with them.
- Unweighted Graphs: Edges have no weights.
### Graph Representation:

3. Adjacency Matrix:
- A 2D array where matrix[i][j] indicates an edge between vertex i and j.
- Space complexity: O(V^2).
3. Adjacency List:
- Each vertex points to a list of its neighbors.
- Space complexity: O(V + E).
### Applications:

- Social networks
- Pathfinding (GPS, network routing)
- Circuit design and analysis
## 2. Graph Traversals

### Types of Traversals:

3. Depth First Search (DFS):
- Explore as deeply as possible before backtracking.
```
void dfs(int node, boolean[] visited, List<List<Integer>> graph) {
    visited[node] = true;
    System.out.print(node + " ");
    for (int neighbor : graph.get(node)) {
        if (!visited[neighbor]) {
            dfs(neighbor, visited, graph);
        }
    }
}

```

3. Breadth First Search (BFS):
- Explore all neighbors at the current depth before moving deeper.
```
void bfs(int startNode, List<List<Integer>> graph) {
    boolean[] visited = new boolean[graph.size()];
    Queue<Integer> queue = new LinkedList<>();
    queue.add(startNode);
    visited[startNode] = true;

    while (!queue.isEmpty()) {
        int node = queue.poll();
        System.out.print(node + " ");
        for (int neighbor : graph.get(node)) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                queue.add(neighbor);
            }
        }
    }
}

```

3. Topological Sort:
- Linear ordering of vertices for a Directed Acyclic Graph (DAG).
```
void topologicalSort(int node, boolean[] visited, Stack<Integer> stack, List<List<Integer>> graph) {
    visited[node] = true;
    for (int neighbor : graph.get(node)) {
        if (!visited[neighbor]) {
            topologicalSort(neighbor, visited, stack, graph);
        }
    }
    stack.push(node);
}

```

3. Shortest Path Algorithms:
- Dijkstra's Algorithm: Finds shortest paths from a source vertex.
```
void dijkstra(int src, int vertices, List<List<int[]>> graph) {
    int[] dist = new int[vertices];
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[src] = 0;

    PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
    pq.add(new int[]{src, 0});

    while (!pq.isEmpty()) {
        int[] curr = pq.poll();
        int node = curr[0], weight = curr[1];

        for (int[] neighbor : graph.get(node)) {
            int nextNode = neighbor[0], edgeWeight = neighbor[1];
            if (dist[node] + edgeWeight < dist[nextNode]) {
                dist[nextNode] = dist[node] + edgeWeight;
                pq.add(new int[]{nextNode, dist[nextNode]});
            }
        }
    }
    System.out.println(Arrays.toString(dist));
}

```

## 3. Advanced Graph Concepts

### Minimum Spanning Tree (MST):

3. Prim’s Algorithm:
- Greedy algorithm to find the MST.
```
void primMST(int vertices, List<List<int[]>> graph) {
    boolean[] visited = new boolean[vertices];
    PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
    pq.add(new int[]{0, 0}); // {node, weight}
    int mstWeight = 0;

    while (!pq.isEmpty()) {
        int[] curr = pq.poll();
        int node = curr[0], weight = curr[1];
        if (visited[node]) continue;

        visited[node] = true;
        mstWeight += weight;
        for (int[] neighbor : graph.get(node)) {
            if (!visited[neighbor[0]]) {
                pq.add(new int[]{neighbor[0], neighbor[1]});
            }
        }
    }
    System.out.println("MST Weight: " + mstWeight);
}

```

3. Kruskal’s Algorithm:
- Sort edges by weight and use union-find to include edges in the MST.
```
void kruskalMST(int vertices, List<int[]> edges) {
    edges.sort((a, b) -> a[2] - b[2]); // Sort by weight
    UnionFind uf = new UnionFind(vertices);
    int mstWeight = 0;

    for (int[] edge : edges) {
        int u = edge[0], v = edge[1], weight = edge[2];
        if (uf.union(u, v)) {
            mstWeight += weight;
        }
    }
    System.out.println("MST Weight: " + mstWeight);
}

class UnionFind {
    int[] parent, rank;
    UnionFind(int size) {
        parent = new int[size];
        rank = new int[size];
        for (int i = 0; i < size; i++) parent[i] = i;
    }
    int find(int node) {
        if (parent[node] != node) {
            parent[node] = find(parent[node]); // Path compression
        }
        return parent[node];
    }
    boolean union(int u, int v) {
        int rootU = find(u), rootV = find(v);
        if (rootU == rootV) return false;

        if (rank[rootU] > rank[rootV]) parent[rootV] = rootU;
        else if (rank[rootU] < rank[rootV]) parent[rootU] = rootV;
        else {
            parent[rootV] = rootU;
            rank[rootU]++;
        }
        return true;
    }
}

```

### Strongly Connected Components (SCC):

- Kosaraju’s Algorithm:
- Perform DFS, reverse the graph, and DFS again.
## 4. Interview Patterns and Techniques

### Cheat Sheet for Graphs:

- Traversal templates (DFS, BFS, Topological Sort).
- Common operations (Shortest Path, MST).
- Recognizing graph-related problems:
- Cycle detection.
- SCC identification.
- Pathfinding in weighted/unweighted graphs.
### Common Problems:

- Leetcode: Number of Islands, Course Schedule, Clone Graph, Network Delay Time.
## 5. Tips and Tricks

- Pattern Recognition:
- If recursion or stack is involved, it's likely DFS.
- Use queue for BFS-related problems.
- Debugging Graph Solutions:
- Print adjacency lists/matrix for verification.
- Use visual aids like graph diagrams.
- Space Optimization:
- Use adjacency lists for sparse graphs.
- Avoid recursion depth limits by using stack/queue-based iterative solutions.
## 6. Practice Problems

### Curated Leetcode Problems:

3. Number of Islands
3. Clone Graph
3. Course Schedule
3. Network Delay Time
3. Shortest Path in Binary Matrix
## 7. Cheatsheet

### Graph Traversal Templates:

```
// DFS Template
void dfs(int node, boolean[] visited, List<List<Integer>> graph) {
    visited[node] = true;
    for (int neighbor : graph.get(node)) {
        if (!visited[neighbor]) {
            dfs(neighbor, visited, graph);
        }
    }
}

// BFS Template
void bfs(int startNode, List<List<Integer>> graph) {
    boolean[] visited = new boolean[graph.size()];
    Queue<Integer> queue = new LinkedList<>();
    queue.add(startNode);
    visited[startNode] = true;

    while (!queue.isEmpty()) {
        int node = queue.poll();
        for (int neighbor : graph.get(node)) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                queue.add(neighbor);
            }
        }
    }
}

```

### Key Formulas:

- Space complexity of adjacency matrix: O(V^2)
- Space complexity of adjacency list: O(V + E)




## 1. Introduction to Graphs

### Complexity Analysis:

- Space complexity for storing a graph:
- Adjacency Matrix: O(V^2) (for V vertices).
- Adjacency List: O(V + E) (for E edges).
- Operations:
- Adding an edge:
- Adjacency Matrix: O(1).
- Adjacency List: O(1).
- Checking edge existence:
- Adjacency Matrix: O(1).
- Adjacency List: O(degree).
### Tips and Tricks:

- Graph Representation Mnemonic:
- Dense graphs → Use Adjacency Matrix.
- Sparse graphs → Use Adjacency List.
## 2. Graph Traversals

### Complexity Analysis:

- DFS:
- Time complexity: O(V + E) (visiting all vertices and edges).
- Space complexity: O(V) (stack size for recursion depth).
- BFS:
- Time complexity: O(V + E).
- Space complexity: O(V) (queue size).
- Topological Sort:
- Time complexity: O(V + E).
### Tips and Tricks:

- Traversal Mnemonic:
- DFS: Think "Stack" → Explore deeply before backtracking.
- BFS: Think "Queue" → Explore neighbors level by level.
- Cycle Detection:
- Use DFS for directed graphs.
- Use Union-Find for undirected graphs.
## 3. Advanced Graph Concepts

### Complexity Analysis:

- Dijkstra’s Algorithm:
- Time complexity: O((V + E) log V) using Priority Queue.
- Prim’s Algorithm:
- Time complexity: O((V + E) log V) using Priority Queue.
- Kruskal’s Algorithm:
- Time complexity: O(E log E) (sorting edges).
- Strongly Connected Components (SCC):
- Kosaraju’s Algorithm: O(V + E).
### Tips and Tricks:

- Shortest Path Mnemonic:
- Dijkstra → Best for non-negative weights.
- Bellman-Ford → Best for graphs with negative weights.
- MST Rule:
- Use Prim’s for dense graphs (Priority Queue).
- Use Kruskal’s for sparse graphs (Union-Find).
## 4. Interview Patterns

### Complexity Analysis:

- Recognizing patterns:
- Cycle detection: O(V + E) using DFS.
- SCC detection: O(V + E) using Kosaraju’s Algorithm.
- Pathfinding: O((V + E) log V) using Dijkstra’s Algorithm.
### Tips and Tricks:

- Debugging Traversals:
- Print adjacency lists/matrix for verification.
- Use visual aids like graph diagrams.
- Space Optimization:
- Use adjacency lists for sparse graphs.
- Avoid recursion depth limits by using stack/queue-based iterative solutions.
## ✅ Depth First Search (DFS)

📌 None of these are tree problems. All are graph or grid-based.

## ✅ Breadth First Search (BFS)

📌 Again, none are tree problems.

## ✅ What is a BST (Binary Search Tree)?

A Binary Search Tree is a type of binary tree with these key rules:

### 🌳 Properties of a BST:

3. Each node has at most two children.
3. Left child has value less than the node.
3. Right child has value greater than the node.
3. This rule is recursively true for all subtrees.
### 📈 Example:

```
markdown
CopyEdit
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13


```

- All nodes to the left of 8 are < 8
- All nodes to the right of 8 are > 8
## ✅ What Can a BST Do?

BST is used for fast search, insert, and delete operations.

## ✅ What is an Ordered Set?

An ordered set is a data structure that:

3. Stores elements in sorted order
3. Does not allow duplicates
3. Allows fast insert, delete, and find
### 📌 Examples:

- In C++, std::set is an ordered set (implemented as Red-Black Tree).
- In Python, the built-in set is unordered, but you can use SortedSet from sortedcontainers package for an ordered set.
- In Java, TreeSet is an ordered set (uses a self-balancing BST).
### 🧠 So, What’s the Relation?

That’s why they have similar operations and performance characteristics.

## ✅ Summary: BST vs Ordered Set

## 1. Java Collections Overview

### Types of Collections:

3. List:
- Implementation: ArrayList, LinkedList.
- Use Case: Dynamic arrays, iteration.
- Time Complexity:
- Access: O(1) (ArrayList), O(n) (LinkedList).
- Insert/Delete: O(n) (ArrayList), O(1) (LinkedList for head/tail).
3. Set:
- Implementation: HashSet, TreeSet.
- Use Case: Unique elements.
- Time Complexity:
- HashSet: Add/Delete/Search → O(1) (average), O(n) (worst case).
- TreeSet: Add/Delete/Search → O(log n).
3. Map:
- Implementation: HashMap, TreeMap.
- Use Case: Key-value pairs.
- Time Complexity:
- HashMap: Insert/Search/Delete → O(1) (average), O(n) (worst case).
- TreeMap: Insert/Search/Delete → O(log n).
## 🌳 1. Tree-Specific Collections & Patterns

```
java
CopyEdit
// 🧱 Tree Node (Binary Tree)
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

// 📍 BFS Traversal — Level Order (uses Queue)
Queue<TreeNode> queue = new LinkedList<>();
queue.offer(root);
while (!queue.isEmpty()) {
    TreeNode node = queue.poll();
    if (node.left != null) queue.offer(node.left);
    if (node.right != null) queue.offer(node.right);
}

// 🧗 DFS Traversal — Preorder/Postorder/Inorder (use Stack or Recursion)
Stack<TreeNode> stack = new Stack<>();
stack.push(root);
while (!stack.isEmpty()) {
    TreeNode node = stack.pop();
    // process node
    if (node.right != null) stack.push(node.right);
    if (node.left != null) stack.push(node.left);
}

// 🧮 TreeMap — Sorted Map (Red-Black Tree internally)
TreeMap<Integer, String> treeMap = new TreeMap<>();
treeMap.put(3, "Three");  // Sorted by key
treeMap.firstKey();       // Min
treeMap.lastKey();        // Max

// 🧮 TreeSet — Sorted Set (No duplicates, Red-Black Tree)
TreeSet<Integer> treeSet = new TreeSet<>();
treeSet.add(5);
treeSet.add(1);
treeSet.contains(5);
treeSet.higher(3);  // Smallest > 3

// 📘 PriorityQueue — Min or Max Heap
PriorityQueue<Integer> minHeap = new PriorityQueue<>();
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
minHeap.offer(1);
minHeap.poll();  // Removes min

// 🔁 LinkedList as Deque (for Zigzag level order)
Deque<TreeNode> deque = new LinkedList<>();
deque.addFirst(node);  // Acts like Stack
deque.addLast(node);   // Acts like Queue

// 📝 Map<TreeNode, Integer> — For memoizing subtree info
Map<TreeNode, Integer> memo = new HashMap<>();


```

## 🔗 2. Graph-Specific Collections & Patterns

```
java
CopyEdit
// 📍 Graph using Adjacency List
Map<Integer, List<Integer>> graph = new HashMap<>();
graph.putIfAbsent(1, new ArrayList<>());
graph.get(1).add(2);  // Edge from 1 to 2

// 🔁 DFS using Stack
Set<Integer> visited = new HashSet<>();
Stack<Integer> stack = new Stack<>();
stack.push(start);
while (!stack.isEmpty()) {
    int node = stack.pop();
    if (visited.contains(node)) continue;
    visited.add(node);
    for (int nei : graph.getOrDefault(node, new ArrayList<>())) {
        stack.push(nei);
    }
}

// 🔁 DFS (recursive)
void dfs(int node, Set<Integer> visited) {
    if (!visited.add(node)) return;
    for (int nei : graph.getOrDefault(node, new ArrayList<>())) {
        dfs(nei, visited);
    }
}

// 🚎 BFS using Queue
Queue<Integer> queue = new LinkedList<>();
Set<Integer> visited = new HashSet<>();
queue.offer(start);
visited.add(start);
while (!queue.isEmpty()) {
    int node = queue.poll();
    for (int nei : graph.getOrDefault(node, new ArrayList<>())) {
        if (!visited.contains(nei)) {
            visited.add(nei);
            queue.offer(nei);
        }
    }
}

// 🧱 Edge list or weighted graph (for Dijkstra)
class Pair {
    int node, weight;
    Pair(int node, int weight) {
        this.node = node; this.weight = weight;
    }
}
Map<Integer, List<Pair>> weightedGraph = new HashMap<>();
weightedGraph.computeIfAbsent(0, k -> new ArrayList<>()).add(new Pair(1, 5));

// 🛣️ PriorityQueue for Dijkstra’s Algorithm
PriorityQueue<Pair> pq = new PriorityQueue<>((a, b) -> a.weight - b.weight);

// 🧪 Union-Find (Disjoint Set)
int[] parent = new int[n];
for (int i = 0; i < n; i++) parent[i] = i;

int find(int x) {
    if (parent[x] != x) parent[x] = find(parent[x]);  // Path compression
    return parent[x];
}
void union(int a, int b) {
    parent[find(a)] = find(b);
}


```

## 🛠️ Utility Java Collections Patterns

```
java
CopyEdit
// 🔢 Count frequency of elements
Map<Integer, Integer> freq = new HashMap<>();
for (int num : nums) {
    freq.put(num, freq.getOrDefault(num, 0) + 1);
}

// 📋 Grouping elements
Map<Integer, List<String>> map = new HashMap<>();
map.computeIfAbsent(3, k -> new ArrayList<>()).add("abc");

// 🔁 Iterate Map
for (Map.Entry<Integer, List<String>> entry : map.entrySet()) {
    int key = entry.getKey();
    List<String> valList = entry.getValue();
}


```



### Time Complexity Summary

### Tree Collections

- Binary Tree:
- Traversals: O(n)
- Binary Search Tree (BST):
- Insert/Delete/Search: Avg O(log n), Worst O(n)
- AVL Tree:
- Insert/Delete/Search: O(log n)
- Trie:
- Insert/Search: O(m) (m = word length)
- N-ary Tree:
- Traversals: O(n)
### Graph Collections

- Adjacency List:
- Add Edge: O(1)
- DFS/BFS Traversals: O(V + E)
- Weighted Graph (Dijkstra):
- O((V + E) log V) using Priority Queue
## 📊 Time Complexity Summary for Collections

# 🧾 Summary: Collections by Use Case



## String  

(im-mutable)



The Java String Constant Pool, also known as the String Pool or String Intern Pool, is a special memory area within the Java Heap that is dedicated to storing unique string literals. Its primary purpose is to optimize memory usage and improve performance by reusing existing string objects.

Key characteristics and mechanisms:

- Location: The String Constant Pool resides within the Heap memory, not a separate memory region.
- Storage of String Literals: When you create a string using a literal 
(e.g., String s = "hello";)
the Java Virtual Machine (JVM) first checks if an identical string already exists in the String Constant Pool.
- If the string literal is found, the JVM returns a reference to that existing string object, avoiding the creation of a new one.
- If the string literal is not found, the JVM creates a new string object in the String Constant Pool and stores its reference.
- Uniqueness:  The String Constant Pool stores only unique string objects. Duplicates are not permitted, which contributes to memory efficiency.
- Immutability:  String objects in Java are immutable. This characteristic allows them to be safely shared within the String Constant Pool without concerns about unintended modifications by different parts of the code.
```
Object point examples for Array

changes on arr will reflect to brr

        int arr[] = new int[3];
        arr[0] = 4;
        System.out.println(arr[0]);    // 4
        int brr[] = arr;               // --> both point to same 
        brr[0] = 8;
        System.out.println(arr[0]);    //8
```

```
Object point examples for String

this will not work same  in — strings
				
				String name1 = "Shashwat";
			  System.out.println(name1)  //Shashwat
        String name2 = name1;      // b points to Shashwat (same as name1 point)
        name2 = "Amit";            // b points to Amit (created new Amit in Heap
        System.out.println(name1);  //Shashwat
```

```
==  in String

//        String name1 = "Shashwat";
//        String name2 = "Shashwat";
//        String name3 = "Shashwat";
//        String name4 = name1;


//        System.out.println(name1==name2);
//        System.out.println(name2==name3);
//        System.out.println(name3==name4);
//        System.out.println(name4==name2);
//        System.out.println(name1==name4);
			---------- All true -----------
```

```
.equals()  

it compare value not references			
//		     System.out.println(name1.equals(name2) );
//        System.out.println(name2.equals(name3));
//        System.out.println(name3.equals(name4));
//        System.out.println(name4.equals(name2));
//        System.out.println(name1.equals(name4));
			---------- All true -----------
```

```
==  in Array
 since all are different object 

//        int name1[]= new int[3];
//        int name2[]= new int[3];
//        int name3[]= new int[3];
//        int name4[]= name1;
//
//        System.out.println(name1==name2);
//        System.out.println(name2==name3);
//        System.out.println(name3==name4);
//        System.out.println(name4==name2);
          System.out.println(name1==name4);   <-- only this true
```

```
new keyword

//        String name1 = new String("Shashwat");
//        String name2 = new String("Shashwat");
//        String name3 = new String("Shashwat");

new object Shashwat will be created evrytime in heap memory..
and name1 ,name2 , name3 will point to different object 
but String Pool will have only one Shashwat and all new created object will be 
verified / validate by String pool

if it was not present in String poll, then the object shashwat will first 
created in string pool then as a new object

```




## String Builder  (performance)

(mutable) 

(Method Chaining) 

## String Buffer

(mutable) 

(Method Chaining) 

(Thread Safe)









3. Taking inputs and Buffer Class
Print —>  belongs to print Stream class

out —> null object created as static variable inside System Class       when calling .. Print Stream
                so, out is object of type Print Stream

in ——> object  in , is of type Input Stream

 .read( ) —> throw IOexception and return int  (ASCI value ), 
                      Read only one character at a time i.e for reading 555, use loop

int num = Sytem.in.read( )    //num will store ASCI /// to get original no —>   num- 48



 .readLine( ) —> throw IOexception  ,,   Reads String

3. Buffer Reader —> under package i.o — > java.io.IOException,  java.io.BufferReader
InputStreamReader isr = new InputStreamReader (System.in)
BufferReadered br = new BufferReadered (isr);
   —> can take input from  InputStreamReader , FIle , Network , Keyboard



int num = br.readLine( ) 
 — > Reads String

int num = Integer.parseInt(br.readLine( ))
 — > Reads Integer  (32 bit)

char c =  (char) br.read ( ) —> read character

/// all parse Lines

int num = Float.parseFloat(br.readLine( ))
 — > Reads Float (upto 6 decimal)

int num = Double.parseDouble(br.readLine( ))
 — > Reads Double (upto 15 deci)

int num = Long.parseLong(br.readLine( ))
 — > Reads Double (64 bit)

int num = Short.parseShort(br.readLine( ))
 — > Reads Short(16 bit)



br.close( )  → close after using buffer reader

3. Scanner Class and methods   —> inside util package
Scanner sc  = new Scanner( System.in )





3. Expection and error , 
@SuppressWarnings("unchecked")
 ,, how to handle and which java version to use






3. File Handling 
```
            //creating file
            File myObj = new File("students.txt");
            myObj.createNewFile();

            //writing on a file
             FileWriter file = new FileWriter("students.txt");
             file.write("This file has information of Teachers");
             file.close();
 
            //reading 
            File file = new File("Teachers.txt");
            Scanner myReader = new Scanner(file);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                System.out.println(data);
            }
            myReader.close();
            
            //deleting
             if (file.delete()) { 
            System.out.println("Deleted Successfully: " + file.getName());
```











String

all methods of string 

scanner 

math

java

io



### Arrays & Strings

- ✅Arrays 
- Strings
- Bit Manipulation
- Hash Tables
### Two-Pointer & Sliding Window

- Two Pointers
- ✅Prefix Sum
- Sliding Window - Fixed Size
- Sliding Window - Dynamic Size
- ✅Kadane's Algorithm
### Matrix & Linked Lists

- Matrix (2D Array)
- ✅Linked List
- ✅LinkedList In-place Reversal
- ✅Fast and Slow Pointers
### Stacks & Queues

- ✅Stacks
- ✅Monotonic Stack
- ✅Queues
- ✅Monotonic Queue
### Sorting & Searching

- Bucket Sort
- Merge Sort
- QuickSort / QuickSelect
- Binary Search
### Recursion & Backtracking

- Recursion
- Divide and Conquer
- Backtracking
### Tree & Graph Traversals

- Tree Traversal - Level Order
- Tree Traversal - Pre Order
- Tree Traversal - In Order
- Tree Traversal - Post-Order
- BST / Ordered Set
- Tries
- Heaps
- Two Heaps
- Top K Elements
- Intervals
- K-Way Merge
### Advanced Data Structures & Algorithms

- Data Structure Design
- Greedy
- Depth First Search (DFS)
- Breadth First Search (BFS)
- Topological Sort
- Union Find
- Minimum Spanning Tree
- Shortest Path
- Eulerian Circuit
### Dynamic Programming (DP)

- 1-D DP
- Knapsack DP
- Unbounded Knapsack DP
- Longest Increasing Subsequence DP
- 2D (Grid) DP
- String DP
- Tree / Graph DP
- Bitmask DP
- Digit DP
- Probability DP
- State Machine DP
### Other Patterns

- String Matching
- Binary Indexed Tree / Segment Tree
- Maths / Geometry
- Line Sweep
- Suffix Array

_Last updated: 2025-10-31 12:36:38_
