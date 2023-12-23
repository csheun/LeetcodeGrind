class MinStack {
private:
    class Node {
    public:
        int value;
        int min;
        Node* next;

        // Constructor using member initializer list
        Node(int val, int minimum, Node* nextNode) : value(val), min(minimum), next(nextNode) {}
    };

    Node* head; // Pointer to the top of the stack

public:
    MinStack() : head(nullptr) {}

    void push(int val) {
        if (head == nullptr) {
            head = new Node(val, val, nullptr);
        } else {
            head = new Node(val, std::min(val, head->min), head);
        }
    }

    void pop() {
        if (head != nullptr) {
            Node* temp = head;
            head = head->next;
            delete temp;
        }
    }

    int top() {
        if (head != nullptr) {
            return head->value;
        }
        // Handle the case when the stack is empty
        return -1; // You can choose a suitable default value
    }

    int getMin() {
        if (head != nullptr) {
            return head->min;
        }
        // Handle the case when the stack is empty
        return -1; // You can choose a suitable default value
    }
};