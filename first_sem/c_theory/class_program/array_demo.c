//Pgm to store and display 5 sub_marks 
//For student  
#include<stdio.h>
int main(){            //integer array of size 5
    int sub_marks[5];
    int my_marks[5];   //declares an array  'sub_marks'
    //with SIZE 5 of 'int' type 
    //storing data/ array initialization - array_name[index]=data/value
    //stores '80' in an array position whose inde  //static array initialization
    //fetch the first array element from 'sub_mark'
    //dynamic initialisation of 'my_marks'
    for (int i = 0; i < 5; i++)
    {
        printf("enter marks %d:",1+i);
        scanf("%d",&my_marks[i]);
    }
    printf("first subject marks:%d\n",my_marks[0]);
    printf("second subject marks:%d\n",my_marks[1]);
    printf("third subject marks:%d\n",my_marks[2]);    
    printf("fourth subject marks:%d\n",my_marks[3]);
    printf("fifth subject marks:%d\n",my_marks[4]);
}