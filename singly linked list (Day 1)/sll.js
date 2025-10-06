class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class SinglyLinkedList {
  constructor() {
    this.head = null;
    this.size = 0;
  }
  insertData(data) {
    const newNode = new Node(data);
    if (!this.head) {
      this.head = newNode;
    } else {
      let curr = this.head;
      while (curr.next) {
        curr = curr.next;
      }
      curr.next = newNode;
    }
    this.size++;
  }
  insertAtTop(data) {
    const newNode = new Node(data);
    newNode.next = this.head;
    this.head = newNode;
    this.size++;
  }
  insertAtPos(data, index) {
    if (index < 0 || index > this.size) {
      console.error("Invalid Index");
      return false;
    }
    if (index === 0) {
      this.prepend(data);
      return true;
    }
    const newNode = new Node(data);
    let curr = this.head;
    let prev = null;
    let count = 0;

    while (count < index) {
      prev = curr;
      curr = curr.next;
      count++;
    }
    newNode.next = curr;
    prev.next = newNode;
    this.size++;
    return true;
  }
  removedAt(index) {
    if (index < 0 || index >= this.size) {
      console.error("Invalid index");
      return null;
    }
    let removedData;
    if (index === 0) {
      removedData = this.head.data;
      this.head = this.head.next;
    } else {
      let curr = this.head;
      let prev = null;
      let count = 0;
      while (count < index) {
        prev = curr;
        curr = curr.next;
        count++;
      }
      removedData = curr.data;
      prev.next = curr.next;
    }
    this.size--;
    return removedData;
  }
  isEmpty() {
    return this.size === 0;
  }
  getSize() {
    return this.size;
  }
  printList() {
    let curr = this.head;
    let result = "";
    while (curr) {
      result += curr.data + " -> ";
      curr = curr.next;
    }
    result += " null ";
    console.log(result);
  }
}

const list = new SinglyLinkedList();
list.insertData(10);
list.insertData(30);
list.insertData(50);
list.insertData(40);
list.insertData(20);
list.insertAtTop(60);
list.insertAtPos(70, 3);
list.printList();
const x = list.removedAt(4);
console.log(x);
list.printList();
