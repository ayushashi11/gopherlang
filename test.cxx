#include<iostream>
int test(int a=0){
    if(a>=0)
        return a;
    else
        return -a;
}
int main(){
    std::cout<<test();
    std::cout<<test(9);
    std::cout<<test(-9);
    return 0;
}