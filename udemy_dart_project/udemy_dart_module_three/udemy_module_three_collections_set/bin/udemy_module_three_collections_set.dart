// Module Three Collections: Set Overview
  // Sets are unordered, they do not contain duplicates
  // They are very similar to a list 
  // Have brackets with an E to define specifc types
void main(List<String> arguments) {
  
  Set<int> numbers = Set();
  
  numbers.add(1);
  numbers.add(2);
  numbers.add(3);
  numbers.add(1); //added twice
  
  print(numbers);

  // Output in terminal:
  // {1, 2, 3} -> because 1 is added twice, the second entry is ignored and not added into the set
}
