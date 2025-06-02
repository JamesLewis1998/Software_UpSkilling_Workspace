// Module Two: Const Variables
  // Understanding the difference between a constant and a variable

main(List<String> arguments) {
  String hello = 'hello';
  String world = 'world';

  // Using the + operator to append two or more strings

  print('$hello');
  print('$world');
  print(hello + ' ' + world);

  // Now add const in front of the type (String)

  const String hello1 = 'Hello';
  const String world1 = 'World';

  print(hello1 + ' ' + world1);

  // If you then try and assign world1 to a different string you then get: 
  world1 = 'James';

    // Dart explodes - giving error that constant variables cannot be assigned values
    // const means by definition if you flag a variable as a constant via const, it can never change

}
