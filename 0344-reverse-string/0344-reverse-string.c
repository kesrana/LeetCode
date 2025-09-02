void reverseString(char* s, int sSize) {
    int first = 0;
    int last = sSize - 1;
    
    while(first < last){
        int temp = 0;
        temp = s[first];
        s[first] = s[last];
        s[last] = temp;
        
        first++;
        last--;
    }
    
}