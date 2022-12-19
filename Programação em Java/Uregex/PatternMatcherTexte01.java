package Uregex;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PatternMatcherTexte01 {
    public static void main(String[] args) {
        // String regex = "$0";
        // String texto = "this/Rule={NE$0, MP$0}";

        String regex = "0";
        String texto = "NE$0, MP$0, MP$1";
        String textoNew = texto.replace("$", "");


        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(textoNew);

        System.out.println("texto:  "+textoNew);
        System.out.println("indice:  001");
        System.out.println("regex: "+regex);
        System.out.println("Posição encontradas:");
        
        while (matcher.find()){
            System.out.print(matcher.start() + " ");
        }

    }
}
