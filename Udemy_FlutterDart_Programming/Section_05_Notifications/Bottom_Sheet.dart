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

// Modal -> means its the only thing that can be active in the application
// concept of a builder in flutter means you're going to have code generate
// the code

class _State extends State<MyApp> {
  void _showBottom() {
    showModalBottomSheet<void>(
        context: context,
        builder: (BuildContext context) {
          return Container(
            padding: EdgeInsets.all(15.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Text('Some info here', style:
                TextStyle(color: Colors.red,
                  fontWeight: FontWeight.bold,),),
                ElevatedButton(onPressed: () => Navigator.pop(context),
                  child: Text('Close'),)
              ],
            ),
          );
        }
    );
  }

  // Modal is a term that says its the only thing that can be active in
  // the application
  // Builder in flutter is a concept where code generates the code

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
            children: <Widget>[Text('Add Widgets Here'),
            ElevatedButton(onPressed: _showBottom, child: Text('Click Me') )
            ],
          ),
        ),
      ),
    );
  }
}