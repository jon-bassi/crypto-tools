/*
 * created by jon-bassi 2016-2-1
 */

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import java.security.Key;

public class AES
{

    public static void main(String[] args) throws Exception
    {
        // should read from file and encrypt contents
        if (args.length < 1)
            System.exit(0);

        String toEncrypt = "";
        for (String s : args)
            toEncrypt += s + " ";
        byte[] plainText = toEncrypt.getBytes("UTF8");
        System.out.println("Plain text:" + toEncrypt);

        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(256);

        Key key = keyGen.generateKey();

        Cipher cipher = Cipher.getInstance("AES");
        System.out.println("\n" + cipher.getProvider().getInfo());

        cipher.init(Cipher.ENCRYPT_MODE, key);
        byte[] cipherText = cipher.doFinal(plainText);
        System.out.println("\nNew Text: " + new String(cipherText, "UTF8"));

        cipher.init(Cipher.DECRYPT_MODE, key);
        byte[] newPlainText = cipher.doFinal(cipherText);
        System.out.println("\nPlain text: " + new String(newPlainText, "UTF8"));
    }
}
