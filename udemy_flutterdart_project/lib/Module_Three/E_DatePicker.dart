import 'package:flutter/material.dart';
import 'dart:async';

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

// Remember some of this code will be running on slower cell phones
// so don't want to pick the first date as the beginning of time

class _State extends State<MyApp> {

  String _value = '';

  Future _selectDate() async {
    DateTime? picked = await showDatePicker(
      context: context,
      initialDate: DateTime.now(),
      firstDate: DateTime(2024),
      lastDate: DateTime(2027),
    );
    if (picked != null) {
      setState(() => _value = picked.toString());
    }
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
              children: <Widget>[
                Text(_value),
                ElevatedButton(onPressed: _selectDate, child: Text('Click me'))
              ],
            ),
          ),
        ),
      );
    }
  }