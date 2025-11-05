int reverseBits(int n) {
    int result = 0;
    for(int i = 0; i < 32; i++){
        int last_bit = n & 1;
        result <<= 1;
        result |= last_bit;
        n >>= 1;
    }
    return result;
    
}