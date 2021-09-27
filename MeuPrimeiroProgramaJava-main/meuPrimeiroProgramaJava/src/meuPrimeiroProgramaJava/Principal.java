/**
 * Este é o meu primeiro programa em java
 * 1) Que um programa Java é contruido dendo de um projeto Java.
 * 2) Todo programa Java deve ter uma classe com um método main.
 * 3) Como exibir informações no terminal (console) do Java.
 * 4) Como Ler uma string do terminal (Console) do Java
 */
package meuPrimeiroProgramaJava;
import java.util.Scanner;

/**
 * @author mathe
 *Data: 03/02/2021
 */
public class Principal { // Classe que contem o metodo principal.
	public static void main(String[] args) {
		System.out.println("Olá amigo!\nQual é o seu nome?"); // Uso do println
		// TODO Auto-generated method stub

		// Ler uma string do console usando a biblioteca Scanner.
		Scanner X = new Scanner(System.in);
		String nome = X.nextLine();
		
		// Exibir uma string usando printf
		System.out.printf("Olá %s!\n", nome);
		X.close();
		
	}

}

