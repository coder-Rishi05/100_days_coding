### Stack in js

code

```
class Stack {
  constructor() {
    this.items = [];
  }
  push(element) {
    this.items.push(element);
  }
  peek(pos) {
    if (this.isEmpty()) {
      return null;
    }
    return this.items[this.items.length - 1];
  }
  pop() {
    if (this.isEmpty()) {
      return null;
    }
    const removedElement = this.items.pop();
    return removedElement;
  }
  isEmpty(i) {
    return this.items.length === 0;
  }
  getSize() {
    return this.items.length;
  }
}

// test code

const stack = new Stack();
stack.push(10);
stack.push(20);
stack.push(40);
stack.push(30);
console.log("top element : " + stack.peek());
const x = stack.pop();
console.log("removed element : " + x);
console.log("top element : " + stack.peek());

```