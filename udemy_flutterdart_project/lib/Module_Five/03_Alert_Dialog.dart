import 'package:flutter/material.dart';
import 'dart:async';


  // Alert Dialog exactly as it sounds - just a dialog that pops up to user


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

  Future _showAlert(BuildContext context, String message) async{
    return showDialog(
        context: context,
        builder:
            (BuildContext context) => AlertDialog(
              title: Text(message),
              actions: <Widget> [
                TextButton(
                    onPressed: () => Navigator.pop(context),
                    child: Text('ok')
            )
              ]
        )
    );
  }

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
            children: <Widget>[Text('Hello World'),
            ElevatedButton(onPressed: () => _showAlert(
                context, 'Do you like the application'),
                child: Text('Click me'))],
          ),
        ),
      ),
    );
  }
}
