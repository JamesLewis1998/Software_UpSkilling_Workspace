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

class _State extends State<MyApp> {
  double _value = 0.0;
  void _setvalue(value) => setState(() => _value = value);

  // Allows user to select a range of numbers graphically using the slider in the hmi
  // Round used below to nearest integer, without it dart would allow a number to show
  // with as many DPs as it can show in the hmi (up to 15 DPs)

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
              Text('Value: ${(_value*100).round()}'),
              Slider(value: _value, onChanged: _setvalue),
            ],
          ),
        ),
      ),
    );
  }
}