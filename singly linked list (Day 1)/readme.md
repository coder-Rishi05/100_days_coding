# 🚀 Singly Linked List in JavaScript 


Yeh program ek **Singly Linked List** ka implementation hai JavaScript me.  
Linked List ek **data structure** hai jisme har element (node) ke andar **data** hota hai aur ek **pointer (next)** hota hai jo next node ki taraf point karta hai.

---

## 📦 Classes Used

### 1️⃣ `class Node`
Yeh class ek single node ko represent karti hai.

```js
class Node {
  constructor(data) {
    this.data = data;  // node ke andar store hone wala data
    this.next = null;  // next node ka reference (default null)
  }
}

    ```    Har node ke do parts hote hain:

    data: actual value

    next: next node ka address (ya reference)
    ```

2️⃣ class SinglyLinkedList

    Yeh class poori linked list ko represent karti hai. Iske andar hum different operations define karte hain jaise insert, remove, print, etc.

        class SinglyLinkedList {
    constructor() {
        this.head = null; // list ka first node
        this.size = 0;    // total number of nodes
    }
    }

🧩 Functions (Methods)
🔹 insertData(data)

List ke end me ek naya node add karta hai.

Steps:

    Naya node banate hain (new Node(data)).

    Agar list empty hai (!this.head) to head usi new node ko banate hain.

    Agar list me kuch pehle se hai, to last node tak jaake new node attach kar dete hain.

    Size increment karte hain.


🔹 insertAtTop(data)

List ke starting me node add karta hai (head ke pehle).

Steps:

Naya node banate hain.

Uska next current head ko point karega.

head ko new node se replace kar dete hain.

🔹 removedAt(index)

List se ek node delete karta hai given index par.

Steps:

Index check karta hai valid hai ya nahi.

Agar index 0 hai, to head ko next node se replace karta hai.

Warna previous node aur current node ko track karke next pointer update karta hai.

Deleted data return karta hai.

🔹 isEmpty()

Return karta hai true agar list me koi node nahi hai, warna false.

🔹 getSize()

Return karta hai list ke total elements (size).


🔹 printList()

Poore list ko traverse karta hai aur data -> data -> null format me print karta hai.

```const list = new SinglyLinkedList();
list.insertData(10);
list.insertData(30);
list.insertData(50);
list.insertData(40);
list.insertData(20);
list.insertAtTop(60);
list.insertAtPos(70, 3);

list.printList();
// Output: 60 -> 10 -> 30 -> 70 -> 50 -> 40 -> 20 -> null

const x = list.removedAt(4);
console.log(x); // Output: 50

list.printList();
// Output: 60 -> 10 -> 30 -> 70 -> 40 -> 20 -> null

```