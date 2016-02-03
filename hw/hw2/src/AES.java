/*
 * created by jon-bassi 2016-2-1
 */

import com.sun.org.apache.xerces.internal.impl.dv.util.Base64;

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.security.Key;
import java.util.Scanner;

public class AES
{

    public static void main(String[] args) throws Exception
    {
        // should read from file and encrypt contents
        String plaintextFile = "";
        if (args.length < 1)
            plaintextFile = "plaintext.txt";
        else
            plaintextFile = args[0];

        // read in plaintext
        System.out.println("Reading from " + plaintextFile);

        Scanner plaintextReader = new Scanner(new File(plaintextFile));
        String toEncrypt = "";
        while (plaintextReader.hasNext())
        {
            toEncrypt += plaintextReader.nextLine() + "\n";
        }
        plaintextReader.close();

        byte[] plainText = toEncrypt.getBytes("UTF8");

        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(256);
        Key key = keyGen.generateKey();
        Cipher cipher = Cipher.getInstance("AES");

        cipher.init(Cipher.ENCRYPT_MODE, key);
        byte[] cipherText = cipher.doFinal(plainText);

        BufferedWriter ciphertextWriter = new BufferedWriter(new FileWriter("ciphertext.txt"));
        ciphertextWriter.write(Base64.encode(cipherText));
        ciphertextWriter.close();

        System.out.println("Cipher text written to ciphertext.txt in base 64 encoding");

        Scanner ciphertextReader = new Scanner(new File("ciphertext.txt"));
        String toDecrypt = "";
        while (ciphertextReader.hasNext())
        {
            toDecrypt += ciphertextReader.nextLine() + "\n";
        }
        ciphertextReader.close();
        cipherText = Base64.decode(toDecrypt);

        cipher.init(Cipher.DECRYPT_MODE, key);
        byte[] newPlainText = cipher.doFinal(cipherText);

        BufferedWriter plaintextWriter = new BufferedWriter(new FileWriter("newPlaintext.txt"));
        plaintextWriter.write(new String(newPlainText, "UTF8"));
        plaintextWriter.close();

        System.out.println("Plaintext written to newPlaintext.txt in UTF8");
    }
}
