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

  // Note widgets are the fundamental building blocks of the user interface, acting
  // as immutable descriptions of UI elements, from simple text to complex layouts

  // Column is part of layout which we'll cover later but this just helps us move
  // things round on the screen

class _State extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // Scaffold is a structure in which you're going to build your
      // material application
      appBar: AppBar(
        title: Text('Name Here'),
      ),
      drawer: Drawer(
        child: Container(
          padding: EdgeInsets.all(32.0),
          child: Column(
          children: <Widget>[
            Text('Hello World'),
            ElevatedButton(onPressed: () => Navigator.pop(context), child: Text('Close'))
            // Fat arrow this over to navigator
            // Navigator. pop just closes the drawer
            // With text added in for on close
          ],
          ),
        )
      ),

      body: Container(
        padding: EdgeInsets.all(32.0),
        child: Center(
          child: Column(
            children: <Widget>[Text('Hello World')],
          ),
        ),
      ),
    );
  }
}