#include <stdio.h>
#include <stdlib.h>
struct Node
{
    int data;
    struct Node *link;
} *START = NULL;

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
};
void insert_at(struct Node *newNode, int index)
{
    if (index == 0)
    {
        // insert at beganning
        newNode->link = START;
        START = newNode;
        return;
    }
    else if (index == 2)
    {
        // insert at last
        if (START)
        {
            struct Node *S = START;
            while (S->link != NULL)
            {
                S = S->link;
            }
            S->link = newNode;
        }
        else
        {
            START = newNode;
        }
    }
    else
    {
        // any index
        // insert at last
        if (START == NULL)
        {
            printf("ll is empty no list to traverse");
            return;
        }
        else
        {
            struct Node *S = START;
            int i = 0;
            while (S != NULL && i < index - 1)
            {
                S = S->link;
                i += 1;
            }
            if (S == NULL)
            {
                printf("error : null pointer refrence");
            }
            else
            {
                newNode->link = S->link;
                S->link = newNode;
            }
        }
    };
};
void traverse()
{
    struct Node *ptr = START;
    while (ptr != NULL)
    {
        printf("%d", ptr->data);
        ptr = ptr->link;
    }
    printf("\n");
};

int main()
{
    int a[] = {1, 2, 3, 4, 5};
    int sizeArray = sizeof(a) / sizeof(int);
    // create one node
    START = createNode(a[0]);
    struct Node *ptr = START;
    for (int i = 1; i < sizeArray; i++)
    {
        struct Node *temp = createNode(a[i]);
        ptr->link = temp;
        ptr = temp;
    }

    traverse();
    insert_at(createNode(10), 0);
    traverse();
    insert_at(createNode(11), 2);
    traverse();
    insert_at(createNode(88), 3);
    traverse();

    return 0;
}
