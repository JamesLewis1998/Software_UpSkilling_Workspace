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
}

class _State extends State<MyApp> {

  String _value = 'Hello World';

  void _onPressed(String value) {
    setState(() {
      _value = value;
      // Setting our Private Value to the function value
      // Private value is _value
      // Function value is value in brackets of _onPressed Function
    });
    }

  @override
  Widget build(BuildContext context) {
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
              new ElevatedButton(onPressed: () => _onPressed('Hello James'),
                // Here we're making an anonymous function that returns the onPressed with Hello James
                child: Text('Click me'),),
            ],  
          ),
        ),
      ),
    );
  }
}
