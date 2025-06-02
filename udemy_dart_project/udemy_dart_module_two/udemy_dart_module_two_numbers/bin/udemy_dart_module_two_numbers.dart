import 'package:udemy_dart_module_two_numbers/udemy_dart_module_two_numbers.dart' as udemy_dart_module_two_numbers;

// Module Two: Numbers
  // Var -> something that will change
  // bool -> is a type

  // Dart comes with generic num type -> num 
    // int -> no decimal place
    // double -> decimal place

  // Note if anything is incorrectly allocated across num, int or double
    // dart will underline the incorrect allocation in red
    // eg people being assigned int and made = to 'people' (string)

  // Every line ends with semi-colon which is how dart knows you are finished with the statement

main(List<String> arguments) {

  var age = 34;
  int people = 6;
  double temp = 32.06;

  // Parsing an integer
    // Make a variable called test which is an int and assign it to int.parse
    // int.parse -> calling a function inside of that  
  int test = int.parse('12');
  print(test);

  // Correct type needs to be assigned to be able to parse appropriately: 
    // () is called an anonymous function
  
  // Tried using the following command: 
  // int err = int.parse('12.09', onError: (source) => null);
  // print(err);
      // Returns the following: The value 'null' can't be returned from a function with return type 'int' because 'int' is not nullable.
      // onError has also been deprecated -> use int.tryparse

  // Use this instead: 
    // err taking int class, calling the parse function, giving it an argument then saying if err doesn't work print statement
  var err = int.tryParse('12.09');
  if (err == null)
    {
      print('could not be parsed');
    }

  // int, num and doubles are our types and you can use them, note you can also parse from strings

  // Example:

  int dogyears = 7; 
  int dogage = age*dogyears;
  print('Your dog is $dogage');
}

  // In programming, "parse" means to analyze and convert a piece of data, often text, into a usable format or structure. 
  // It's like breaking down a sentence into its parts (words, nouns, verbs) to understand its meaning. 
  //In computer science, it's commonly used in the context of analyzing source code or data formats to determine their structure and meaning. 