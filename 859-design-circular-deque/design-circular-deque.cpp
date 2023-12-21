class MyCircularDeque {
public:
    MyCircularDeque (int k) : _size (k), _vec (k, -1) {}

    bool insertFront (int value) {
        if (isFull ()) return false;
        if (_head == 0) { _head += _size; _tail += _size; }
        _vec [_head-- % _size] = value;
        return true;
    }

    bool insertLast (int value) {
        if (isFull ()) return false;
        _vec [_tail++ % _size] = value;
        return true;
    }

    bool deleteFront () {
        if (isEmpty ()) return false;
        _vec [++_head % _size] = -1;
        return true;
    }

    bool deleteLast() {
        if (isEmpty ()) return false;
        _vec [--_tail % _size] = -1;
        return true;
    }

    int getFront() {
        if (isEmpty ()) return -1;
        return _vec [(_head + 1) % _size];
    }

    int getRear() {
        if (isEmpty ()) return -1;
        return _vec [(_tail - 1) % _size];
    }

    bool isEmpty() {
        return size() == 0;
    }

    bool isFull() {
        return size() == _size;
    }

    int size() {
        return _tail - (_head + 1);
    }

private:
    std::vector <int> _vec;
    const size_t _size;
    int _head = 0;
    int _tail = 1;
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */
