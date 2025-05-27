
// main entry point
main(List<String> arguments) {
  bool? isOn; // this is a variable - something that will change, opposite to this is a constant
  bool isDog = false; 

  // We have diff data types 
    // 1. Bool means true or false

  // Following command will fail 
    // Everything in dart is an object
    // But an instance of an object means the object actually exists and is running in memory, null means
    //  it is simply not there

  // print(isOn); // Returns Error: isOn must be assigned before it can be used

  // Demonstration of a changing variable
    // The $ sign and brackets means to run the code in the print statement
    // Note below the variable needs assigning - dart has in updates declared null is no longer a subtype
      // therefore no type of null is permitted except from the null class
      // to form into the null class we need to define bool? above this is one of the nullable types that permit null

  
  print('isOn = ${isOn}');

  isOn = true;
  print('isOn = ${isOn}');

  isOn = false;
  print('isOn = ${isOn}');

  // Everything is an object as illustrated by isOn followed by . to expose functions following this

  }
