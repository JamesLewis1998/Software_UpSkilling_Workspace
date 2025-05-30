
// Module Two: Strings
  // See example below of strings and various uses with print statements

main(List<String> arguments) {

String hello ='hello world'; 
print('Hello world');
print(hello);

String name = 'James Dickinson';

print('my name is $name');

// Substring example: Indexing via numbers 
String firstname =name.substring(0,5);
String surname = name.substring(6,15);
print('$firstname $surname');
  // substring([],[]) -> [] is the indexing used to determine where to start and end the extraction

// Substring: Indexing via indexOf
int index = name.indexOf(' ');
String lastname = name.substring(index).trim();
print('$lastname');
  // Trim used to remove any additional spaces
  // indexOf() - in the brackets this is the value who's index is searched for in the list

// Length
print(name.length);

// Search statements
print(name.contains('J'));
  // returns true

// Lists
List parts = name.split(' ');
print(parts);
print(parts[0]);
print(parts[1]);

  // Indexing the list above - notice the similiarities between dart and python as a language

}
