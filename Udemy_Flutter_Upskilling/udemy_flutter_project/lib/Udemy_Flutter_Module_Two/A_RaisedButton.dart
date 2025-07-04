import 'package:flutter/material.dart';

void main() {
  runApp(new MaterialApp(
    home: new MyApp(),
  ));
}
// Stateful just means remembering whats going on
// Stateful Widget itself is not actually the state

class MyApp extends StatefulWidget {
  @override
  _State createState() => new _State();
  // Here myApp is creating a state which extends myApp
}

class _State extends State<MyApp> {

  String _value = 'Hello World';

  void _onPressed() {
    setState(() {
      _value = 'My name is';
    });
}

  @override
  Widget build(BuildContext context) {
    // Anytime you see WidgetBuild think render - ie you're rending something to the screen
    return new Scaffold(
      // Scaffold is a structure in which you're going to build your
      // material application
      appBar: new AppBar(
        title: new Text('Name Here'),
      ),
      body: new Container(
        padding: new EdgeInsets.all(32.0),
        child: new Center(
          child: new Column(
            children: <Widget>[
              new Text(_value),
              new ElevatedButton(onPressed: _onPressed,
                      child: Text('Click me'),),
          ],
          ),
        ),
      ),
    );
  }
}
