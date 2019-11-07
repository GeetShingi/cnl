import java.io.*;
import java.net.*;
import java.util.*;

class Receiver
{
	public static void main(String[] args) throws IOException
	{
			InetAddress addr = InetAddress.getByName("Localhost");
			Socket client = new Socket(addr,5000);
			DataInputStream in =new DataInputStream(client.getInputStream());
			DataOutputStream out = new DataOutputStream(client.getOutputStream());
			Scanner scr = new Scanner(System.in);
			int len = in.readInt();
			char[] arr = new char[len];
			int i = 0;
			while(i < len)
			{
				int rec = in.readInt();
				char c = in.readChar();
				if(rec == i)
				{
					arr[rec] = c;
					out.writeInt(rec);
					out.writeChar(arr[rec]);
					System.out.println("Acknowledgement sent for "+arr[rec]+"\n");
					i++;
				}
			}
			client.close();
			in.close();
			out.close();
	}
}