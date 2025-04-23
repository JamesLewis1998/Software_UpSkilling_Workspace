import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    home: MyApp(),
  ));
}
// Stateful just means remembering whats going on
// Stateful Widget itself is not actually the state

class MyApp extends StatefulWidget {
  const MyApp({super.key});
  @override
  createState() => _State();
}

class _State extends State<MyApp> {
  // A key is way of referencing the actual widget
  // above we're saying this scaffold has a key of scaffold state
    // referencing below
    // in c or c++ think of this as a pointer
  // note here the above will be available across entire application regardless of where you call it

  void _showbar (){
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Hello World')));
  }

  // snackbar meant for instant notifications or on screen displays to user e

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // Scaffold is a structure in which you're going to build your
      // material application
      appBar: AppBar(
        title: Text('Name Here'),
      ),
      body: Container(
        padding: EdgeInsets.all(32.0),
        child: Center(
          child: Column(
            children: <Widget>[
              Text('Hello World'),
              ElevatedButton(onPressed: _showbar, child: Text('Click me'))
            ],
          ),
        ),
      ),
    );
  }
}

// Note the following approach above removes the keys to reference when building the app and implements scaffold messenger instead post deprecation of .showsnackbar