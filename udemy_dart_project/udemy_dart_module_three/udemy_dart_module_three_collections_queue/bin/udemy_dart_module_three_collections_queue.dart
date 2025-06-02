//Module Three Collections: Queue
  // Queues: think about queues as a line
  // Not part of the standard library so we have to import it
  // Queues are ordered and very quick in memory 
    // they are ordered, no index and add and remove from start and the end 
      // there's no ordering with these, you have to add or remove from the end, you can't add or remove from the middle 

import 'dart:collection';
void main(List<String> arguments) {

Queue items =Queue();
items.add(1);
items.add(2);
items.add(3);
items.add(4);
items.removeFirst();
items.removeLast();
print(items);

// Only thing left is {2,3} because we've removed the first and the last item being 1 and 4

}
