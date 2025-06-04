// Module Four Flow Control: Loops 
  // Start of section by creating some variables to use with the loop

  // If you want the function to run at least once, use do 
  // If you want it to evaluate first before doing any running use while

void main(List<String> arguments) {
  int value;
  int init = 1;
  int max = 5;

  value = init;

  // Example One: Evaluate the expression at the end
  do {
    print('Value in do loop is $value');
    value++;
  } while(value < max);
  print('Done with the do loop');

  value = init;                   // need to respecify value because loop will increase to value above

  // Example Two: Evaluate the expression at the start 
  while(value < max) {
    print('Value in the while loop is $value');
    value++;
  } 
  print('Done with while loop');

  // Infinite Loops:
  value = init;
  do{
    print('Value = $value');
    value++;

    if(value == 3){
      print('function will continue');
      continue;
    }

    if(value == 5){
      print('function will stop');
      break;
    }

  } while(true);

  print('Programme Finished');
    // Common coding mistake above - we've accidently created an infinite loop
    // this is always going to execute because we don't have a value in the brackets of while
      // all we have is the value true
      // the do loop will therefore run infinitely

    // Therefore when we run the programme it executes infinitely in the terminal until we forcefully stop it
    // In order to fix the above, we need to add in some flow control using continue and break
      // Add in the condition where we continue if the value == 10 but break if value is 15
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
