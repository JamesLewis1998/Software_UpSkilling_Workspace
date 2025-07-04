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

  // Floating action button - you actually can't see it immediately off
  // our scaffold
  // a circular, prominent button, typically placed in the bottom-right corner of the screen,
  // that promotes the primary action in the app, such as creating, sharing, or navigating

class _State extends State<MyApp> {

  String _value = '';
  void _onClicked() => setState(() => _value = DateTime.now().toString());

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // Scaffold is a structure in which you're going to build your
      // material application
      appBar: AppBar(
        title: Text('Name Here'),
      ),

      floatingActionButton: FloatingActionButton(
          onPressed: _onClicked,
          backgroundColor: Colors.red,
          mini: false,
          child: Icon(Icons.timer),
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