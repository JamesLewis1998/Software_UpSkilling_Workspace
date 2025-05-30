
// main entry point
main(List<String> arguments) {
  var isOn; // this is a variable - something that will change, opposite to this is a constant
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

  print('isOn is a ${isOn.runtimeType} runtime type');

  // runtime type vs variable 
    // var means its a generic object
    // runtime type is a mechanism that allows the type of an object to be determined during program execution

  // In computer programming, a variable is a storage location in memory that holds a value, 
  // while a runtime type refers to the actual type of the data stored within that variable at the moment the program is executing

  isOn = 5;
  print('isOn is a ${isOn.runtimeType} runtime type');

  // Defined isOn as Var in programme, then change the definition of the variable from bool to int during run time
  // In terminal prints out isOn as bool then int runtime type

  }
