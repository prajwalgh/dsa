#include <stdio.h>
#include <stdlib.h>
struct Node
{
    int data;
    struct Node *link;
} *START;

struct Node *createNode(int d)
{
    struct Node *temp = (struct Node *)malloc(sizeof(struct Node));
    if (temp == NULL)
    {
        exit(1);
    }
    temp->data = d;
    temp->link = NULL;
    return temp;
}

int main()
{
    int a[] = {1, 2, 3, 4, 5};
    int sizeArray = sizeof(a) / sizeof(int);
    // create one node
    START = (struct Node *)malloc(sizeof(struct Node));
    START->data = a[0];
    struct Node *ptr = START;
    for (int i = 1; i < sizeArray; i++)
    {
        struct Node *temp = createNode(a[i]);
        ptr->link = temp;
        ptr = temp;
    }
    ptr = START;
    while (ptr != NULL)
    {
        printf("%d", ptr->data);
        ptr = ptr->link;
    }
    return 0;
}
