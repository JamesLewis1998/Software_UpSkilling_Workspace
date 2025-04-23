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

  int _value1 = 0;
  int _value2 = 0;

  // Remember to refactor code the way we did in past as follows:
  void _setValue1(value) => setState(() => _value1 = value);
  void _setValue2(value) => setState(() => _value2 = value);

  // Rather than adding some controls into the child we're going to create
  // some functions to add in the controls this way rather than in children below

  Widget makeRadios(){
    List<Widget> list = <Widget> [];

    for(int i = 0; i < 3; i++ ) {
      // Above we're incrementing i (see ++)
      list.add(Radio(
          value: i,
          groupValue: _value1,
          onChanged: _setValue1,
          activeColor: Colors.red,
      ));
    }
    Column column = Column(children: [...list],);
    return column;
  }

  // Notice the difference between the radios and radio tiles in the emulator
  // Also pay attention to the difference in the position between the two with the first set
  // in the centre and the second set located on the left

  Widget makeRadioTiles(){
    List<Widget> list = <Widget> [];

    for(int i = 0; i < 3; i++ ) {
      // Above we're incrementing i (see ++)
      list.add(RadioListTile(
          value: i,
          groupValue: _value2,
          onChanged: _setValue2,
          activeColor: Colors.green,
          controlAffinity: ListTileControlAffinity.trailing,
          title: Text('Item: $i'),
          subtitle: Text('subtitle: '),
      ));
    }
    Column column = Column(children: [...list],);
    return column;
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
              makeRadios(),
              makeRadioTiles(),
            ],
          ),
        ),
      ),
    );
  }
}