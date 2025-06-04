// Module Four Flow Control: Loops 
  // Start of section by creating some variables to use with the loop

void main(List<String> arguments) {
  int value;
  int init = 1;
  int max = 5;

  value = init;

  do {
    print(value);
    value++;
  } while(value < max);
  print('Done with the loop');

  print(value);
  value = init;                   // need to respecify value because loop will increase to value above

}

  // Do and while functions used above
    // init in the above is set to value 1
    // max is set to value 5 
    // Block of code is essentially, do this block of code until we tell you to stop 
      // the stop trigger comes from the while statement
      // while the while expression is false, the do code scope continues to run
        // the minute the while expression becomes true the do function ceases to execute

// Within the Do function: 
  // print the function in the terminal 
  // value is then incremented with the ++
  // do function then checks to see if the condition is still true
    // once the threshold is met the function then exits and prints the Done with the loop statement
