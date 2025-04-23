import 'package:flutter/material.dart';

void main() {
  runApp( MaterialApp(
    home:  MyApp(),
  ));
}
// Stateful just means remembering whats going on
// Stateful Widget itself is not actually the state

class MyApp extends StatefulWidget {
  @override
  createState() =>  _State();
}

class _State extends State<MyApp> {

  bool _value1 = false;
  bool _value2 = false;

  void _value1Changed(value){
    setState(() {
      _value1 = value;
    });
  }

  // Note we can refactor the above as follows in Dart:
  void _value2Changed(value) => setState(() => _value2 = value);
  // Using the => allocator to omit the squirmy brackets

  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      // Scaffold is a structure in which you're going to build your
      // material application
      appBar:  AppBar(
        title:  Text('Name Here'),
      ),
      body:  Container(
        padding:  EdgeInsets.all(32.0),
        child:  Center(
          child:  Column(
            children: <Widget>[
                 Checkbox(
                     value: _value1,
                     onChanged: _value1Changed),
                 CheckboxListTile(
                    value: _value2,
                    onChanged: _value2Changed,
                  title:  Text('Hello World'),
                  controlAffinity: ListTileControlAffinity.leading,
                  subtitle:  Text('Subtitle'),
                secondary:  Icon(Icons.archive),
                activeColor: Colors.red,
                )
              ],
          ),
        ),
      ),
    );
  }
}
