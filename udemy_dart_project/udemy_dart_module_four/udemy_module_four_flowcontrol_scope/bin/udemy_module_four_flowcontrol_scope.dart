// Module Four Flow Control: Scope
  // Scope is where a variable lives
  // Remember variables are things that will change
    // Hit the brakes using assertions and throwing errors
    // steer the car using the if statements
    // But variables have a short lifecycle 
void main(List<String> arguments) {
  int age = 56;
  
  // Age variable above exists in entire main scope {}
    // Every time you see {} brackets just thing this is scope
    // Is simply a bubble a variable can live in 
  
  // Below made another variable within specific scope following else statement
    // Note the variable has to be used in the scope within which it is declared
    // In the case below, hasBills is defined in the subscope, within the scope of if age == 43

  // So in the example below if we wanted to use hasBills across the whole programme, we'd need to move it into the main
  // scope, ie directly under line 8 to make sure its contained in the scope of main

  if(age == 43){
    print('You are 43');
  } else {
    bool hasBills = true;
    print('You are $age and has bills is $hasBills');

  }
}