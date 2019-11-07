#include<sys/types.h>
#include<sys/socket.h>
#include<stdio.h>
#include<netinet/in.h> 
#include<unistd.h>
#include<string.h> 
#include<strings.h>
#include <arpa/inet.h>
#include<math.h>

int main(int argc, char const *argv[])
{
	char msg[25];
	char ch;
	FILE *fp;
	int a,b,choice;
	double result;
	int sockfd,sin_size,connfd;
	if((sockfd = socket(AF_INET,SOCK_STREAM,0)) > 0)
	{
		printf("Socket created successfully\n");
	}
	struct sockaddr_in servaddr;
	struct sockaddr_in clientaddr;

	servaddr.sin_family = AF_INET;
	servaddr.sin_addr.s_addr = inet_addr("127.0.0.1");
	servaddr.sin_port = 6666;
	if((bind(sockfd,(struct sockaddr *)&servaddr,sizeof(servaddr))) == 0)
	{
		printf("Bind Successfull\n");
	}
	if((listen(sockfd,5)) == 0)
	{
		printf("Listen Successfull\n");
	}
	sin_size = sizeof(clientaddr);
	if((connfd=accept(sockfd,(struct sockaddr *)&clientaddr,&sin_size))>0)
	{
		printf("Accept Successfull\n");
	}
	read(connfd,&msg,sizeof(msg));
	printf("Msg : %s\n",&msg);

	fp = fopen("a.txt","r");
	ch = fgetc(fp);
	while(ch != EOF)
	{
		write(connfd,&ch,sizeof(ch));
		ch = fgetc(fp);
	}
	write(connfd,&ch,sizeof(ch));
	printf("FILE SENT\n");
	fclose(fp);
	read(connfd,&a,sizeof(a));
	read(connfd,&b,sizeof(b));
	read(connfd,&choice,sizeof(choice));
	switch(choice)
	{
		case 1:
		result = a+b;
		break;
		case 2:
		result = a-b;
		break;
		case 3:
		result = a*b;
		break;
		case 4:
		result = a/b;
		break;
	}
	write(connfd,&result,sizeof(result));
	close(sockfd);
	close(connfd);

	return 0;
}