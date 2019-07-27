typedef int elementType;

#ifndef __SEQ_LIST_H__
#define __SEQ_LIST_H__

#include "LinearList.h"
#define MAX_SIZE 100
#define LIST_INCREMENT 10


typedef struct
{
    elementType element[MAX_SIZE];
    int length;
} seqList;

bool listExist(seqList *list);
bool initList(seqList *list);
bool clearList(seqList *list);
bool listEmpty(seqList *list);
int listLength(seqList *list);
elementType getElem(seqList *list, int seat);
int locateElem(seqList *list, elementType element);
elementType priorElem(seqList *list, int seat);
elementType nextElem(seqList *list, int seat);
bool listInsert(seqList *list, int seat, elementType element);
bool listDelete(seqList *list, int seat);
bool showList(seqList *list);

#endif