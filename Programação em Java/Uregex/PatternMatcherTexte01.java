package Uregex;

import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PatternMatcherTexte01 {
    public static void main(String[] args) {
        // String regex = "$0";
        // String texto = "this/Rule={NE$0, MP$0}";

        String regex = "0";
        String texto = "NE$0, MP$0, MP$1, CE$0, CE$1";
        String textoNew = texto.replace("$", "");


        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(textoNew);

        System.out.println("texto:  "+textoNew);
        System.out.println("indice:  001");
        System.out.println("regex: "+regex);
        System.out.println("Posição encontradas:");
        
        ArrayList<String> regsLista = new ArrayList<String>();
        String regra= "";

        while (matcher.find()){
            System.out.print(matcher.start() + " ");
            System.out.println(textoNew.substring((matcher.start()-2), matcher.start()));
            regra = textoNew.substring((matcher.start()-2), matcher.start());
            regsLista.add(regra);
        }

        System.out.println(regsLista);

        String saidaJson = String.join(", ", regsLista);
 
		System.out.println("As do json: "+ saidaJson);

    }
}
