import 'package:flutter/material.dart';

void main() {
  runApp( MaterialApp(
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

  String _value = '';

  void _onChange(value) {
  setState(() {
    _value = 'Change: $value';
  });
  }

  void _onSubmit(value) {
    setState(() {
      _value = 'Submit: $value';
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // Scaffold is a structure in which you're going to build your
      // material application
      appBar:  AppBar(
        title: Text('Name Here'),
      ),
      body:  Container(
        padding:  EdgeInsets.all(32.0),
        child:  Center(
          child:  Column(
            children: <Widget>[
               Text(_value),
               TextField(
                decoration:  InputDecoration(
                  labelText: 'Hello',
                  hintText: 'Hint',
                  icon:  Icon(Icons.people)
                ),
                autocorrect: true,
                autofocus:  true,
                keyboardType: TextInputType.text,
                onChanged: _onChange,
                onSubmitted: _onSubmit,
              )
            ],
          ),
        ),
      ),
    );
  }
}