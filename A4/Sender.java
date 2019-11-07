import java.net.*;
import java.util.*;
import java.io.*;

class Sender
{
	public static void main(String[] args) throws IOException
	{
			InetAddress addr = InetAddress.getByName("Localhost");
			ServerSocket ss = new ServerSocket(5000);
			Socket server = new Socket();
			server = ss.accept();
			DataInputStream in = new DataInputStream(server.getInputStream());
			DataOutputStream out = new DataOutputStream(server.getOutputStream());
			Scanner scr = new Scanner(System.in);

			boolean err = false;
			System.out.println("Enter string\n");
			String s = scr.next();
			char[] arr= s.toCharArray();
			int len = arr.length;
			out.writeInt(len);
			System.out.println("Enter m\n");
			int m = scr.nextInt();
			int window = (int)(Math.pow(2,m) - 1);
			System.out.println("Transmission type\n1. Error\n2. No Error");
			int ch = scr.nextInt();
			if(ch == 1)
				err = true;
			else
				err = false;
			int i = 0;
			while(i<len)
			{
				int cnt = 0;
				for(int j = 0;j<window && (i+j)<len;j++)
				{
					if(err)
					{
						System.out.println("Sending frame "+arr[i+j]+"\n");
						System.out.println("1. Error\n2. No Error\n");
						int z = scr.nextInt();
						if(z == 2)
						{
							out.writeInt((i+j));
							out.writeChar(arr[(i+j)]);
						}
					}
					else
					{
						out.writeInt((i+j));
						out.writeChar(arr[(i+j)]);
					}
				}
				server.setSoTimeout(3000);
				for(int j = 0;j<window && (i+j)<len;j++)
				{
					try
					{
						int rec = in.readInt();
						char c = in.readChar();
						if(rec == (i+j))
						{
							System.out.println("Acknowledgement received for "+c+"\n");
							cnt++;
						}
						else
						{
							Thread.sleep(500);
						}
					}
					catch(Exception e)
					{
						if((i+cnt) < window)
						{
							System.out.println("Acknowledgement not received for "+arr[i+cnt]);
							System.out.println("\nResending...\n");
							j = window;
						}
					}
				}
				i = i + cnt;
			}
			server.close();
			in.close();
			out.close();
	}
}