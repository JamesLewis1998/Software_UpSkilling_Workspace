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

  bool _value1 = false;
  bool _value2 = false;

  void _onChanged1(value) => setState(() => _value1 = value);
  void _onChanged2(value) => setState(() => _value2 = value);

  // Switch just has an ON and OFF - very similar to a checkbox
  // Along with switch we also have switch list tile

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
              Switch(value: _value1, onChanged: _onChanged1),
              SwitchListTile(
                  value: _value2,
                  onChanged: _onChanged2,
                  title:Text('This is a toggle',
                    style: TextStyle(
                        fontWeight: FontWeight.bold,
                        color: Colors.red),),
                  subtitle: Text('This is a subtitle'),
              )
              ],
          ),
        ),
      ),
    );
  }
}