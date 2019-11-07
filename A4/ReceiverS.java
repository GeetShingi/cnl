import java.io.*;
import java.net.*;
import java.util.*;

class ReceiverS
{
	public static void main(String[] args) throws IOException
	{
		InetAddress addr = InetAddress.getByName("Localhost");
		Socket client = new Socket(addr,5000);
		DataInputStream in = new DataInputStream(client.getInputStream());
		DataOutputStream out = new DataOutputStream(client.getOutputStream());
		Scanner scr = new Scanner(System.in);
		int len = in.readInt();
		char[] arr = new char[len];
		int i = 0;
		while(i < len)
		{
			int z = in.readInt();
			char c = in.readChar();
			if(i == z || true)
			{
				arr[z] = c;
				System.out.println("Received frame "+arr[z]);
				out.writeInt(z);
				out.writeChar(arr[z]);
				System.out.println("Acknowledgement sent for "+arr[z]+"\n");
				i++;
			}
		}
		client.close();
		in.close();
		out.close();
	}
}