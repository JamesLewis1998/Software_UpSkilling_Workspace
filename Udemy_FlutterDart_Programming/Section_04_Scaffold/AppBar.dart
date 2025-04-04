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

  // Remember when you see build in the widget below this means we're going to
  // build something in the app or actually render something on the screen
  // Below we're actually rending the scaffold because we're returning it
    // In the scaffold we have an Appbar and a body

  // What does the Appbar do?
    // More than simple decoration - can put host of functionality in there

class _State extends State<MyApp> {

  int _value = 0;

  void _add() => setState(() => _value++);
  void _remove() => setState(() => _value--);


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // Scaffold is a structure in which you're going to build your
      // material application
      appBar: AppBar(
        title: Text('Road to Regionals'),
            backgroundColor: Colors.red,
        actions: [
          IconButton(onPressed: _add, icon: Icon(Icons.add)),
          IconButton(onPressed: _remove, icon: Icon(Icons.remove)),
        ],

      ),
      body: Container(
        padding: EdgeInsets.all(32.0),
        child: Center(
          child: Column(
            children: <Widget>[
              Text('Make Money'),
              Text(_value.toString(), style: TextStyle(
                fontWeight: FontWeight.bold, fontSize:  37.0
              ),)
            ],
          ),
        ),
      ),
    );
  }
}