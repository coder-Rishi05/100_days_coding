
# JavaScript Queue Implementation

This project demonstrates how to implement a **Queue** in JavaScript using a class. A **Queue** is a linear data structure which follows the **FIFO (First In First Out)** principle. The element that is added first will be removed first.

---

## Features / Functions

### 1. `enqueue(element)`
Adds an element at the **rear** of the queue.

**Example:**
```js
queue.enqueue(10);
queue.enqueue(20);
```

### 2. `dequeue()`
Removes and returns the element from the **front** of the queue.  
Returns `null` if the queue is empty.

**Example:**
```js
let removed = queue.dequeue();
console.log(removed); // 10
```

### 3. `getFront()`
Returns the **front element** without removing it.  
Returns `null` if the queue is empty.

**Example:**
```js
console.log(queue.getFront()); // 20
```

### 4. `getRear()`
Returns the **rear element** without removing it.  
Returns `null` if the queue is empty.

**Example:**
```js
console.log(queue.getRear()); // 20
```

### 5. `isEmpty()`
Checks if the queue is empty. Returns `true` or `false`.

**Example:**
```js
console.log(queue.isEmpty()); // false
```

### 6. `getSize()`
Returns the number of elements in the queue.

**Example:**
```js
console.log(queue.getSize()); // 1
```

---

## Example Usage

```js
const queue = new Queue();
queue.enqueue(10);
queue.enqueue(30);
queue.enqueue(50);

console.log("Front =", queue.getFront(), "Rear =", queue.getRear()); // Front = 10 Rear = 50

const deleted_item = queue.dequeue();
console.log("Deleted item:", deleted_item); // 10

console.log("Front =", queue.getFront(), "Rear =", queue.getRear()); // Front = 30 Rear = 50
console.log("Is empty:", queue.isEmpty()); // false
console.log("Size of queue:", queue.getSize()); // 2
```

---

## Notes
- This queue uses **arrays** internally.
- Works best for learning queue concepts.
- All operations have **O(1) time complexity** for enqueue and dequeue if using `push` and `shift`.
