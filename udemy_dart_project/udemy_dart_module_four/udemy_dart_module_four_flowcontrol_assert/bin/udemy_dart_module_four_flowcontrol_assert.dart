// Module Four Flow Control: Assert
  // Easiest type of flow control is assert 
  // Assert determines whether something is true

void main(List<String> arguments) {
  print('starting');
  int age = 43;
  assert( age == 43);
  print('finish');

// The above runs as expected, now change the age to unsatisfy the argument 

  print('starting');
  int age1 = 15;
  assert( age1 == 43);
  print('finish');

// _AssertionError is then shown in the terminal, note this is similar to throwing an error
  // "throwing errors in dealing with assertions is a lot like hitting the brakes in a car"
}
