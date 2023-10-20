// MinHeap을 class로 구현한 코드

class MinHeap {
  constructor() {
    this.heap = [];
  }

  getParentIndex(i) {
    return Math.floor((i - 1) / 2);
  }

  getLeftChildIndex(i) {
    return 2 * i + 1;
  }

  getRightChildIndex(i) {
    return 2 * i + 2;
  }

  hasParent(i) {
    return this.getParentIndex(i) >= 0;
  }

  hasLeftChild(i) {
    return this.getLeftChildIndex(i) < this.heap.length;
  }

  hasRightChild(i) {
    return this.getRightChildIndex(i) < this.heap.length;
  }

  parent(i) {
    return this.heap[this.getParentIndex(i)];
  }

  leftChild(i) {
    return this.heap[this.getLeftChildIndex(i)];
  }

  rightChild(i) {
    return this.heap[this.getRightChildIndex(i)];
  }

  swap(i, j) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }

  push(element) {
    this.heap.push(element);
    this.heapifyUp();
  }

  pop() {
    if (this.heap.length === 0) return null;
    const item = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.heapifyDown();
    return item;
  }

  heapifyUp() {
    let index = this.heap.length - 1;
    while (this.hasParent(index) && this.parent(index) > this.heap[index]) {
      const parentIndex = this.getParentIndex(index);
      this.swap(parentIndex, index);
      index = parentIndex;
    }
  }

  heapifyDown() {
    let index = 0;
    while (this.hasLeftChild(index)) {
      let smallerChildIndex = this.getLeftChildIndex(index);
      if (
        this.hasRightChild(index) &&
        this.rightChild(index) < this.leftChild(index)
      ) {
        smallerChildIndex = this.getRightChildIndex(index);
      }

      if (this.heap[index] < this.heap[smallerChildIndex]) {
        break;
      }

      this.swap(index, smallerChildIndex);
      index = smallerChildIndex;
    }
  }
}
