int hammingDistance(int x, int y) {
    //counter
    int result = 0;
    //xor the values together
    int xor_val = x^y;

    while(xor_val > 0){
        int last_bit = xor_val & 1;
        if(last_bit == 1){
            result += 1;
        }
        xor_val >>= 1;
    }

    return result;
}