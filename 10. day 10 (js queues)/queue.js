class Queue {
  constructor() {
    this.items = [];
  }
  enqueue(ele) {
    this.items.push(ele);
  }
  dequeue() {
    if (this.isEmpty()) {
      return null;
    }
    const removeElement = this.items.shift();
    return removeElement;
  }
  getFront() {
    if (this.isEmpty()) {
      return null;
    }
    return this.items[0];
  }
  getRear() {
    if (this.isEmpty()) {
      return null;
    }
    return this.items[this.items.length - 1];
  }
  isEmpty() {
    return this.items.length === 0;
  }
  getSize() {
    return this.items.length;
  }
}

// test code.

const queue = new Queue();
queue.enqueue(10);
queue.enqueue(30);
queue.enqueue(50);
queue.enqueue(20);
queue.enqueue(100);

console.log(" Front = " + queue.getFront() + " Rear= " + queue.getRear());
const deleted_item = queue.dequeue();
console.log("deleted item : ",deleted_item);
console.log(" Front = " + queue.getFront() + " Rear= " + queue.getRear());

const val = queue.isEmpty();
console.log("is empty : ",val);
const size = queue.getSize();
console.log("size of queue is : ",size);
