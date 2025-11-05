bool isPowerOfTwo(int n) {
    int count = 0;
    if(n <= 0){
        return false;
    }
    while(n > 0){
        int last_bit = n & 1;
        count += last_bit;
        if(count > 1){
            return false;
        }
        n >>= 1;
    }
    return true;
    
}