A sample command-line application with an entrypoint in `bin/`, library code
in `lib/`, and example unit test in `test/`.

# Folder Structure Definitions

1. .pub is for packages and plugins
2. bin, this will be your code
    - The "bin" folder is a convention for storing binary files, which are executable files (like programs or applications)
    - contains main.dart
3. lib is libraries and additional code

# File Definitions

1. pubspec.yaml is a way contain project settings and dependencies

# main.dart Structure

The file imports the following in the first line of the application: import 'package:udemy_dart_module_one/udemy_dart_module_one.dart' as udemy_dart_module_one;

Breaking the statement down: 

- import means you're taking something from another file 
    - Here we're importing a package
- The package is udemy_dart_module_one/udemy_dart_module_one.dart 
    - So the import here is actually a file
    - name of programme is edemy_dart_module_one
    - location of file is in lib and called udemy_dart_module_one.dart
- we also set this as a variable called udemy_dart_module_one

Next we have the programme structure: 

```
void main(List<String> arguments) {
  print('Hello world: ${udemy_dart_module_one.calculate()}!');
}
```
- In the brackets are a list of parameters given to the programme when it starts 
    - these are called arguments
- {} denote a code block or a section of code
- print statement runs
    - in this case it prints udemy_dart_module_one.calculate
    - .calculate is being called from the file udemy_dart_module_one in lib

# Udemy Flutter Module Quiz and Summary

## Udemy Flutter Module One Quiz

1. Google created dart
2. Dart runs on the Web, Server and Mobile
3. Dart is strong at quick development
4. Dart has a strong community, packages and loaded framework