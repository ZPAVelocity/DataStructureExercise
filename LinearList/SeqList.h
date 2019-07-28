typedef int elemType;

#ifndef __SEQ_LIST_H__
#define __SEQ_LIST_H__
#define MAX_SIZE 100

typedef struct
{
    elemType element[MAX_SIZE];
    int length;
} seqList;

bool listExist(seqList *list);
bool initList(seqList *list);
bool clearList(seqList *list);
bool listEmpty(seqList *list);
int listLength(seqList *list);
elemType getElem(seqList *list, int seat);
int locateElem(seqList *list, elemType element);
elemType priorElem(seqList *list, int seat);
elemType nextElem(seqList *list, int seat);
bool listInsert(seqList *list, int seat, elemType element);
bool listDelete(seqList *list, int seat);
bool showList(seqList *list);

#endif