// Module Three Collections: Lists
  // List is the king of collections
  // Declare variable type of a list, then assign it square brackets

void main(List<String> arguments) {

List test = [1,2,3,4];
// Above creating a list in memory and then assigning this list against the variable test

// Lists are really useful for:
  // assigning variables to them such as 

print('List $test');

print('Length = ${test.length} '); // How many items there are in the list
print('First Item = ${test[0]} ');    // Print the first item in that list, index as 0 (zero based index meaning first item will always be zero)
print(test.elementAt(3)); //Returns the number 4 because its in the third position, due to zero based indexing

// Note if you try to go above the above you'll get an error: 
// print(test.elementAt(16));
  // Returns range error: RangeError (length): Invalid value: Not in inclusive range 0..3: 16

// Note in the above example, need to use {} brackets to contain all arguements needed in one
  // first one being test.length 
  // second one being test[0] 
  // Whereas in example one we just need to definfe $ without the brackets because there's no argument extensions added to list

// Another Example: Create a new list: 
List things = List.empty(growable: true);
  // Note growable means the list can grow from a starting size of zero items
things.add(1);
things.add('cats');
things.add(true); 
  // Three separate values above, int, string and bool
print(things);

// To define a list with number entries only: 
List<int> numbers = List.empty(growable: true);

// numbers.add(true);
  // Above will return an error: arguement type bool can't be assigned to parameter type
numbers.add(1);
numbers.add(2);
numbers.add(3);
print(numbers);
}
