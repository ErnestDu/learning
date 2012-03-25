#include <stdio.h>
typedef int ElemType;

typedef struct LinkNode {
	ElemType data;
	struct LinkNode *next;
}LinkNode, *LinkList;

// initialize link list
LinkListInit()
{
	LinkNode *L;
	L = (LinkNode *)malloc(sizeof(LinkNode));	// 
	if (L == NULL)
		printf("Memory allocation failed.\n");
	L->next = NULL;
}


// create link list, insert new element to head
LinkList LinkListCreateH()
{
	LinkNode *L;
	L = (LinkNode *)malloc(sizeof(LinkNode));
	L->next = NULL;
	
	ElemType x;
	while (scanf("%d", &x) != EOF) {
		LinkNode *p;
		p = (LinkNode *)malloc(sizeof(LinkNode));
		p->data = x;
		p->next = L->next;
		L->next = p;
	}
	LinkNode *p;
	p = L;
	p = p -> next;
	while (p != NULL) {
		printf("%d ", p->data);
		p = p->next;
	}
	printf("\n");
	return L;
}

// create link list, insert new element to tail
LinkList LinkListCreateT()
{
	LinkNode *L;
	L = (LinkNode *)malloc(sizeof(LinkNode));
	LinkNode *tail;
	L->next = NULL;
	ElemType x;
	while (scanf("%d", &x) != EOF) {
		LinkNode *p;
		p = (LinkNode *)malloc(sizeof(LinkNode));
		p->data = x;
		p = tail;
		L->next = p;
	}
	LinkNode *p;
	p = L;
	p = p->next;
	while (p != NULL) {
		printf("%d", p->data);
		p = p->next;
	}
	printf("\n");
	return L;
}

//void LinkListTraverse(LinkList L)
//{
//	LinkNode *p;
//	p = L;
//	while (p->next != NULL) {
//		printf("%d ", p->data);
//		p = p->next;
//	}
//	printf("\n");
//}
main()
{
	LinkList L;
//	LinkListCreateH();
	LinkListCreateT();
}
