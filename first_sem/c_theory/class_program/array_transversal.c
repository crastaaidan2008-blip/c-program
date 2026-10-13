#include<stdio.h>
int main(){
    int arraySize=read_array_size() //calling method & stores retuurned value
    validate-array_Size(arraySize); ////passing 'arraysize'; int array_size=arraysize

    if (isvalid ==0){

    }
}
//reads array SIZE from kb 
int read_array_size(){
    int size;   //local variable 
    printf("enter the array size[.4]:");
    scanf("%d",&size);
    return size;
}

int validate_array_size(int array_size){
    if(array_size >4){
        return 1;

    }
    return 0;
}