#include<stdio.h>
// get_array_sum() define
//int number[]=mynumber
int get_array_sum(int number[]){
    int sum=0;
    for (int i=0;i<5;i++){
        sum=sum + number[i];


    }
    return sum;

}



int main (){
    int mynumber[5];
    // array initialisation
    for(int i=0;i<5;i++){
        printf("enter the %d number:",i+1 );
      scanf("%d", &mynumber[i]);
    }
    // calculate the sum and returns sum 
    int sum_array=get_array_sum(mynumber);
    printf("the sum is %d",sum_array);
}    