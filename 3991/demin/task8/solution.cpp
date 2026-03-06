#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <ostream>
#include <string>
#include <sys/types.h>
#include <random>
#include <time.h>
#include <chrono>

#define DIGIT_CODE_MIN 49 
#define DIGIT_CODE_MAX 57
#define LETTER_CAPITAL_CODE_MIN 65 
#define LETTER_CAPITAL_CODE_MAX 90 
#define LETTER_LOWER_CODE_MIN 97 
#define LETTER_LOWER_CODE_MAX 122 


//gives a random number in range from min to (max-1)
uint32_t randomInt(uint32_t min, uint32_t max)
{
  return min + (rand() % (max - min));
}

const std::string specials = "$%^*#@!+=";
int main()
{
  int length;
  std::cout << "Введите длинну пароля" << std::endl;
  std::cin >> length;
  std::string password = "";
  std::cout << "Включать цифры? 1 - да 0 - нет" << std::endl;
  std::cout << "Включать спецсимволы? 1 - да 0 - нет" << std::endl;
  int d;
  int symb;
  std::cin >> d >> symb;
  for(size_t i = 0; i < length; i++)
  {
    auto const now = std::chrono::system_clock::now();
    time_t nowTime = std::chrono::system_clock::to_time_t(now); 
    srand(time(&nowTime) + i * rand());
    if(d || symb)
    {
      uint32_t choise = randomInt(0 , 3);
      if(choise == 2 && !symb) choise = 1;
      if(choise == 1 && !d) choise = 2;
      uint8_t letter;
      uint8_t isBig = static_cast<uint8_t>(randomInt(0, 2));
      uint8_t digit;
      size_t special;
      switch(choise)
      {
        case 0:
          letter = static_cast<uint8_t>(randomInt(LETTER_LOWER_CODE_MIN, LETTER_LOWER_CODE_MAX));
          if(isBig) letter = static_cast<uint8_t>(randomInt(LETTER_CAPITAL_CODE_MIN, LETTER_LOWER_CODE_MAX));
          password.push_back(letter);
          continue;
          break;
        case 1:
          digit = static_cast<uint8_t>(randomInt(DIGIT_CODE_MIN, DIGIT_CODE_MAX));
          password.push_back(digit);
          continue;
          break;
        case 2:
          special = specials[static_cast<size_t>(randomInt(0,specials.length()))];
          password.push_back(special);
          continue;
          break;
      }
    }
    uint8_t letter;
    uint8_t isBig = randomInt(0, 2);
    letter = randomInt(LETTER_LOWER_CODE_MIN, LETTER_LOWER_CODE_MAX);
    if(isBig) letter = randomInt(LETTER_CAPITAL_CODE_MIN, LETTER_CAPITAL_CODE_MAX);
    password.push_back(letter);
  }
  std::cout << "Пароль: " << password << std::endl;
  return 0;
}
