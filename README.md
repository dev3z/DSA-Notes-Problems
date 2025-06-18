# Synced Notion Notes

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





## ✅ Monotonic Stack

 → Next Greater / Smaller

 → Previous Greater / Smaller  

 → Array related , Time O(n²)  → O(n)

 → Better To Store indices of Array

### Monotonic Increasing



### NGE (

### Monotonic Decreasing



```
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

_Last updated: 2025-06-18 08:50:55_
