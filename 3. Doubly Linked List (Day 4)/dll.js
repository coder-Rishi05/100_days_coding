class Node {
  constructor(data, prev = null, next = null) {
    this.data = data;
    this.prev = prev;
    this.next = next;
  }
}

class dll {
  constructor() {
    this.head = null;
    this.size = 0;
    this.tail = null;
  }

  append(data) {
    const newNode = new Node(data, this.tail);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.size++;
  }
  append(data) {
    const newNode = new Node(data, this.tail);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }

    this.size++;
  }
  prepend(data) {
    const newNode = new Node(data, null, this.head);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.head.prev = newNode;
      this.head = newNode;
    }
    this.size++;
  }
  insertAt(data, index) {
    if (index < 0 || index > this.size) {
      console.log("Invalid index");
      return false;
    }
    if (index === 0) {
      this.prepend(data);
      return true;
    }
    if (index === this.size) {
      this.append(data);
      return true;
    }
    let cur = this.head;
    let count = 0;
    while (count < index) {
      cur = cur.next;
      count++;
    }
    const newNode = new Node(data, cur.prev, cur);
    cur.prev = newNode;
    this.size++;
    return true;
  }
  removeAt(index) {
    if (index < 0 || index >= this.size) {
      console.log("invalid index");
      return null;
    }
    let cur = this.head;
    let removeData;
    if (index === 0) {
      removeData = this.data;
      this.head = this.head.next;
      if (this.head) {
        this.head.prev = null;
      } else {
        this.tail = null;
      }
    } else if (index === this.size - 1) {
      cur = this.tail;
      removeData = cur.data;
      this.tail = cur.prev;
      this.tail.next = null;
    } else {
      let count = 0;
      cur = this.head;
      while (count < index) {
        cur = cur.next;
        count++;
      }
      removeData = cur.data;
      cur.prev.next = cur.next;
      cur.next.prev = cur.prev;
    }
    this.size--;
    return removeData;
  }

  isEmpty() {
    return this.size === 0;
  }
  getSize() {
    return this.size;
  }

  printListForward() {
    let cur = this.head;
    let res = "";
    while (cur) {
      res += cur.data + " <-> ";
      cur = cur.next;
    }
    res += " null ";
    console.log(res);
  }
  printListBackward() {
    let cur = this.tail;
    let res = "";
    while (cur) {
      res += cur.data + " <-> ";
      cur = cur.prev;
    }
    res += "null";
    console.log(res);
  }
}

// test code:

const list = new dll();

list.append(10);
list.append(30);
list.append(50);
list.append(80);
list.append(10);
list.append(20);
list.insertAt(90, 4);
list.printListBackward();
list.printListForward();
