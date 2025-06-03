// Module Three Enum Introduction

  // Enum needs to be defined outside of the function
    // If you try to define within the function you will recieve an error
  // Enumerators allow you to do switches which is part of flow control - to be covered in future

enum colours {red,blue,orange}

void main(List<String> arguments) {

  print(colours);
  // This command just prints out the word colours in the terminal

  // Notice how there's no runtime type, therefore use the following command to print the values out:
  print(colours.values);
    // Produces the following in the command terminal: [colours.red, colours.blue, colours.orange]

  // To print individual values: 
  print(colours.blue);

}
