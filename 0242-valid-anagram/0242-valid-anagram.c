#include <string.h>
int compare(const void* a, const void *b){
        int val1 = *(char*)a;
        int val2 = *(char*)b;

        return val1 - val2;
   }
bool isAnagram(char* s, char* t) {
    int lenS = strlen(s);
    int lenT = strlen(t);

    if (lenS != lenT) return false;

    qsort(s, lenS, sizeof(char), compare);
    qsort(t, lenT, sizeof(char), compare);

    return strcmp(s, t) == 0;
   

}