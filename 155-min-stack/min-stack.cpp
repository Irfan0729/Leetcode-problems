class MinStack {
public:
    class Node{
    public:
        int val;
        int min;
        Node* next;
        Node(int x, int m, Node* n){
            val = x;
            min = m;
            next = n;
        }
    };

    MinStack() {
        
    }
    
    void push(int val) {
        if(head == NULL)
            head = new Node(val, val, NULL);
        else
            head = new Node(val, val<head->min?val:head->min, head);
        return;
    }
    
    void pop() {
        head = head->next;
        return;
    }
    
    int top() {
        return head->val;
    }
    
    int getMin() {
        return head->min;
    }
    
private:
    Node* head = NULL;
};