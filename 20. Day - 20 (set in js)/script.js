
class CustomSet{
    constructor(){
        this.items=new Map();
    }
    add(element){
        if(this.items.has(element)){
            return false;
        }
        this.items.set(element,element);
        return true;
    }
    has(element){
        return this.items.has(element);
    }
    remove(element){
        return this.items.delete(element);
    }
    size(){
        return this.items.size;
    }
    values(){
        return [...this.items.keys()];
    }
    union(otherSet){
        const unionSet=new CustomSet();
        this.values().forEach(value =>unionSet.add(value));

        otherSet.values().forEach(value => unionSet.add(value));
        return unionSet;
    }
    intersection(otherSet){
        const intersectionSet=new CustomSet();

        const smallerSet=this.size() <otherSet.size()? this:otherSet;
        const largerSet=this.size()<otherSet.size()?otherSet:this;

        smallerSet.values().forEach( value =>{
            if(largerSet.has(value)){
                intersectionSet.add(value);
            }
        });
        return intersectionSet;
    }
}

const setA = new CustomSet();

setA.add(2);
setA.add(4);
setA.add(6);
setA.add(3);
setA.add(7);
setA.add(2);
setA.add(4);
setA.add(10);
setA.add(20);

const setB = new CustomSet();
setB.add(7);
setB.add(2);
setB.add(4);
setB.add(10);
setB.add(20);

console.log("seta : ", setA);
console.log("setb : ", setB);

const setc = setA.union(setB);
console.log("setc : ", setc);

setd = setA.intersection(setB);

console.log("setd : ", setd);
