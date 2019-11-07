#include<sys/types.h>
#include<sys/socket.h>
#include<iostream>
#include<netinet/in.h> 
#include<unistd.h>
#include<string.h> 
#include<strings.h>
#include <arpa/inet.h>
#include<math.h>

using namespace std;

int main(int argc, char const *argv[])
{
	int sockfd,con,sin_size;
	int a,b;
	int choice;
	double result;
	FILE *fp;
	char ch;
	if((sockfd=socket(AF_INET,SOCK_STREAM,0))>0)
	{
		cout<<"Socket created sucessfully"<<endl;
	}
	struct sockaddr_in servaddr;
	servaddr.sin_family = AF_INET;
	servaddr.sin_addr.s_addr = inet_addr("127.0.0.1");
	servaddr.sin_port = 6666;
	sin_size = sizeof(servaddr);

	if((con = connect(sockfd,(struct sockaddr *)&servaddr, sin_size)) == 0)
	{
		cout<<"Connected sucessfully"<<endl;
	}

	write(sockfd,"Hello",sizeof("Hello"));
	fp = fopen("b.txt","wb");
	read(sockfd,&ch,sizeof(ch));
	while(ch != EOF)
	{
		fputc(ch,fp);
		read(sockfd,&ch,sizeof(ch));
	}
	printf("FILE RECEIVED\n");
	fclose(fp);
	cout<<"Enter two operands\n";
	cin>>a>>b;
	printf("Enter opeartion\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n");
	cin>>choice;
	write(sockfd,&a,sizeof(a));
	write(sockfd,&b,sizeof(b));
	write(sockfd,&choice,sizeof(choice));
	read(sockfd,&result,sizeof(result));
	cout<<"Result : "<<result<<endl;
	close(sockfd);
	return 0;
}