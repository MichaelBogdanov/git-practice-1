import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    void main() {
        Scanner scanner = new Scanner(System.in);
        String inputPath = scanner.nextLine();
        List<String> splitWords;

        try {
            splitWords = getSplitWords(inputPath);
        } catch (Exception e) {
            System.out.println(e.getMessage());
            return;
        }

        System.out.println("Исходные данные");
        printStringList(splitWords);

        List<String> uniqueWords = getUniqueWords(splitWords);

        System.out.println("\nГотовые данные:");
        printStringList(uniqueWords);
    }
    //Метод разделения строки по пробелу
    public List<String> getSplitWords(String filePath) {
        String fileContent;

        try {
            fileContent = Files.readString(Paths.get(filePath));
        } catch (Exception ex) {
            throw new IllegalArgumentException("Ошибка чтения файла");
        }

        return Arrays.asList(fileContent.split(" "));
    }
    //Метод получения списка уникальных слов с сохранением их порядка
    public List<String> getUniqueWords(List<String> data) {
        List<String> uniqueWords = new ArrayList<String>();
        for(String item : data) {
            if(!uniqueWords.contains(item))
                uniqueWords.add(item);
        }

        return uniqueWords;
    }
    //Метод вывода данных списка
    public void printStringList(List<String> list) {
        for(int i = 0; i < list.size(); i++) {
            System.out.printf("%d. %s\n", i+1, list.get(i));
        }
    }
}