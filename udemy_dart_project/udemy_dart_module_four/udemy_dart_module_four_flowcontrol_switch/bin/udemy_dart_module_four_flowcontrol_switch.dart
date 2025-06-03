// Module Four Flow Control: Switch
  // For switch statement you need a variable, it does not matter which one
  // Inside of the switch statement we have various cases
  // Think of a switch statement like a giant switch board

  // Evaluation takes place in the switch scope itself 
  // Whenever you see case think, this is when the argument within the swith statement is equal to that value 
    // In example below, when case is 18, this is equiv to when age == 18 going into the function
    // default: means its none of the above
    // Break is exactly what it means, i.e. "hitting the brakes"
      // The last break brakes out of the current scope and moves into the next line of the programme

  // Note, break is a special key word where you cannot name a variable in the programme as break -> break is part of flow control

void main(List<String> arguments) {

  int age = 10; 

  switch(age){
    case 18:
      print('You are 18 - Officially an adult');
      break; 
    
    case 21:
      print('You are 21 - Can drink in America');
      break; 

    case 65:
      print('You are 65 - eligable for bus pass');
      break;

    default:
    print('Nothing special about your age');
  }
  print('Finished');
}

// One caveat to the above is that you cannot do special processing for a case of < 18 or > 18 or other conditional statements
// It has to be absolute values == to either 18, 21 or 65 in the example above.
  // This appraoch works very well with the Enums 