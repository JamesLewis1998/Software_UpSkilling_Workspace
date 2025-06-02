import 'dart:io';
main(List<String> arguments) {
  stdout.write('What is your name?\r\n');
  String name = stdin.readLineSync()!;
  print('Your name is');
  name.isEmpty ? stderr.write('Name is empty') : stdout.write('Hello ${name} :) \r\n');
}

// Udemy Dart Module Two: User Input
  // io package allows for input/output which is what we'll be working with
  // async allows for imports for synchronous and asynchronous operations
    // asychronous operations are things that can be done at the same time
      // a lot of io in dart is asychronous
      // Note this creates a little bit of a problem considering we're working a sychronously:
        // Namely because we want things to happen in a certain order

    // NOTE!!! stdout.write() in Dart has apparently been altered from sync to async therefore no longer require
      // asynch import

  // Work with standard out: 
    // write('what is your name? \r\n');

      // the \r\n is an escape sequence slash slash n depending on your operating system
      // when press enter on keyboard, 1 or 2 character is printed out but you dont see them
        // r == hard return
        // n == new line feed

    // stdout.write('what is your name?');
    // stdout.write('what is your name? \r\n');

  // If you omit the above you end up with the following in the command window: 
    // what is your name?what is your name? 
    // when you add r and n in you'll see it breaks this up into multiple lines

  // So standard out is similar to print but there are some caveats you need to be aware of
    // this reads a line of input from the user syncrhonously meaning it will block your programme from executing until that
    // function has executed
      // when user enters value into screen, dart will then inject that value into the name variable

  // String? name = stdin.readLineSync();
  // print(name);
  // stdout.write('Hello $name');

// What do you do if the user does not enter a value
  // use sterr == standard error, along with standard input output to write different values into the command terminal based on
  // user input
  // Only time we use these in dart is standard inputs for console applications

// NOTE!!! 
  //dart debug console in vs code does not allow for user inputs, you therefore need to change the dart extension settings to 
  // run in the terminal rather than the CLI console where commands are excepted