# turing_machine
### Иммитация работы машины Тьюринга
На вход программе подаются 4 файла:
1. alfabet.txt - алфавит в машине, по нему идет проверка допустимости символов в правилах и ленте
2. commands.txt - список команда, составляемый по виду: значение текущего состояния (0-9), текущий символ, знак больше (>), следующее состояние (0-9), новое значение текущего символа, пермещение указателя (R/L)
3. tape.txt - лента входных данных
4. result.txt - процесс работы и результат

На выходе программа отдает значения в файле results.txt в виде:
- Текущая итерация
- Текущая лента
- Указатель на положение в ленте
- Исполняемая команда
- Новая лента
- Новое положение

У программы есть один значительный недочет, замеченный довольно поздно - из-за особенности чтения команды (посимвольно), программа не будет правильно воспроинимать команды со значением состояния более 9. Решается это заменой чтения состояния посимвольно на чтения первого состояния за один символ до ">", так мы отсечем символ который подразумевается как текущий, и чтение второго состояния за один символ до значения перехода вправо или влева, по аналогии с первым.

---

### Emulation Turing machine
4 files are submitted to the program for input:
1. alfabet.txt - the alphabet is in the car, it is used to check the validity of characters in the rules and the tape
2. commands.txt - a list of commands, compiled by type: the value of the current state (0-9), the current character, the greater sign (>), the next state (0-9), the new value of the current character, pointer displacement (R/L)
3. tape.txt - input data tape
4. result.txt - the process of work and the result

At the output, the program returns the values in the file results.txt in the form of:
- Current iteration
- Current tape
- Pointer to the position in the tape
- Executable command
- New feed
- New position

The program has one significant flaw, noticed quite late - due to the peculiarity of reading the command (character-by-character), the program will not correctly receive commands with a state value greater than 9. This is solved by replacing reading the state character-by-character with reading the first state one character before ">", so we will cut off the character that is meant as the current one, and reading the second state one character before the value of the transition to the right or left, by analogy with the first.
