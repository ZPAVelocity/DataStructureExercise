#include <cstdlib> // system("cls");
#include <iostream>
#include "SeqList.h"

using namespace std;

int main()
{
    seqList l;

    initList(&l);

    elemType element;
    int seat;

    cout << "insert" << endl;
    for (int i = 0; i < 10; i++)
    {
        cin >> seat >> element;
        system("cls");
        if (listInsert(&l, seat, element) == false)
            cout << "Error" << endl;
        showList(&l);
    }

    cout << "delete" << endl;
    for (int i = 0; i < 10; i++)
    {
        cin >> seat;
        system("cls");
        if (listDelete(&l, seat) == false)
            cout << "Error" << endl;
        showList(&l);
    }
    return 0;
}

bool listExist(seqList *list)
{
    if (list == NULL)
        return false;
    else
        return true;
}
bool initList(seqList *list)
{
    if (!listExist(list))
        return false;
    list->length = 0;
    return true;
}
bool clearList(seqList *list)
{
    if (!listExist(list))
        return false;
    list->length = 0;
    return true;
}
bool listEmpty(seqList *list)
{
    if (listExist(list))
        return false;
    if (list->length == 0)
        return true;
    else
        return false;
}
int listLength(seqList *list)
{
    return list->length;
}
elemType getElem(seqList *list, int seat)
{
    return list->element[seat];
}
int locateElem(seqList *list, elemType element)
{
    for (int i = 0; i < list->length; i++)
    {
        if (list->element[i] == element)
            return i;
    }
}
elemType priorElem(seqList *list, int seat)
{
    return list->element[seat + 1];
}
elemType nextElem(seqList *list, int seat)
{
    return list->element[seat - 1];
}
bool listInsert(seqList *list, int seat, elemType element)
{
    if (!listExist(list) ||
        list->length >= MAX_SIZE ||
        seat > list->length ||
        seat < 0)
        return false;

    for (int i = list->length; i >= seat; i--)
        list->element[i + 1] = list->element[i];
    list->length++;
    list->element[seat] = element;
    return true;
}
bool listDelete(seqList *list, int seat)
{
    if (!listExist(list) ||
        list->length <= 0 ||
        seat >= list->length ||
        seat < 0)
        return false;

    for (int i = seat + 1; i < list->length; i++)
        list->element[i - 1] = list->element[i];
    list->length--;
    return true;
}

bool showList(seqList *list)
{
    if (!listExist(list))
        return false;
    cout << "List: " << endl;

    for (int i = 0; i < list->length; i++)
        cout << "[" << i << "]"
             << "\t";
    cout << endl;

    for (int i = 0; i < list->length; i++)
        cout << list->element[i] << "\t";
    cout << endl;
    return true;
}