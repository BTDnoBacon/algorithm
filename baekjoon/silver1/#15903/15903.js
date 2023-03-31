let input = require('fs').readFileSync('input.txt').toString().split('\n')
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n')


class Heap {
    constructor() {
        this.heap = []
    }

    getLeftChildIndex = (parentIndex) => parentIndex * 2 + 1
    getRightChildIndex = (parentIndex) => parentIndex * 2 + 2
    getParentIndex = (childIndex) => Math.floor((childIndex-1) / 2)

    peek = () => this.heap[0]

    insert = (key, value) => {
        const node = {key, value};
        this.heap.push(node)
        this.heapifyUp()
    }

    heapifyUp = () => {
        let index = this.heap.length - 1
        const lastInsertedNode = this.heap[index]

        while (index > 0) {
            const parentIndex = this.getParentIndex(index)

            if (this.heap[parentIndex].key > lastInsertedNode.key) {
                this.heap[index] = this.heap[parentIndex]
                index = parentIndex
            } else break
        }

        this.heap[index] = lastInsertedNode
    }

    remove = () => {
        const count = this.heap.length
        const rootNode = this.heap[0]
    
        if (count <= 0) return undefined
        if (count === 1) this.heap = []
        else {
          this.heap[0] = this.heap.pop() // 끝에 있는 노드를 부모로 만들고
          this.heapifyDown() // 다시 min heap 의 형태를 갖추도록 한다.
        }
    
        return rootNode
    }

    heapifyDown = () => {
        let index = 0
        const count = this.heap.length
        const rootNode = this.heap[index]
    
        // 계속해서 left child 가 있을 때 까지 검사한다.
        while (this.getLeftChildIndex(index) < count) {
          const leftChildIndex = this.getLeftChildIndex(index)
          const rightChildIndex = this.getRightChildIndex(index)
    
          // 왼쪽, 오른쪽 중에 더 작은 노드를 찾는다
          // rightChild 가 있다면 key의 값을 비교해서 더 작은 값을 찾는다.
          // 없다면 leftChild 가 더 작은 값을 가지는 인덱스가 된다.
          const smallerChildIndex =
            rightChildIndex < count && this.heap[rightChildIndex].key < this.heap[leftChildIndex].key
              ? rightChildIndex
              : leftChildIndex
    
          // 자식 노드의 키 값이 루트노드보다 작다면 위로 끌어올린다.
          if (this.heap[smallerChildIndex].key <= rootNode.key) {
            this.heap[index] = this.heap[smallerChildIndex]
            index = smallerChildIndex
          } else break
        }
    
        this.heap[index] = rootNode
      }
}

class PriorityQueue extends Heap {
    constructor() {
      super()
    }
  
    enqueue = (priority, value) => this.insert(priority, value)
    dequeue = () => this.remove()
    isEmpty = () => this.heap.length <= 0
  }

// console.log(input)

const [n, m] = input[0].split(' ').map(item => +item)
const arr = input[1].split(' ').map(item => +item)

const HeapQueue = new PriorityQueue()
arr.forEach(item => HeapQueue.enqueue((0, item)))
for (let i=0; i < m; i++) {
    let a = HeapQueue.dequeue().key
    // console.log(HeapQueue.heap)

    // console.log(a)
    let b = HeapQueue.dequeue().key
    let temp = a+b
    HeapQueue.enqueue((0, temp))
    HeapQueue.enqueue((0, temp))

}
console.log(HeapQueue.heap.reduce((acc, cur) => acc + cur.key, 0))