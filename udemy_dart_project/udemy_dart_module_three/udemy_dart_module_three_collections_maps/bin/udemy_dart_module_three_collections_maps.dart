// Module Three Collections: Maps 
    // Maps consist of key value pairs
    // Hence why when you go to type Map, the programme shows Map() -> K + V
void main(List<String> arguments) {

Map family  = {'dad' : 'bryan', 'wife':'ann','daughter':'sophie','son':'ben'};
print(family);
  // Key and value broken down between commas, key == dad, value == bryan

print('keys are ${family.keys}');
print('values are ${family.values}');

// In order to access the values for the associated keys you would do the following
print('dad is ${family['dad']}');
print('son is ${family['son']}');
print('wife is ${family['wife']}');

// Maps allow you to add things to a collection without knowing their index and call upon their values by the use of their keys

// Another way to do this is to specify the following: 
Map<String, String> people = Map();
  // Now we can programmatically add things into the above:

people.putIfAbsent('dad', ()=> 'Bryan');
// In the above example we're creating an annonymous function and adding the value 'Bryan'
people.putIfAbsent('wife', ()=> 'ann');
people.putIfAbsent('son', ()=> 'Ben');
print(people);

print('daughter is ${people['daughter']}');
// Will return daughter is null because daughter is not defined or injected into the people Map

}
