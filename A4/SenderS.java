import java.io.*;
import java.net.*;
import java.util.*;

class SenderS
{
	public static void main(String[] args) throws IOException
	{
		boolean err = false;
		InetAddress addr = InetAddress.getByName("Localhost");
		ServerSocket ss = new ServerSocket(5000);
		Socket server = new Socket();
		server = ss.accept();
		DataInputStream in = new DataInputStream(server.getInputStream());
		DataOutputStream out = new DataOutputStream(server.getOutputStream());
		Scanner scr = new Scanner(System.in);
		System.out.println("Enter String");
		String s = scr.next();
		char[] arr = s.toCharArray();
		int len = arr.length;
		out.writeInt(len);
		boolean[] b = new boolean[len];
		System.out.println("Enter m");
		int m = scr.nextInt();
		int window = (int)(Math.pow(2,(m-1)));
		System.out.println("Transmission type\n1. Error\n2. No Error");
		int ch = scr.nextInt();
		if(ch == 1)
			err = true;
		else
			err = false;
		int i = 0;
		for(int k = 0;k<len;k++)
		{
			b[k] = false;
		}
		 i = 0;
		while(i<len)
		{
			for(int j = 0;j<window && (i+j)<len;j++)
			{
				if(!b[i+j])
				{
					System.out.println("Sending frame "+arr[i+j]);
					if(err)
					{
						System.out.println("Enter type\n1. Error\n2. No Error");
						int q = scr.nextInt();
						if(q == 2)
						{
							out.writeInt(i+j);
							out.writeChar(arr[i+j]);
						}
					}
					else
					{
						out.writeInt(i+j);
						out.writeChar(arr[i+j]);
					}
				}
			}
			server.setSoTimeout(2000);
			boolean inc = true;
			for(int j = 0;j<window && (i+j)<len;j++)
			{
				try
				{
					int z = in.readInt();
					char c = in.readChar();
					System.out.println("Acknowledgement received for frame "+arr[z]);
					b[z] = true;
				}
				catch(Exception e)
				{
					int z = 0;
					while(b[i+z] && (i+z)<window)
					{
						z++;
					}
					if((i+z) < window)
					{
						System.out.println("Acknowledgement not received for frame "+arr[i+z]);
						System.out.println("Resending");
						j = window;
						inc = false;
					}
				}
			}
			while(inc && i<len)
			{
				if(b[i])
					i++;
				else
					break;
			}
			
		}
	}
}