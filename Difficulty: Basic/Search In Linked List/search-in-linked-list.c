// User function Template for C

/*
struct Node
{
    int data;
    struct Node *next;

};
*/

int searchLinkedList(struct Node *head, int x) {
    struct Node* temp = head;
    while (temp != NULL) {
        if (temp->data == x) {
            return 1;
        }
        temp = temp->next;
    }
    return 0;
}