/*Stop and wait protocol*/

#include<stdio.h>

int main(){
    int framesize,sent=0,ack,i;
    printf("Enter number of frames : ");
    scanf("%d",&framesize);
    while(1){
        for(i=0;i<framesize;i++){
            printf("from %d has been transmitted.\n",sent);
            sent++;
            if(sent==framesize)
            break;
        }
        printf("\nPlease enter the last acknowledgement recieved.\n");
        scanf("%d",&ack);
        if(ack==framesize)
        break;
        else
        sent=ack;
    }
    return 0;
}