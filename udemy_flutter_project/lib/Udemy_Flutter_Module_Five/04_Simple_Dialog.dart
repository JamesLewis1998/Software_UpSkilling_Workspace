import 'package:flutter/material.dart';
import 'dart:async';

// Here we display a dialog with a list of options, allow the user to select an option
// and then display it back

// Working with async functions therefore need to import async package

// Future represents a computation that doesn't complete immediately

//

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

// Notice enum is outside of class
enum Answers{YES,NO,MAYBE}

class _State extends State<MyApp> {
  String _value = '';
  void _setValue(String value) => setState(() => _value = value);

  Future _askUser() async {
    switch(
        await showDialog(
          context: context,
          builder: (BuildContext context) {
            return SimpleDialog(
              title: Text('Do you like flutter?'),
              children: <Widget> [
                SimpleDialogOption(child: Text('Yes!!'),onPressed: (){Navigator.pop(context, Answers.YES);},),
                SimpleDialogOption(child: Text('No :('),onPressed: (){Navigator.pop(context, Answers.NO);},),
                SimpleDialogOption(child: Text('Maybe :|'),onPressed: (){Navigator.pop(context, Answers.MAYBE);},),
            ],
          );
        }
      )
    ) {
      case Answers.YES:
        _setValue('Yes');
        break;
      case Answers.NO:
        _setValue('No');
        break;
      case Answers.MAYBE:
        _setValue('Maybe');
        break;
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
              ElevatedButton(onPressed: _askUser, child: Text('Click me'))
            ],
          ),
        ),
      ),
    );
  }
}
