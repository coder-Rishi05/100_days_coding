### Sets in js

// custom set in js

// class CustomSet {
//   constructor() {
//     this.items = new Map();
//   }
//   add(ele) {
//     if (this.items.has(ele)) {
//       return false;
//     }
//     this.items.set(ele, ele);
//   }
//   hasItem(ele) {
//     return this.items.has(ele);
//   }
//   removeElement(ele) {
//     return this.items.delete(ele);
//   }
//   size() {
//     return this.items.size;
//   }

//   values() {
//     return [...this.items.keys()];
//   }

//   union(otherSet) {
//     const unionSet = new CustomSet();

//     this.values().forEach((value) => unionSet.add(value));

//     otherSet.values().forEach((value) => unionSet.add(value));
//     return unionSet;
//   }

//   intersection(otherSet) {
//     const intersectionSet = new CustomSet();

//     const smallerSet = this.size() < otherSet.size() ? this : otherSet;
//     const largerSet = this.size() < otherSet.size() ? otherSet : this;

//     smallerSet.values().forEach((value) => {
//       if (largerSet.has(value)) {
//         intersectionSet.add(value);
//       }
//     });
//     return intersectionSet;
//   }
// }
