import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;


//Цель: вывести частоту каждого символа в файле
//Требования:
//Игнорировать/не игнорировать регистр - опция
//Сортировка вывода по убыванию частоты
public class Main {
    private boolean isIgnoreCase = false;

    void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<String> words;

        System.out.println("Укажите путь к файлу");
        String filePath = scanner.nextLine();

        System.out.println("Игнорировать регистр? (yes/no)");
        if(scanner.nextLine().equals("yes")) {
            this.isIgnoreCase = true;
        }

        try {
            words = getSplitWords(filePath);
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
            return;
        }

        Map<String, Integer> frequencyWords = getMapFrequencyWords(words);
        printSortedWordsByFrequency(frequencyWords);
    }
    //Метод разделения строки по пробелу
    public List<String> getSplitWords(String filePath) {
        String fileContent;

        try {
            fileContent = Files.readString(Paths.get(filePath));
        } catch (Exception ex) {
            System.out.println(ex);
            throw new IllegalArgumentException("Ошибка чтения файла");
        }

        //Заменяем переходы строк на пробелы
        fileContent = fileContent.replace("\n", " ");
        //Разделяем по 1+ пробелов
        return Arrays.asList(fileContent.split("\\s+"));
    }
    //
    public Map<String, Integer> getMapFrequencyWords(List<String> words) {
        Map<String, Integer>  freequencyMap = new HashMap<>();

        for(String item : words) {
            if(this.isIgnoreCase)
                item = item.toLowerCase();
            //Если существует слово, прибавляем 1
            if(freequencyMap.containsKey(item)) {
                freequencyMap.put(item, freequencyMap.get(item) + 1);
            } else {
                freequencyMap.put(item, 1);
            }
        }

        return freequencyMap;
    }

    public void printSortedWordsByFrequency(Map<String, Integer> map) {
        List<Integer> frequency = new ArrayList<>();
        List<String> words = new ArrayList<>();
        int tempFrequency;
        String tempWord;

        for(Map.Entry<String, Integer> item : map.entrySet()) {
            words.add(item.getKey());
            frequency.add(item.getValue());
        }

        for(int i = 0; i < words.size(); i++) {
            for(int j = 0; j < words.size() - 1; j++) {
                if(frequency.get(j) < frequency.get(j + 1)) {
                    tempWord = words.get(j);
                    words.set(j, words.get(j + 1));
                    words.set(j + 1, tempWord);

                    tempFrequency = frequency.get(j);
                    frequency.set(j, frequency.get(j + 1));
                    frequency.set(j + 1, tempFrequency);
                }
            }
        }

        for(int i = 0; i < words.size(); i++) {
            System.out.printf("%s: %d\n", words.get(i), frequency.get(i));
        }
    }
}