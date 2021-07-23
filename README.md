# AutomatedTesting

Simple testing program for c++ files. After you've inputted tests and right answers for them, you need to press just one button to retest.

Things to know:
1. The testing system uses g++, so check if it is installed with 'g++ --version'.
2. The main method in your c++ file should start with 'int main(', without any additional words between those. Spaces are allowed:). For example:
   - "int main(){"
   - "    int  main(int argc,  char     \*argv[]) {"
   - "int main () {"
 
   are ok, but "Int lol Main(){" is not.
3. Testing system uses file input/output for testing, so It most probably will work incorrectly if your program uses file IO.
4. While testing, the system is ignoring:
   - empty lines;
   - spaces in the beginning and in the end of lines.
5. You can change output colors in 'colors.py'.

Working format:
1. Run program. 

   ![Run program](https://i.ibb.co/3YkfKLP/Run-program.png)
2. Input path (can be absolute or relative) to c++ file.

   ![Absolute path](https://i.ibb.co/Jt4nQXD/Abs-Path-Censored.png) or ![Relative path](https://i.ibb.co/qd37J5N/2021-07-23-13-40-29.png)
3. Input number of tests, for each test confirm program answer or input right answer.

   ![Inputting tests](https://i.ibb.co/XztMtV9/image.png)
4. If needed, change your source code; input 'r' to rebuild, '+' to add test, 'c' to continue to the next problem or 'q' to quit.

   ![Retest](https://i.ibb.co/qNLFT35/2021-07-23-13-52-22.png)
  
   ![Add](https://i.ibb.co/xGrnbJH/2021-07-23-13-54-01.png)

That's all, good luck:)
