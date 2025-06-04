// Module Four: Flow Control
  // "if statement a lot like steering a car"
  // Notice how on the if statement below we keep the output from the condition on the same line

void main(List<String> arguments) {
  int age = 25;
  if(age ==43) print('You are 43');
  if(age !=43) print('You are not 43');

  // Nestled IFs
    // Everything inside the {} brackets will run

  if(age < 18){
    print('You are a minor');
    if(age<13) print('You are not even a teenager');
  }

  if(age > 65){
    print('You are a senior');
    if(age > 102) print('You are ancent');
  }

  // Now consider else statements:
  if(age == 21) {
    print('This is your special year');
  } else { 
    print('This is just a normal year');
    if(age < 21){
      print('You are a minor');
    } else{
      print('You are an adult');
    }
  }

  // In the above example, nestle if statements can be added into the else statement
    // so in the above example if the age is 10 This is just a normal year and You are a minor are printed into the terminal

}

// Example One: Age is set == to 103
  // first if statement is false
  // second if statement returns true
  // then move onto if age> 65, also returns true
    // therefore prints senior statement
    // then age> 102 also true therefore prints accent statement

// Example Two: Age set to == 56
  // the only if statement to be evaluated to be true is the != 43 years old

// The above is called polymorphic code, meaning that it can change based on the input it is given